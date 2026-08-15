# Kronos 3D Model — GitHub upload set

Upload the **entire contents of this folder** (preserving the subfolders) to the repo **`KronosFE/3D_Model`**, served at `kronosfusionenergy.com/3D_Model`.

## What's here
| File / folder | Purpose |
|---|---|
| `index.html` | Entry page (identical to `twin.html`; makes `/3D_Model/` serve the app directly) |
| `twin.html` | Assembly page — machine toggle + 3-D hero + embedded detail app |
| `twin_3d_reactor.html` | The Three.js 3-D reactor (loaded in an iframe) |
| `twin_rebuild_core_physics.html` | The detail app — all 43 pages, solver, toolkit, gating |
| `instructional_video.html` | The instructional film |
| `cad/` | STEP + hidden-line SVG projections (owner-only downloads in-app) |
| `solver/` | The live in-browser breeder evaluator (Pyodide fetches these) |
| `data/` | Design scan, UQ, validation JSON (fetched at runtime) |
| `assets/` | `og-3d-model.svg` — social share card |

## Before go-live (do these once)
1. **Export `assets/og-3d-model.png`** from `og-3d-model.svg` at 1200×630 — the OG meta tag points at the `.png`.
2. **Flip SEO to indexable**: in `twin.html` and `index.html`, change the `robots` meta from `noindex, nofollow` to `index, follow` (marked with a "SEO SWITCH" comment). Do the same in `twin_rebuild_core_physics.html` / `twin_3d_reactor.html` if you want those crawlable.
3. **Access tiers (Lovable auth)**: set body classes by sign-in state —
   - anonymous public → `member-locked public-locked`
   - signed-in reviewer → `public-locked`
   - owner () → *no classes*
   The in-app `◉ Preview` widget is for previewing these tiers; live gating comes from these body classes.

## Notes
- Must be served over **http/https** (the iframes + `fetch()` of solver/data don't work from `file://`).
- The 3-D reactor pulls Three.js from a CDN — needs internet; every other page works offline.
- Nothing is deployed/locked by this folder — that's your step.
