#!/usr/bin/env python3
"""Availability checker for company-name candidates.

Usage:  python3 check_names.py NAME [NAME ...]      (results cached in names.json)
        python3 check_names.py --recheck NAME ...   (ignore cache)

Checks per name:
  ytj      PRH open YTJ API v3 (exact + similar names, active companies)
  tm       TMview (EUIPO/TMDN) word-mark search, classes 9/35/42
  se_ab    allabolag.se search page for "<NAME>"
  domains  .fi/.com/.ai via RDAP; falls back to DNS NS delegation when RDAP is blocked

Every check records its source and status. A check that could not reach its
source is recorded as {"status": "blocked"} and must be verified manually -- it
is never treated as "free/clear".
"""
import json, sys, re, datetime, pathlib
import requests
import dns.resolver

HERE = pathlib.Path(__file__).parent
CACHE = HERE / "names.json"
TIMEOUT = 20

RDAP = {
    "fi": "https://rdap.fi/rdap/rdap/domain/{}",
    "com": "https://rdap.verisign.com/com/v1/domain/{}",
    "ai": "https://rdap.identitydigital.services/rdap/domain/{}",
}


def load():
    return json.loads(CACHE.read_text()) if CACHE.exists() else {}


def save(db):
    CACHE.write_text(json.dumps(db, indent=2, ensure_ascii=False, sort_keys=True))


def _get(url, **kw):
    try:
        return requests.get(url, timeout=TIMEOUT, **kw), None
    except requests.RequestException as e:
        return None, type(e).__name__ + ": " + str(e)[:120]


def similar(a, b):
    """Shared stem or <=2 edits -- roughly how PRH judges confusing similarity."""
    a, b = a.lower(), b.lower()
    if a in b or b in a:
        return True
    # Levenshtein distance
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] <= 2


def check_ytj(name):
    url = "https://avoindata.prh.fi/opendata-ytj-api/v3/companies"
    r, err = _get(url, params={"name": name})
    if r is None or r.status_code != 200:
        return {"status": "blocked", "source": url, "error": err or f"HTTP {r.status_code}"}
    data = r.json()
    hits = []
    for c in data.get("companies", []):
        for n in c.get("names", []):
            if n.get("endDate"):
                continue
            nm = n.get("name", "")
            stem = re.sub(r"\b(oy|ab|oyj|ltd|ky|tmi|ay)\b", "", nm, flags=re.I).strip(" .,-")
            if any(similar(name, w) for w in stem.split()) or similar(name, stem):
                hits.append({"name": nm, "businessId": c.get("businessId", {}).get("value")})
    exact = [h for h in hits if re.sub(r"\s+(oy|ab|oyj)$", "", h["name"], flags=re.I).lower() == name.lower()]
    return {"status": "conflict" if exact else ("similar" if hits else "clear"),
            "total": data.get("totalResults"), "hits": hits[:15], "source": url}


def check_tm(name):
    url = "https://www.tmdn.org/tmview/api/search/results"
    body = {"page": "1", "pageSize": "50", "criteria": "C", "basicSearch": name,
            "fOffices": ["EM", "FI", "SE", "WO"], "fNiceClass": ["9", "35", "42"],
            "fTMStatus": ["Filed", "Registered"]}
    try:
        r = requests.post(url, json=body, timeout=TIMEOUT)
    except requests.RequestException as e:
        return {"status": "blocked", "source": url, "error": type(e).__name__}
    if r.status_code != 200:
        return {"status": "blocked", "source": url, "error": f"HTTP {r.status_code}"}
    marks = [{"mark": t.get("tmName"), "office": t.get("tmOffice"), "classes": t.get("niceClass")}
             for t in r.json().get("tradeMarks", [])]
    hits = [m for m in marks if m["mark"] and similar(name, m["mark"])]
    return {"status": "conflict" if hits else "clear", "hits": hits[:15], "source": url}


def check_se_ab(name):
    url = f"https://www.allabolag.se/what/{name}"
    r, err = _get(url, headers={"User-Agent": "Mozilla/5.0"})
    if r is None or r.status_code != 200:
        return {"status": "blocked", "source": url, "error": err or f"HTTP {r.status_code}"}
    found = sorted(set(re.findall(rf"\b{re.escape(name)}[\w\s&-]{{0,30}}AB\b", r.text, flags=re.I)))
    return {"status": "found" if found else "none", "hits": found[:15], "source": url}


def check_domain(name, tld):
    dom = f"{name.lower()}.{tld}"
    r, err = _get(RDAP[tld].format(dom))
    if r is not None and r.status_code in (200, 404):
        return {"status": "taken" if r.status_code == 200 else "free", "method": "rdap"}
    # RDAP unreachable -> DNS delegation (a real lookup, but weaker evidence)
    try:
        ns = [str(x) for x in dns.resolver.resolve(dom, "NS", lifetime=10)]
        return {"status": "taken", "method": "dns", "ns": ns[:2]}
    except dns.resolver.NXDOMAIN:
        return {"status": "likely_free", "method": "dns",
                "note": "no DNS delegation; RDAP unreachable -> confirm at registrar"}
    except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return {"status": "taken", "method": "dns", "note": "name exists in DNS"}
    except Exception as e:
        return {"status": "error", "method": "dns", "error": type(e).__name__}


def check(name):
    return {
        "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "ytj": check_ytj(name),
        "tm": check_tm(name),
        "se_ab": check_se_ab(name),
        "domains": {t: check_domain(name, t) for t in RDAP},
    }


def main(argv):
    recheck = "--recheck" in argv
    names = [a for a in argv if not a.startswith("--")]
    db = load()
    for n in names:
        key = n.capitalize()
        entry = db.setdefault(key, {})
        if "auto" in entry and not recheck:
            print(f"{key}: cached")
            continue
        entry["auto"] = check(n)
        save(db)
        a = entry["auto"]
        d = " ".join(f".{t}={v['status']}" for t, v in a["domains"].items())
        print(f"{key:10} ytj={a['ytj']['status']:8} tm={a['tm']['status']:8} se={a['se_ab']['status']:8} {d}")


if __name__ == "__main__":
    main(sys.argv[1:])
