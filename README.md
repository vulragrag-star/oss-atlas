# oss-atlas

**A living map of GitHub open-source contribution terrain — for humans and agents.**

`oss-atlas` treats contribution strategy as a **paper + code + data** artifact:

| Layer | What it is |
|---|---|
| **Paper** | Methodology, failure modes, cadence, and synthesis of where agents should (and should not) contribute |
| **Code** | Scripts to harvest repos, score AI/contribution policies, and refresh the map |
| **Data** | Universe samples, scored tables, sector digests, curated shortlist |

This is topography — policies, maintainer climate, automation/hostility signals, and bug classes that merge — not a “good first issue” dump.

## Quick start

```bash
python scripts/harvest_universe.py --out data/universe.jsonl
python scripts/score_repo.py owner/repo
python scripts/build_shortlist.py
```

Agents: read [`AGENTS.md`](AGENTS.md) before third-party forks/PRs.

## Status

- Universe seed: **16334** high-star main repos (systems-leaning + TS/JS/Zig fill)
- Scored rows: **1193** across eight sectors · proceed **786**
- Sector deep-dives synced: all eight (+ midband digests) in [`sectors/`](sectors/)
- Shortlist: [`SHORTLIST.md`](SHORTLIST.md) — **100** sector-balanced proceed targets (cli/devops/editors weighted)
- Synthesis: CLI/build primary; DevEx + SQL/storage + careful security secondary; hard leaves fish/sqlite/AgentScan/Zig — [`SYNTHESIS.md`](SYNTHESIS.md)


## License

Docs/methodology: CC BY 4.0. Code: MIT. See [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff).
