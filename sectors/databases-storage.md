# Sector survey: databases-storage

Account: `vulragrag-star` · Input: `survey/raw/databases-storage.jsonl` (64 repos) · Sampled **35** product-ish repos deep (policy files via `gh api`) + **10** noise/wrong-class leaves scored · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **parser / path / SQL edge bugs with regression tests** (not docs farm, not GFI spam, not satellite).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 37 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 5 | ASF generative-tooling and/or explicit AI-assisted rules (opendal, rook, litestream, datafusion, superset) |
| hostility_risk | 2 | Weaviate auto-close AI/bulk; SQLCipher inherits SQLite culture |
| hard_ban | 1 | `sqlite/sqlite` AGENTS.md agentic ban |
| **agentscan** | 0 | No sample repo/owner on local adopters/blacklist |

Proceed: **24** · Leave: **21** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `apache/superset` | 74677 | disclosure | ASF + AGENTS.md; SQL lab / viz — prefer SQL parsing edges over UI farm | SQL parse/Jinja/template edge with tests |
| `prometheus/prometheus` | 66005 | silent | AGENTS.md aligns agents to review norms; PromQL/textparse/tsdb path edges | PromQL/textparse quoting or tsdb path + table tests |
| `tursodatabase/libsql` | 17208 | silent | SQLite fork that accepts PRs; SQL parser extensions (ANALYZE etc.) | SQL parser / savepoint edge + tests |
| `tikv/tikv` | 16836 | silent | Distributed KV; date/TSO/format edges exist but high bar / OWNERS heavy | format/parse or path edge in compact-log-backup + tests |
| `apple/foundationdb` | 16677 | silent | AGENTS.md for agents; simulation-test culture; C++ hard — small testable tool bugs only | simulation knob/path edge + tests |
| `dgraph-io/badger` | 15758 | silent | LSM KV; SST open/compaction error paths with tests | SST path/corruption / compaction edge + tests |
| `go-sql-driver/mysql` | 15282 | silent | No AI ban; DSN/param/bool parsing; maintainer-heavy but outsider tests welcome | DSN/param/quoting/TINYINT edge + dsn_test |
| `benbjohnson/litestream` | 14358 | disclosure | Welcomes AI-assisted bugfixes with investigation+go test cmds; path/config edges | path/config DSN/replica path + go test |
| `rook/rook` | 13645 | disclosure | CNCF AI guidelines: disclose AI, no autonomous bots, max 3 open PRs; path/storage orchestration | path/ceph volume mount + unit tests |
| `drakkan/sftpgo` | 12498 | silent | SFTP/HTTP storage; path traversal/normalize class; recent surface mostly dependabot | path sanitize / virtual folder edge + tests |
| `manticoresoftware/manticoresearch` | 11993 | silent | Full-text/vector search SQL; parser edges plausible | SQL/fulltext parse edge + tests |
| `PRQL/prql` | 10910 | silent | No hard AI ban; dialect SQL compile; recent quote-escape parser fixes with tests | SQL dialect quoting/escape parser + snapshot tests |
| `etcd-io/bbolt` | 9727 | silent | Embedded KV; tx/bucket path edges; CNCF; recent PRs mostly Go bumps | bucket/key path or freelist edge + tests |
| `apache/datafusion` | 9292 | disclosure | ASF generative-tooling + AGENTS.md; SQL planner/parser with strong test culture | SQL parser/planner edge + table-driven tests |
| `mattn/go-sqlite3` | 9236 | silent | database/sql driver; schema/cache/vtab edges; mostly mattn but testable driver bugs | stmt cache/schema/vtab edge + tests |
| `dinedal/textql` | 9103 | silent | CSV→SQL; label:path and sqlparser edges; low velocity but exact class | sqlparser / path:label table name + tests |
| `codenotary/immudb` | 9029 | silent | Immutable SQL/KV; statement-failure tx edge recently fixed | SQL statement/tx edge + tests |
| `XiaoMi/soar` | 8755 | silent | SQL optimizer/rewriter; rule edge cases; Chinese maintainer base | SQL rewrite rule / time-parse / DSN edge + tests |
| `mongodb/mongo-go-driver` | 8540 | silent | AGENTS.md; BSON/URI parse edges; bugs via JIRA GODRIVER not GitHub Issues | URI/BSON parse edge + task test |
| `asg017/sqlite-vec` | 8087 | silent | Not sqlite.org; vec0 virtual table SQL edges; active maintainer | SQL virtual-table / rename edge + tests |
| `Masterminds/squirrel` | 7987 | silent | Fluent SQL builder; known placeholder/JoinClause edge bugs with tests | SQL placeholder/JoinClause subquery + unit tests |
| `authzed/spicedb` | 7030 | silent | Zanzibar permission DSL/parser; typed annotation edges | schema/DSL parse edge + consistency tests |
| `FalkorDB/FalkorDB` | 5946 | silent | Graph DB; Cypher-ish query/index edges | query/index parse edge + tests |
| `apache/opendal` | 5371 | disclosure | Explicit AI-Assisted Contributions; human accountable; storage path/quoting layer | path/normalize/quoting across storage backends + tests |

### Tier notes

**Best first homes (small testable SQL/path hunks):**

