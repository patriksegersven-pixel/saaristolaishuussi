# Company name search: final shortlist (registry checks pending)

Updated 2026-10-08. About 190 names DNS-screened; 40+ deep-screened for conflicts. Raw data is in `names.json`.
Tools: `check_names.py` (full checker) and `bulk_dns.py` (fast domain screen).

## What was and wasn't verified
The environment's egress policy **blocks every registry**: PRH/YTJ, TMview/EUIPO, allabolag, Bolagsverket, RDAP and whois.
- **Domains:** live DNS NS lookups (.com, .fi, .ai, .se). "free" = not delegated at the TLD, so very likely unregistered; confirm at a registrar.
- **Companies, trademarks, AB:** web searches scoped to asiakastieto/finder/scoris (FI), allabolag/merinfo/ratsit/hitta (SE),
  and justia/trademarkelite/euipo (TM), including 1–2 letter variants. Indirect: **manual registry check still required.**

## Final shortlist (international)

| # | Name | Meaning | FI Oy (web) | Trademark (web) | SE AB (web) | .fi | .com | .ai | .se | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Stimanta** | IT *stima* "estimate / esteem"; echoes *diamante* / FI *timantti* (diamond) | none close; only *Stima* sole trader, Tampere | none in 9/35/42 | *STIMA AB* (Västerås, field unknown) | free | **free** | free | free | **Recommended** |
| 2 | **Stimea** | IT *stima*, shorter form | none in field (Sitema, Styma, Stremia: unrelated) | none | none close | free | for sale (Afternic) | free | free | Clean |
| 3 | **Trazia** | IT *trazione* "traction"; ES *traza* "trace" | none in field | none identical (Traze: supply-chain SaaS, US) | none in field | free | in use (hosted) | free | free | Clean |
| 4 | **Lucerio** | IT *lucerna* "lamp" / ES *lucero* "bright star": insight | none | none in 9/35/42 | ⚠ *Luceria AB* (tiny ad agency) | free | taken (GoDaddy) | free | free | Minor risk |
| 5 | **Svelia** | IT *svelare* "to unveil" | none in field | none in 9/35/42 | ⚠ *Svevia AB*, large SE road contractor, 1 letter | free | parked (investor) | free | taken | Minor risk |

Backups: Margea (identical tiny *MarGea AB* in SE), Kertio (*Kortio AB* IT, 1 letter), Tuiko (clean, but reads Finnish-only).

## Rejected after deep screen
| Name | Reason |
|---|---|
| Fiuta | *Fiuter*: Madrid AI e-commerce segmentation SaaS (same niche); "fiut" is vulgar in Polish |
| Scova | scova.ai is a live site |
| Scovia | *Scopia Oy* 3424436-1, software, Espoo (1 letter); Avaya Scopia |
| Scovara | *Skavara AB* 559240-3546, e-commerce consulting, Göteborg (near-homophone) |
| Sagira | *Sagura Oy* 3011455-1, IT consulting (1 letter) |
| Augera | crowded: *Augere AB* (info services), *Auree Oy* (software), Auger/Augeo/Augury |
| Fructio | *Fructifi* (FR retention analytics); Fructis shampoo |
| Indizia | *Indicia AB* (consulting), Indicium AI; IT *indiziato* = "suspect" |
| Ennusto | *Ennuro Oy* (consulting, 2 letters); near-descriptive "ennuste" |
| Earlier rounds | Augeo, Fulcra, Intuira, Auguro, Fulcrio, Presago, Auxeo, Ascio, Rivela, Coltiva, Sondaro, Sprona, Spicca, Nousio, Kipino (see `names.json`) |

## Lessons
- Pronounceable 4–7 letter .com domains are effectively all registered; Stimanta was the only clean one with .com free.
- "Insight" roots (augur, presage, intuit, lumen, fulcrum, scov-) are crowded with analytics brands.
- Swedish and Finnish small-company registers carry many 1-letter neighbours, so check both before filing.

## Recommendation
**Stimanta**: Italian *stima* (estimate and esteem: what the data says, and the trust it earns), with a sound that echoes
*diamante* / *timantti*. Says the same in Finnish, Swedish, English and Italian (sti-MAN-ta). It is the only name screened
that is clean on the web and has .com, .fi, .ai and .se all unregistered.
Tagline: *"Stimanta: growth you can estimate."*

Fallback: **Stimea** (shorter; .com buyable on Afternic). Mild caveat for both: English slang "stim" (stimulants or stimming).

Correction: an earlier version said Oivaro "means insight and excellence in Finnish". That was wrong; Oivaro is a coined word.

## To finish
Allow the registry hosts in the environment's network settings, then run
`python3 check_names.py --recheck Stimanta Stimea Trazia Lucerio Svelia`.
Also search TMview manually for similar marks in classes 9/35/42, and register the domains promptly.
