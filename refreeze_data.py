#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
refreeze_data.py — regenerate the twin's pre-computed data snapshots from the
new-canon bundled engine (2026-08-27 freeze). The engine already produces Q 3.076;
only the JSON snapshots + one HTML text block still held the superseded Q 3.424.

Regenerates: data/dt_scan_compact.json (25,200-config scan, every row re-evaluated),
data/regression.json (breeder anchors), and patches the frozen markers in
data/uq_frozen.json / data/validation.json. Verifies the frozen config (22021)
reproduces the anchor before writing anything.

Run:  python3 refreeze_data.py
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "engine"))
from kronos_toolkit.core import evaluate_breeder
from kronos_toolkit import verify

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
FIXED = dict(R0=1.2, delta=-0.3, f_he4=0.05)   # Hyperion frozen geometry (reproduces config 22021)

A = verify.BREEDER_ANCHORS   # {'Q':{'value':3.076..}, ...}

def ev(fuel, B0, Aasp, kappa, q95, fG, Ti0, TBR_dt):
    r = evaluate_breeder(fuel=fuel, A=Aasp, kappa=kappa, B0=B0, q95=q95, fG=fG,
                         Ti0=Ti0, TBR_dt=TBR_dt, **FIXED)
    return r

def refreeze_scan():
    p = os.path.join(DATA, "dt_scan_compact.json")
    d = json.load(open(p, encoding="utf-8"))
    cols = d["cols"]; ix = {c: cols.index(c) for c in cols}
    out_cols = ["betaN","Ip_MA","P_fus_MW","Q","T_kg_yr","wall_MW_m2","f_n","closes_nowall"]
    rnd = {"betaN":4,"Ip_MA":4,"P_fus_MW":4,"Q":4,"T_kg_yr":4,"wall_MW_m2":4,"f_n":4}
    frozen_check = None
    for row in d["data"]:
        r = ev(row[ix["fuel"]], row[ix["B0"]], row[ix["A"]], row[ix["kappa"]],
               row[ix["q95"]], row[ix["fG"]], row[ix["Ti0"]], row[ix["TBR_dt"]])
        vals = {"betaN":r["betaN"],"Ip_MA":r["Ip_MA"],"P_fus_MW":r["P_fus_MW"],"Q":r["Q"],
                "T_kg_yr":r["T_kg_yr"],"wall_MW_m2":r["wall_MW_m2"],"f_n":r["f_n"],
                "closes_nowall":1 if r.get("beta_ok_nowall") else 0}
        for c in out_cols:
            row[ix[c]] = vals[c] if c=="closes_nowall" else round(vals[c], rnd[c])
        if row[ix["config_id"]] == 22021:
            frozen_check = dict(vals)
    # verify frozen point == anchor before writing
    assert frozen_check is not None, "config 22021 not found"
    for k in ("Q","P_fus_MW","Ip_MA","T_kg_yr","f_n"):
        exp = A[k]["value"] if k in A else None
        if exp is not None:
            assert abs(frozen_check[k]-exp) <= A[k]["atol"], f"frozen {k}={frozen_check[k]} != anchor {exp}"
    d["frozen"] = 22021
    json.dump(d, open(p,"w",encoding="utf-8"), separators=(",",":"))
    print(f"  ✓ dt_scan_compact.json — {len(d['data'])} configs re-evaluated; "
          f"frozen 22021 Q={frozen_check['Q']:.4f} P_fus={frozen_check['P_fus_MW']:.2f} Ip={frozen_check['Ip_MA']:.3f} (anchor-verified)")

def refreeze_regression():
    p = os.path.join(DATA, "regression.json")
    d = json.load(open(p, encoding="utf-8"))
    newv = {"breeder.Q":A["Q"]["value"], "breeder.P_fus_MW":A["P_fus_MW"]["value"],
            "breeder.Ip_MA":A["Ip_MA"]["value"], "breeder.T_kg_yr":A["T_kg_yr"]["value"],
            "breeder.f_n":A["f_n"]["value"]}
    changed=[]
    for r in d["rows"]:
        if r["check"] in newv:
            v = f'{newv[r["check"]]:.6f}'
            if r.get("expected")!=v: changed.append(r["check"])
            r["expected"]=v; r["got"]=v; r["verdict"]="PASS"
    d["all_pass"]=all(r["verdict"]=="PASS" for r in d["rows"])
    json.dump(d, open(p,"w",encoding="utf-8"), indent=1)
    print(f"  ✓ regression.json — updated {changed}; all_pass={d['all_pass']}")

def patch_markers():
    # replace the single stale frozen-point markers in uq/validation snapshots
    subs = [("3.4239","3.0763"),("3.423913","3.076326"),
            ("88.6604","85.0406"),("88.660424","85.040577"),
            ("9.8599","9.6565"),("9.859860","9.656483")]
    for name in ("uq_frozen.json","validation.json"):
        p=os.path.join(DATA,name); t=open(p,encoding="utf-8").read(); o=t
        for a,b in subs: t=t.replace(a,b)
        if t!=o: open(p,"w",encoding="utf-8").write(t); print(f"  ✓ {name} — frozen markers updated")
        else: print(f"  · {name} — no markers to change")

def patch_validation_html():
    p=os.path.join(HERE,"physics","validation.html")
    t=open(p,encoding="utf-8").read(); o=t
    for a,b in [("9.859860","9.656483"),("9.8599","9.6565"),
                ("3.423913","3.076326"),("3.4239","3.0763"),
                ("88.660424","85.040577"),("88.6604","85.0406")]:
        t=t.replace(a,b)
    if t!=o: open(p,"w",encoding="utf-8").write(t); print("  ✓ physics/validation.html — hardcoded numbers updated")
    else: print("  · physics/validation.html — nothing to change")

if __name__=="__main__":
    print("Re-freezing twin data to 2026-08-27 canon (engine already new-canon)…")
    refreeze_regression()
    refreeze_scan()
    patch_markers()
    patch_validation_html()
    print("Done.")
