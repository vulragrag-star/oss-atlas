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

## Product deepen-2 (≥5k★ subset) (2026-09-10, +15 scored)

Account: `vulragrag-star` · Curated product DB/storage homes still missing after prior databases-storage passes · Policy via `raw.githubusercontent.com` · **12** proceed / **3** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 14, 'disclosure': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `alibaba/zvec` | 15847 | silent | In-process vector database; index/path edges | vector index/path edge + C++ tests |
| `happyfish100/fastdfs` | 9252 | silent | Distributed file system; path/storage edges | storage path/tracker edge + C tests |
| `WiseLibs/better-sqlite3` | 7475 | silent | Node SQLite3 binding; stmt/API/path edges | stmt/bind/path edge + JS tests |
| `amacneil/dbmate` | 7347 | silent | Framework-agnostic DB migration CLI; path/URL edges | migration path/URL/dialect edge + Go tests |
| `aarondl/sqlboiler` | 6990 | silent | Schema-driven Go ORM codegen; SQL/dialect edges | schema/SQL dialect edge + Go tests |
| `postgresml/postgresml` | 6820 | silent | Postgres+GPU ML extension stack; SQL/path edges | SQL/extension/path edge + Rust tests |
| `GreptimeTeam/greptimedb` | 6648 | disclosure | Observability columnar DB; SQL/PromQL/path edges | SQL/PromQL/path edge + Rust tests |
| `RediSearch/RediSearch` | 6234 | silent | Redis full-text/vector query module; query/index edges | query/index/path edge + Rust/C tests |
| `OpenAtomFoundation/pikiwidb` | 6127 | silent | Redis-compatible DB; cmd/RESP/path edges | RESP/cmd/path edge + C++ tests |
| `HelixDB/helix-db` | 5890 | silent | OLTP graph DB with vector/FTS; query/path edges | graph query/path edge + Rust tests |
| `Meituan-Dianping/SQLAdvisor` | 5616 | silent | SQL index advisor CLI; SQL parse edges | SQL parse/index-hint edge + C tests |
| `cube2222/octosql` | 5265 | silent | Multi-source SQL query CLI; dialect/path edges | SQL dialect/path edge + Go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `dbgate/dbgate` | 7297 | silent | Heavy multi-DB GUI manager — weak small hunk/outsider fit |
| `erikgrinaker/toydb` | 7277 | silent | Educational distributed SQL toy — not a production contrib home |
| `dataease/SQLBot` | 6758 | silent | LLM Text-to-SQL RAG app — wrong class / agent-product adjacency |

Notes: Prefer engines/modules/CLIs (GreptimeDB, RediSearch, PikiwiDB, HelixDB, dbmate, better-sqlite3, SQLBoiler, OctoSQL). Disclosure homes (greptimedb, cloudberry, osm2pgsql) need human-owned PR bodies. Leave GUI managers, Text-to-SQL apps, tutorials, client-only drivers, Docker packaging, and agent MCP/BaaS surfaces.

## Product deepen (≥5k★ subset) (2026-09-11, +118 scored)

