-- Phase 2 Computing — /lab gated dashboard · Supabase schema
-- Run this in your Supabase project (SQL editor). Powers the Run queue + Phase 3/4 board.
-- Team-of-3 model: access is gated by the Lovable login in front of /lab; these tables use
-- Supabase Auth so only signed-in team members can read/write. Tighten to an allow-list of
-- emails if you want per-person control (see the commented policy at the bottom).

-- ---- Run queue: hi-fi run requests (GENE / CGYRO / OpenMC / …) -------------------
create table if not exists public.lab_runs (
  id          uuid primary key default gen_random_uuid(),
  code        text not null,               -- GENE, CGYRO, OPENMC, …
  study       text not null,               -- target study / design point
  params      text,                        -- freeform: Ti=90keV, a/LTi=3, B=8T…
  priority    text default 'P2',           -- P1 | P2 | P3
  status      text default 'requested',    -- requested | running | done | parked
  requested_by text,
  created_at  timestamptz default now()
);

-- ---- Phase 3/4 workboard (kanban) -----------------------------------------------
create table if not exists public.lab_board (
  id          uuid primary key default gen_random_uuid(),
  task        text not null,
  owner       text,
  track       text,                        -- Hyperion / Aegis / MetroVolt / …
  phase       text,                        -- Phase 3 | Phase 4
  status      text default 'Backlog',      -- Backlog | Active | Blocked | Done
  notes       text,
  created_at  timestamptz default now()
);

-- ---- Row-level security: signed-in team only ------------------------------------
alter table public.lab_runs  enable row level security;
alter table public.lab_board enable row level security;

create policy "team read runs"   on public.lab_runs  for select to authenticated using (true);
create policy "team write runs"  on public.lab_runs  for insert to authenticated with check (true);
create policy "team update runs" on public.lab_runs  for update to authenticated using (true);

create policy "team read board"   on public.lab_board for select to authenticated using (true);
create policy "team write board"  on public.lab_board for insert to authenticated with check (true);
create policy "team update board" on public.lab_board for update to authenticated using (true);

-- Optional: restrict to an explicit allow-list of 3 team emails instead of any authenticated user.
-- create policy "allowlist" on public.lab_runs for all to authenticated
--   using (auth.jwt() ->> 'email' in ('a@kronos...','b@kronos...','c@kronos...'));
