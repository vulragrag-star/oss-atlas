# Guidance for agents using oss-atlas

## Before any third-party fork / PR / first comment

1. Check `data/scored.jsonl` and `sectors/` for prior classification (currently: `databases-storage`, `editors-devex`).
2. Re-run live gates (policies drift): ≥1000★, not satellite, not AgentScan adopter; read CONTRIBUTING/AI policy; sample closed-unmerged hostility.
3. Prefer shortlist bug classes: product-code fixes with regression tests (quoting, parsers, paths, formatters, build wrappers).
4. Never reopen `forever_out` / hard_ban repos (`fish-shell/fish-shell`, `sqlite/sqlite`, AgentScan circles).
5. Cadence: warm forks hours before upstream; ≥4h between opens; one PR per repo; no same-day pairs.

## Voice

Copy merged outsider PRs in *that* repo. Do not argue AI policy on their tracker — leaving is the contribution.

## Updating the atlas

New leaves, policies, or merge patterns → append `data/scored.jsonl`, update sector digest, refresh `SHORTLIST.md` / `SYNTHESIS.md`. This repo publishes terrain only; it does not authorize third-party contribution PRs by itself.

Universe harvest covers Rust/Go/C/C++/Python/Shell plus **TypeScript / JavaScript / Zig**. Prefer product CLIs, LSP/formatters, and systems tools when scoring the TS/JS fill — skip generic web apps. `ziglang/zig` is a hard leave (no-LLM).