1. `PRQL/prql` — dialect SQL compile; recent merged work is literally escaped-quote parser fixes with grammar tests.
2. `Masterminds/squirrel` / `dinedal/textql` / `go-sql-driver/mysql` — placeholder, DSN, `label:path` edges; classic playbook shape.
3. `benbjohnson/litestream` — explicit AI-assisted bugfix welcome if investigation + runnable `go test`; path/config duplicates already a live theme.
4. `apache/opendal` — storage path normalize across backends; must follow AI-Assisted section (human explains, no raw LLM paste in review).
5. `apache/datafusion` — SQL planner/parser; ASF accountability; heavy CI but excellent test culture.
6. `prometheus/prometheus` — PromQL/`textparse` quoting; AGENTS.md documents title/test conventions (not a ban).
7. `AlistGo/alist` — high velocity outsider path-normalize fixes across storage drivers.

**Proceed with process friction:** `rook/rook` (disclose AI, ≤3 open PRs, issue-first for large changes); `mongodb/mongo-go-driver` (bugs via JIRA GODRIVER); `tikv/tikv` / `apple/foundationdb` (high bar, still silent policy).

**SQLite-adjacent but not sqlite.org:** `tursodatabase/libsql`, `mattn/go-sqlite3`, `asg017/sqlite-vec`, `rqlite` (leave rqlite as home — maintainer-monopoly merges). Do **not** treat these as permission to touch `sqlite/sqlite`.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `sqlite/sqlite` | 10438 | hard_ban | AGENTS.md: does not accept agentic code; PRs need prior agreement |
| `macrozheng/mall` | 84727 | silent | Ecommerce app using DBs — not DB/storage product |
| `Developer-Y/cs-video-courses` | 83441 | silent | Awesome-list / curriculum dump — not product code |
| `zylon-ai/private-gpt` | 57495 | silent | RAG app — docs/feature farm risk; not parser/SQL product core |
| `run-llama/llama_index` | 52068 | silent | RAG framework — not storage engine; docs/example farm risk |
| `rqlite/rqlite` | 17725 | silent | Healthy product but nearly all merges by otoolep — outsider merge rate unknown/low |
| `weaviate/weaviate` | 16793 | hostility_risk | Closes unlinked/cosmetic/bulk-automated/AI-generated PRs without review; CLA |
| `haiwen/seafile` | 15222 | silent | No CONTRIBUTING in common paths; C sync client — weak survey signal |
| `cayleygraph/cayley` | 15062 | silent | No CONTRIBUTING; graph DB may be low-maintenance |
| `vesoft-inc/nebula` | 12379 | silent | Contrib docs point to nebula-community; heavy distributed graph |
| `fogleman/Craft` | 11092 | silent | Minecraft clone — wrong sector noise |
| `pingcap/talent-plan` | 10995 | silent | Training courses — not product |
| `yugabyte/yugabyte-db` | 10518 | silent | Huge Postgres fork; AGENTS.md tips only; not small hunk friendly |
| `cstack/db_tutorial` | 10514 | silent | Tutorial — not product |
| `bxcodec/go-clean-arch` | 10158 | silent | Sample architecture — not product |
| `spacejam/sled` | 9085 | silent | Alpha refactor by author; discuss-first CONTRIBUTING; poor outsider fit now |
| `sqlcipher/sqlcipher` | 7265 | hostility_risk | SQLite fork; upstream bans agentic patches — leave unless cleared |
| `perkeep/perkeep` | 7239 | silent | bradfitz-centric; blob/hash path — slow outsider queue |
| `xiaobaiTech/golangFamily` | 6964 | silent | Interview dump — not product |
| `alibaba/AliSQL` | 5948 | silent | Alibaba MySQL branch; unclear modern outsider process / likely stale relative to upstream |
| `cmu-db/bustub` | 5086 | silent | Educational course scaffolding — not product contribution target |

## Sector synthesis

- **Hard exclude in-sector:** only `sqlite/sqlite` is a published agentic-code ban. SQLCipher is guilt-by-fork; Weaviate is a bulk/AI closer.
- **Disclosure cluster is usable:** OpenDAL/Litestream/Rook explicitly welcome *human-owned* AI-assisted bugfixes; copy their templates (opendal AI section, litestream `AI_PR_GUIDE.md`, rook AI guidelines) — do not invent trailers.
- **Fit theme:** SQL parsers/builders (PRQL, DataFusion, squirrel, textql, soar, go-mysql DSN), storage path normalize (OpenDAL, Alist, SFTPGo, Litestream replica paths), PromQL/textparse.
- **Avoid:** awesome-lists/tutorials in the raw dump; RAG apps (`private-gpt`, `llama_index`); course scaffolds (`bustub`, `talent-plan`); maintainer-only homes (`rqlite`/`otoolep`, `perkeep`/`bradfitz`, `sled` alpha).
- **AgentScan:** none of the deep sample hit local adopters/skip_orgs (2026-09-02 dump). Re-run `agentscan-check.py --refresh` before any future fork.

## Method notes

- Policy files probed: CONTRIBUTING*, AI.md, AI_POLICY.md, AGENTS.md, CoC, PR templates, docs/CONTRIBUTING*, `.github/workflows` names.
- Local AgentScan check only (no network refresh during survey).
- Merged-PR titles sampled read-only via `gh pr list` for fit; no tracker comments.

