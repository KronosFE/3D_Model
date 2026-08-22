# Kronos Model — the machine, the physics, the program

**Live:** https://www.kronosfusionenergy.com/3D_Model

One place for everything Kronos has designed, computed, and published:

- **Machine** — the interactive 3D reactor (every component inspectable), hardware systems, materials & environment, the instructional film.
- **Physics** — the live instruments: the deposited D–T breeder engine, the D–³He tandem-mirror closure map, and Bosch–Hale reactivity — running in your browser via WebAssembly Python. The engine re-derives the frozen design points (Q 3.424 · 88.7 MW · 9.86 MA) before any control unlocks. Validation, V&V and UQ with the live 19/19 anchor regression.
- **Program** — the open record: every fully reproducible study (pre-registered, citation-audited, with data), the roadmap and its stated gates, readiness & risks, computing, and how to cite.
- **Lab** — the team workspace (deep data, unlocked instruments, hi-fi run queue, Phase 3/4 board). Sign-in required; hosted on the Kronos private workspace, not in this repository.

## The engine, open source
`engine/kronos_toolkit/` is the Kronos Research Toolkit — one versioned, anchor-tested Python engine behind every published number (Apache-2.0, see `engine/LICENSE`). `assets/engine/` is the numpy-only browser kernel the pages run; both reproduce the same frozen anchors, which `engine/kronos_toolkit/verify/` enforces.

## Honest gates
Conceptual design and simulation study — no machine has been built. The breeder is a strategic-materials platform, not a power plant. The burner is plug-gated, not net-power today. No economics appears in this repository.

## Open record
Breeder deposit DOI 10.5281/zenodo.21746157 · burner deposit DOI 10.5281/zenodo.21746479 · CC BY 4.0.
Site content © 2026 Kronos Fusion Energy, Inc. (see `LICENSE`); engine code Apache-2.0.
