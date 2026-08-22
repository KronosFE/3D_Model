#!/usr/bin/env bash
# Firewall release gate for KronosFE/3D_Model — run before every push.
# HARD patterns fail the build; SOFT patterns are listed for human review.
# engine/tests/ is excluded from HARD: it holds dummy fixtures that deliberately exercise the no-economics guard.
set -u
cd "$(dirname "$0")/.."
HARD='\$[0-9]|p\.ford@|pford@|\.step"|DO NOT PUBLISH|PHASE3_FINANCIALS|/Users/pford'
SOFT='LCOE|capex|valuation|Funding Strategy|CONFIDENTIAL'
SCOPE=$(git ls-files | grep -E '\.(html|md|js|css|json|py|txt)$' | grep -vE '^lab-src/release_gate.sh$|^engine/tests/')
hard=$(echo "$SCOPE" | xargs grep -nE "$HARD" 2>/dev/null)
soft=$(echo "$SCOPE" | xargs grep -nE "$SOFT" 2>/dev/null)
echo "== release gate =="
if [ -n "$hard" ]; then echo "HARD FAIL:"; echo "$hard" | cut -c1-160; exit 1; fi
echo "hard patterns: clean"
if [ -n "$soft" ]; then echo "soft patterns (review):"; echo "$soft" | cut -c1-160; else echo "soft patterns: clean"; fi
echo "gate: PASS"
