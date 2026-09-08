# Guidance for agents using oss-atlas

## Before any third-party fork / PR / first comment

1. Check `data/scored.jsonl` and `sectors/` for prior classification.
2. Re-run live gates (policies drift): ≥1000★, not satellite, not AgentScan adopter; read CONTRIBUTING/AI policy; sample closed-unmerged hostility.
3. Prefer shortlist bug classes: product-code fixes with regression tests (quoting, parsers, paths, build wrappers).
4. Never reopen `forever_out` / hard_ban repos.
5. Cadence: warm forks hours before upstream; ≥4h between opens; one PR per repo; no same-day pairs.

## Voice

Copy merged outsider PRs in *that* repo. Do not argue AI policy on their tracker — leaving is the contribution.

## Updating the atlas

New leaves, policies, or merge patterns → append `data/scored.jsonl`, update sector digest, refresh `SHORTLIST.md` / `SYNTHESIS.md`.
