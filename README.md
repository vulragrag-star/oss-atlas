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

- Universe seed: ~2100 high-star main repos (systems-leaning)
- Sector deep-dives: running in parallel
- Shortlist / synthesis: regenerating as scores land

## License

Docs/methodology: CC BY 4.0. Code: MIT. See [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff).
