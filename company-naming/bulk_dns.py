import sys, json, dns.resolver
def st(d):
    try: dns.resolver.resolve(d,"NS",lifetime=8); return "T"
    except dns.resolver.NXDOMAIN: return "f"
    except Exception: return "T"
from concurrent.futures import ThreadPoolExecutor
names=sys.argv[1:]
def row(n):
    n=n.lower(); return n, {t:st(f"{n}.{t}") for t in ("com","fi","ai","se")}
with ThreadPoolExecutor(16) as ex:
    res=list(ex.map(row,names))
for n,r in sorted(res,key=lambda x:(x[1]["com"],x[1]["fi"],x[1]["ai"])):
    print(f"{n:11} com={r['com']} fi={r['fi']} ai={r['ai']} se={r['se']}")