Account: `vulragrag-star` · Curated database/storage/search/TSDB/migration product homes still missing after midband + famous-CLI passes · Policy via `raw.githubusercontent.com` · **78** proceed / **40** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 94, 'disclosure': 20, 'hard_ban': 1, 'hostility_risk': 2, 'agentscan': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `redis/redis` | 76292 | silent | Redis server; command/RESP/path edges with tests | RESP/cmd/config path edge + C tests |
| `meilisearch/meilisearch` | 59217 | disclosure | Search engine; query/index/path — disclose AI | query/index/path edge + Rust tests |
| `ClickHouse/ClickHouse` | 49730 | disclosure | OLAP DB; SQL/format/path — AI_POLICY disclosure | SQL/format/path edge + C++ tests |
| `prisma/orm` | 47610 | disclosure | TS ORM; schema/migrate/client edges — disclose | schema/migrate/query edge + TS tests |
| `milvus-io/milvus` | 46036 | disclosure | Vector DB; search/index/path — disclose | vector search/index path edge + Go tests |
| `duckdb/duckdb` | 41108 | disclosure | Embedded OLAP; SQL/CSV/parquet — AI_POLICY HITL | SQL/CSV/parquet path edge + C++ tests |
| `pingcap/tidb` | 40505 | silent | Distributed SQL; parser/planner/path edges | SQL parser/planner path edge + Go tests |
| `go-gorm/gorm` | 39950 | silent | Go ORM; query builder/schema edges | query/schema/dialect edge + Go tests |
| `google/leveldb` | 39395 | silent | Embedded KV; open/path/compaction edges | KV open/path edge + C++ tests |
| `typeorm/typeorm` | 36649 | silent | TS ORM; entity/migration/path edges | entity/migration/path edge + TS tests |
| `restic/restic` | 35954 | silent | Backup CLI; path/repo/format edges | backup path/repo format edge + Go tests |
| `drizzle-team/drizzle-orm` | 35715 | silent | TS SQL ORM; schema/query edges | schema/SQL query edge + TS tests |
| `seaweedfs/seaweedfs` | 34557 | silent | Distributed object/file storage; path/volume edges | volume/path/API edge + Go tests |
| `qdrant/qdrant` | 34462 | disclosure | Vector search engine; filter/index — disclose | filter/index/path edge + Rust tests |
| `surrealdb/surrealdb` | 32997 | silent | Multi-model DB; SurrealQL/path edges | SurrealQL/path edge + Rust tests |
| `facebook/rocksdb` | 32075 | silent | Embedded KV/storage engine; option/path edges | option/path/compaction edge + C++ tests |
| `influxdata/influxdb` | 31729 | silent | Time-series DB; InfluxQL/line protocol edges | line protocol/query path edge + Rust tests |
| `dragonflydb/dragonfly` | 31467 | silent | Dragonfly Redis-compatible; cmd/RESP/path edges | RESP/cmd/path edge + C++ tests |
| `sequelize/sequelize` | 30366 | silent | Node ORM; dialect/query edges | dialect/query/model edge + JS tests |
| `chroma-core/chroma` | 29263 | silent | Vector DB for embeddings; collection/path edges | collection/query path edge + Python tests |
| `grafana/loki` | 28857 | silent | Log aggregation TS store; LogQL/path edges | LogQL/path/label edge + Go tests |
| `valkey-io/valkey` | 27160 | silent | Valkey Redis-compatible server; RESP/cmd edges | RESP/cmd/path edge + C tests |
| `typesense/typesense` | 26542 | silent | Search engine; collection/query/path edges | collection/query path edge + C++ tests |
| `taosdata/TDengine` | 25103 | silent | Time-series DB; SQL/path edges | TS SQL/path edge + C tests |
| `tursodatabase/turso` | 24221 | disclosure | SQLite-compatible Rust DB — disclose AI | SQL/compat/path edge + Rust tests |
| `timescale/timescaledb` | 23499 | disclosure | Postgres TS extension; SQL/hypertable — human ownership | SQL hypertable/path edge + C tests |
| `neondatabase/neon` | 23062 | silent | Serverless Postgres storage/compute split; path/pageserver edges | pageserver/path/WAL edge + Rust tests |
| `dgraph-io/dgraph` | 21788 | silent | Graph DB; DQL/query/path edges | DQL/query/path edge + Go tests |
| `valeriansaliou/sonic` | 21337 | silent | Schema-less search backend; ingest/query edges | ingest/query/path edge + Rust tests |
| `vitessio/vitess` | 21303 | silent | MySQL clustering; VTGate SQL/path edges | VTGate SQL/path edge + Go tests |
| `knex/knex` | 20343 | silent | SQL query builder; dialect/migration edges | dialect/migration/path edge + JS tests |
| `golang-migrate/migrate` | 18904 | silent | DB migration CLI; source/URL/path edges | migration source/URL path edge + Go tests |
| `sqlc-dev/sqlc` | 18260 | silent | SQL→type-safe codegen CLI; parse/path edges | SQL parse/codegen path edge + Go tests |
| `jmoiron/sqlx` | 17733 | silent | Go database/sql extensions; named query edges | named query/scan edge + Go tests |
| `VictoriaMetrics/VictoriaMetrics` | 17679 | silent | Metrics TSDB; PromQL/remote-write edges | PromQL/remote-write path edge + Go tests |
| `transact-rs/sqlx` | 17461 | silent | Rust async SQL toolkit; query/migrate edges | query/migrate/path edge + Rust tests |
| `questdb/questdb` | 17315 | silent | Time-series SQL DB; ILP/SQL edges | ILP/SQL/path edge + Java tests |
| `ent/ent` | 17196 | silent | Go entity framework; schema/codegen edges | schema/codegen/path edge + Go tests |
| `apache/arrow` | 17092 | disclosure | Columnar format; IPC/parquet — disclose AI | IPC/parquet/path edge + C++ tests |
| `tigerbeetle/tigerbeetle` | 16971 | silent | Financial tx DB; journal/path edges | journal/path/replica edge + Zig tests |
| `prestodb/presto` | 16733 | silent | Distributed SQL engine; connector/SQL edges | SQL/connector/path edge + Java tests |
| `quickwit-oss/tantivy` | 16050 | silent | Full-text search library; index/query edges | index/query/path edge + Rust tests |
| `electric-sql/pglite` | 16000 | silent | Embeddable Postgres WASM; SQL/path edges | SQL/WASM/path edge + TS tests |
| `apache/doris` | 15889 | silent | MPP OLAP DB; SQL/path edges | SQL/path/FE edge + Java tests |
| `scylladb/scylladb` | 15740 | silent | Cassandra-compatible NoSQL; CQL/path edges | CQL/path/compaction edge + C++ tests |
| `juicedata/juicefs` | 14418 | silent | POSIX-on-object-storage FS; path/meta edges | meta/path/object edge + Go tests |
| `arangodb/arangodb` | 14269 | silent | Multi-model DB; AQL/path edges | AQL/path edge + C++ tests |
| `thanos-io/thanos` | 14200 | silent | Prometheus long-term storage; store/query edges | store/query/path edge + Go tests |
| `diesel-rs/diesel` | 14173 | disclosure | Rust ORM; query/schema — disclose AI | query/schema/migration edge + Rust tests |
| `kopia/kopia` | 14067 | silent | Backup CLI; repo/path/format edges | backup repo/path format edge + Go tests |
| `apache/druid` | 14050 | silent | Realtime analytics DB; ingest/query edges | ingest/query/path edge + Java tests |
| `borgbackup/borg` | 13706 | disclosure | Dedup backup CLI — AI policy disclosure | archive/path/format edge + Python tests |
| `opensearch-project/OpenSearch` | 13701 | silent | Search/analytics fork; query/index edges | query/index/path edge + Java tests |
| `github/gh-ost` | 13559 | silent | Online MySQL schema migration CLI; binlog/path edges | binlog/DDL/path edge + Go tests |
| `trinodb/trino` | 13223 | silent | Distributed SQL; connector/SQL edges | SQL/connector/path edge + Java tests |
| `citusdata/citus` | 12753 | silent | Postgres distributed extension; SQL/shard edges | SQL/shard/path edge + C tests |
| `StarRocks/starrocks` | 12098 | silent | MPP OLAP; SQL/path edges | SQL/path/FE edge + Java tests |
| `quickwit-oss/quickwit` | 11577 | disclosure | Log search engine — AI_POLICY present | index/query/path edge + Rust tests |
| `pressly/goose` | 11429 | silent | Go migration CLI; SQL/path edges | migration SQL/path edge + Go tests |
| `apache/cassandra` | 10087 | disclosure | Wide-column DB — disclose AI | CQL/path/compaction edge + Java tests |
| `flyway/flyway` | 10083 | silent | Migration CLI/tool; SQL/path edges | migration SQL/path edge + Java tests |
| `databendlabs/databend` | 9441 | disclosure | Cloud warehouse; SQL/path — AI welcome w/ disclosure | SQL/storage/path edge + Rust tests |
| `risingwavelabs/risingwave` | 9305 | silent | Streaming SQL DB; SQL/path edges | streaming SQL/path edge + Rust tests |
| `apache/iceberg` | 9222 | disclosure | Table format; snapshot/path — disclose | snapshot/manifest/path edge + Java tests |
| `delta-io/delta` | 8991 | silent | Lakehouse table format; protocol/path edges | delta protocol/path edge + Scala tests |
| `ariga/atlas` | 8709 | silent | Schema-as-code CLI; HCL/SQL/path edges | schema HCL/SQL path edge + Go tests |
| `vespa-engine/vespa` | 7080 | silent | Big data serving engine; query/rank edges | query/rank/path edge + Java tests |
| `MaterializeInc/materialize` | 6368 | silent | Streaming SQL DB; SQL/path edges | streaming SQL/path edge + Rust tests |
| `apache/hudi` | 6236 | silent | Lakehouse table format; commit/path edges | commit/timeline/path edge + Java tests |
| `apache/pinot` | 6134 | silent | Realtime OLAP; query/segment edges | query/segment/path edge + Java tests |
| `cockroachdb/pebble` | 6019 | silent | RocksDB-inspired KV; option/path edges | KV option/path edge + Go tests |
| `cubefs/cubefs` | 5655 | silent | Cloud-native distributed storage; meta/path edges | meta/data path edge + Go tests |
| `liquibase/liquibase` | 5609 | silent | DB migration tool; changelog/path edges | changelog/SQL path edge + Java tests |
| `apache/hbase` | 5558 | silent | Wide-column store; region/path edges | region/path/API edge + Java tests |
| `treeverse/lakeFS` | 5521 | silent | Git-like data lake control; path/ref edges | ref/path/object edge + Go tests |
| `grafana/tempo` | 5471 | disclosure | Distributed tracing backend — disclose AI | trace query/path edge + Go tests |
| `grafana/mimir` | 5231 | silent | Prometheus long-term metrics; PromQL/path edges | PromQL/store path edge + Go tests |
| `apache/calcite` | 5182 | silent | SQL parser/planner framework; SQL dialect edges | SQL parse/plan edge + Java tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `elastic/elasticsearch` | 77902 | silent | Search mega process — prefer OpenSearch/meilisearch/typesense-sized homes |
| `pandas-dev/pandas` | 49696 | silent | Pandas dataframe mega — prefer DuckDB/Arrow/Polars-adjacent; polars is agent-forbidden |
| `apache/spark` | 43978 | silent | Spark process mega — not small parser/SQL hunk farm |
| `pola-rs/polars` | 39697 | hostility_risk | AI_POLICY: agents strictly forbidden from interacting; leave agent workflow |
| `numpy/numpy` | 32706 | disclosure | Foundational scientific mega with AI disclosure — park vs DuckDB/Arrow product homes |
| `cockroachdb/cockroach` | 32448 | silent | Cockroach distributed SQL mega — high bar |
| `mongodb/mongo` | 28544 | silent | MongoDB server mega — process-heavy; prefer modules/drivers already scored |
| `facebook/zstd` | 27807 | silent | Compression codec — not DB/storage product hunk class |
| `PostgREST/postgrest` | 27655 | hard_ban | Gentoo AI policy via CONTRIBUTING — hard leave |
| `Automattic/mongoose` | 27472 | silent | Mongo ODM — prefer engine/module homes over ODM wrappers for first PRs |
| `rethinkdb/rethinkdb` | 26994 | silent | RethinkDB low-maintenance realtime DB — verify activity; park |
| `apache/flink` | 26333 | disclosure | Flink process mega despite disclosure AGENTS — leave megas |
| `redis/go-redis` | 22230 | silent | Redis Go client-only driver — leave client-only class per atlas guidance |
| `postgres/postgres` | 22056 | silent | Postgres core mega — not small hunk-friendly first home |
| `apache/pouchdb` | 17604 | silent | Browser pocket DB — weak systems hunk class for playbook |
| `neo4j/neo4j` | 17220 | silent | Neo4j graph mega — prefer smaller graph homes already scored |
| `ceph/ceph` | 17011 | silent | Ceph distributed storage mega — leave for smaller object stores |
| `apache/hadoop` | 15654 | disclosure | Hadoop process mega — leave |
| `redis/ioredis` | 15335 | silent | Node Redis client-only — leave client-only drivers |
| `jackc/pgx` | 14227 | silent | Postgres pgx driver — leave client-only drivers |
| `dask/dask` | 13913 | silent | Dask parallel mega — leave |
| `redis/redis-py` | 13635 | silent | Python Redis client-only — leave client-only drivers |
| `Snapchat/KeyDB` | 12506 | silent | KeyDB Redis fork under Snapchat — verify contribution path; park vs valkey/dragonfly |
| `redis/jedis` | 12361 | silent | Java Redis client-only — leave client-only drivers |
| `lz4/lz4` | 12051 | silent | Compression codec — not DB/storage product hunk class |
| `modin-project/modin` | 10392 | silent | Pandas-on-Ray skin — leave |
| `oceanbase/oceanbase` | 10263 | silent | OceanBase distributed mega — leave |
| `mongodb/node-mongodb-native` | 10179 | silent | MongoDB Node driver — leave client-only drivers |
| `lib/pq` | 9957 | silent | Postgres lib/pq client-only — leave client-only drivers |
| `sqlfluff/sqlfluff` | 9866 | agentscan | AgentScan adopter — leave |
| `openebs/openebs` | 9810 | silent | K8s storage platform umbrella — weak SQL/parser hunk class |
| `tobymao/sqlglot` | 9603 | hostility_risk | LLM-assisted contribs discouraged; low-effort mostly-LLM PRs closed |
| `apache/beam` | 8658 | silent | Beam process mega — leave |
| `MariaDB/server` | 8189 | silent | MariaDB server mega — leave |
| `longhorn/longhorn` | 7968 | silent | K8s distributed block storage — ops platform, not DB engine |
| `google/snappy` | 6606 | silent | Compression codec — not DB/storage product hunk class |
| `elastic/go-elasticsearch` | 6067 | silent | Elasticsearch Go client-only — leave client-only drivers |
| `apache/hive` | 6020 | silent | Hive mega — leave |
| `cortexproject/cortex` | 5861 | disclosure | Cortex largely superseded by Mimir lineage — prefer mimir/loki/thanos |
| `redis/lettuce` | 5780 | silent | Java Redis client-only — leave client-only drivers |

Notes: Prefer engines/modules/SQL CLIs/ORMs/query builders/search/TSDB/vector/object-storage/backup (redis/valkey/dragonfly, ClickHouse/duckdb/tidb/vitess, meilisearch/typesense/qdrant/milvus, loki/mimir/tempo/thanos/VictoriaMetrics, restic/borg/kopia/gh-ost, goose/flyway/atlas/sqlc, rocksdb/leveldb/pebble/juicefs/seaweedfs, arrow/iceberg/delta/hudi). Disclosure: meilisearch/ClickHouse/duckdb/qdrant/turso/timescale/arrow/cassandra/iceberg/quickwit/diesel/borg/databend/prisma/milvus/tempo. Leave PostgREST Gentoo-ban, polars agent-forbidden, sqlfluff AgentScan, sqlglot hostility, client-only drivers, compression codecs, Spark/Flink/Hadoop/Ceph/Postgres megas.

