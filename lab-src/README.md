# Lab — source notes (public repo holds no gated content)

The **Lab** is the Kronos team workspace: the deep data browser (every study, every tier), unlocked
instruments (full UQ studio, burner live-solve, sensitivity sweeps, design-space explorer), the
high-fidelity **run queue** (GENE / CGYRO / OpenMC / SOLPS requests → HPC), the **Phase 3/4 workboard**,
and internal-only analyses including economics.

It is **hosted on the Kronos private workspace behind the existing team login** — never on this public
repository. This folder holds only what is safe and useful in the open:

- `supabase/schema.sql` — the run-queue + workboard tables with row-level security (authenticated team only).
- `release_gate.sh` — the firewall check run before every push of this repository.

What is deliberately *not* here: the gated dashboard HTML, the full research registry (it carries internal
paths and unpublished study titles), the economics/LCOE material, CAD/STEP models and detail blueprint
sheets, and the internal scanners that index the research tree. Those live with the private build.

Public entry point: [`/lab/index.html`](../lab/index.html).
