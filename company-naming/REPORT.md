# Company name search: shortlist (registry checks pending)

Run 2026-10-08. 8 batches, 102 candidates. Raw results are in `names.json`; the checker is `check_names.py`.

## Read this first: what was and wasn't verified

This session's network egress policy **blocked every registry host**:
`avoindata.prh.fi` (YTJ), `tmdn.org` / `euipo.europa.eu` (TMview), `allabolag.se`, `bolagsverket.se`,
`rdap.org` / `rdap.fi` / Verisign / Identity Digital RDAP, and whois (port 43).

| Check | What was actually done | Strength |
|---|---|---|
| YTJ (PRH) | API call → blocked. Web search of FI directories (asiakastieto, finder, scoris) | Indirect: **manual check required** |
| Trademarks 9/35/42 | TMview call → blocked. Web search incl. euipo/wipo/justia | Indirect: **manual check required** |
| Swedish AB | allabolag → blocked. Web search scoped to allabolag/merinfo/hitta | Indirect: **manual check required** |
| Domains | RDAP blocked → **live DNS NS lookup** at the TLD | Real lookup. NXDOMAIN = not delegated = very likely free; confirm at registrar |
| Web/brand | Web search per name | Real |

**No name is marked "viable" yet.** To finish, allow those hosts in the environment's network settings and run
`python3 check_names.py --recheck Scova Fiuta Scruta Margina Svela Ennusto Oivalto Stimanta`.

## Shortlist: international

| Name | Meaning | YTJ | Trademark | Swedish AB | .fi | .com | .ai | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Scova** | IT *scovare* "to unearth / ferret out": finding the hidden growth | manual; no hit (nearest *Skavo Oy*, unrelated) | manual; none found | manual; none found | free* | taken | taken: live site (likely an active startup) | Demoted |
| **Fiuta** | IT *fiutare* "to sniff out"; *fiuto* = business flair | manual; no hit | manual; none found (nearest FIYTA, watches) | manual; none found | free* | taken (parked at NameBright, likely buyable) | free* | **#1** |
| **Scruta** | IT *scrutare* "to scrutinise"; reads as "scrutiny" in EN | manual; no hit | ⚠ *Scrut Automation* (compliance SaaS, class 42), 1 letter | manual; none found | free* | taken | free* | Risky |
| **Margina** | "margin": profit-first growth (IT *margine*, SV *marginal*) | ⚠ crowded stem: *Marginum Oy*, *Margeia Oy*, *Margin Investments Oy* | manual; none found | manual; none found | free* | taken | free* | Risky (PRH) |
| **Svela** | IT *svelare* "to unveil" | manual; *Svola Oy* (salon) only | manual; none found | ⚠ identical *SveLa AB* 556525-3571 (apparently dormant) | free* | taken | taken | Risky (SE) |

## Shortlist: Finnish/Italian roots (from batches 1–3)

| Name | Meaning | .fi | .com | .ai | Note |
|---|---|---|---|---|---|
| Oivalto | Coined from FI *oivaltaa* "to have an insight" + IT *alto* | free* | taken | free* | "Oiva" stem in several Oy names |
| Ennusto | Coined; evokes FI *ennuste* "forecast" | free* | free* | free* | close to a descriptive word |
| Stimanta | Coined from IT *stima* "estimate / esteem" | free* | free* | free* | clean on web |
| Oivaro | Coined; echoes FI *oiva*. **No meaning in Finnish** | free* | free* | free* | "Oiva" stem |

\* free = no DNS delegation at the registry (live lookup); confirm at the registrar before announcing.

## What failed, and what it taught
- **Real words (Finnish, Latin or Italian, 4–6 letters):** effectively every .com is taken, and most .fi.
- **Crowded "insight" roots:** augur, presage, intuit, fulcrum and auxo are already used by analytics brands.
  Rejected: Augeo (US marketing co., class 35), Fulcra (Fulcra Dynamics data platform), Intuira (Intura data-viz),
  Auguro (AUGURI decision-support TM), Fulcrio (Fulcri Srl software), Presago (Presage Analytics), Auxeo (Auxo Software), Ascio (domain registrar).
- **Italian verbs** were the most productive seam. Rejected: Rivela (Rivelo, an Italian forecasting platform),
  Coltiva (Koltiva), Sprona (Sprana), Sondaro (Sondarö, an island and a FI company), Spicca (contains an English ethnic slur).
- **Finnish-root conflicts:** Nousio (Nousua Oy, software, Espoo), Kipino (Kipinä).

## Recommendation
**Fiuta**: Italian *fiutare*, "to sniff out"; *fiuto* is the Italian word for business flair. Five letters, said the same way
everywhere ("FYOO-ta"). No company or brand found, .fi and .ai not delegated, and the .com is parked at a domain marketplace.
Tagline: *"Fiuta: a nose for profitable growth."*

Scova was the previous #1. It was demoted because scova.ai serves a live site (IONOS DNS, A record 185.158.133.1,
believed to be app-builder hosting), so there is probably an active startup using the name.

Correction: an earlier version said Oivaro "means insight and excellence in Finnish". That was wrong; Oivaro is a coined word with no Finnish meaning.
