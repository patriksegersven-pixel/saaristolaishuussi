# Company name search: shortlist (registry checks pending)

Run 2026-10-08. 38 candidates in 3 batches. Raw results are in `names.json`; the checker is `check_names.py`.

## Read this first: what was and wasn't verified

This session's network egress policy **blocked every registry host**:
`avoindata.prh.fi` (YTJ), `tmdn.org` / `euipo.europa.eu` (TMview), `allabolag.se`, `bolagsverket.se`,
`rdap.org` / `rdap.fi` / Verisign / Identity Digital RDAP, and whois (port 43).

| Check | What was actually done | Strength |
|---|---|---|
| YTJ (PRH) | API call attempted → blocked. Web search of FI company directories (asiakastieto, scoris, finder, kimsalmi) | Indirect: **manual check required** |
| Trademarks 9/35/42 | TMview call attempted → blocked. Web search incl. euipo/wipo/justia | Indirect: **manual check required** |
| Swedish AB | allabolag attempted → blocked. Web search on allabolag/merinfo/hitta | Indirect: **manual check required** |
| Domains | RDAP blocked → **live DNS NS lookup** at the TLD | Real lookup. NXDOMAIN = not delegated = *very likely* free; confirm at registrar |
| Web/brand | Web search per name | Real |

So **no name is marked "viable" yet**. The list below holds the 5 strongest names that passed every check that could run.
To finish, allow the hosts above in the environment's network settings and run
`python3 check_names.py --recheck Oivaro Ennusto Stimanta Kasvanta Oivalto Svoltia`.

## Shortlist

| Name | Meaning | YTJ | Trademark | Swedish AB | .fi | .com | .ai | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Oivaro** | FI *oiva* "excellent", root of *oivallus* "insight"; Italian-sounding ending | manual. No exact hit; ⚠ stem "Oiva" in *Asumispalvelut Oiva Oy*, *Oiva Isännöinti Oy* | manual. None found on web | manual. None found | free* | free* | free* | **Shortlist #1** |
| **Ennusto** | FI *ennuste* "forecast", Italianised | manual. No hit | manual. None found; ⚠ close to descriptive word "ennuste" | manual. None found | free* | free* | free* | Shortlist |
| **Stimanta** | IT *stima* "estimate / esteem" | manual. No hit | manual. Only STIMA crypto token (other field) | manual. None found | free* | free* | free* | Shortlist |
| **Kasvanta** | FI *kasvaa* "to grow" | manual. No hit | manual. None found | manual. None found | free* | free* | free* | Shortlist |
| **Oivalto** | FI *oivaltaa* "to grasp an insight" + IT *alto* "high" | manual. Same "Oiva" stem risk | manual. None found | manual. None found | free* | taken | free* | Shortlist (pick Oivaro *or* this) |
| Svoltia | IT *svolta* "turning point" | manual. No hit | ⚠ SVOLT Energy (batteries) holds marks, class 9 | manual. None found | free* | free* | free* | Risky |
| Stimaro | IT *stima* + -aro | manual. No hit | manual. None found | manual. None found | free* | taken | free* | Backup |

\* free = no DNS delegation at the registry (live lookup); confirm at the registrar before announcing.

## Rejected and why (lessons that shaped the batches)
- **Batch 1 (real words: Stima, Spinta, Verso, Acume, Orma, Vaisto, Seula, Taimi, Senno, Ennus, Svolta, Fiuto):** every single .com was taken, and 9 of 12 .fi too, so we moved to coined Finnish+Italian blends.
- **Nousio:** *Nousua Oy* (3101890-8) is a software firm in Espoo, 2 letters away. PRH would likely reject it.
- **Kipino:** one letter from the very common "Kipinä" in company names.
- **Versoma, Taimisto, Aistima, Lumetra, Vireo, Ennova, Lumivo:** .fi taken, or both .fi and .com taken.

## Recommendation
**Oivaro**: insight and excellence in Finnish, an easy Italian sound, nothing else using it on the web, and all three domains undelegated.
Tagline: *"Oivaro: insight that compounds."*

Fallback if PRH objects to the "Oiva" stem: **Stimanta** (no stem conflict, all domains free).
