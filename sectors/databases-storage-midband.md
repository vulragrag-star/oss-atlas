# Sector survey: databases-storage (midband 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/databases-storage-midband.jsonl` · Deep-sampled **62** real product repos via `raw.githubusercontent.com` policy files · Hard leaves respected · No fork/PR/comment · Band: `1k-5k`.

Playbook lens: famous main product (1k–5k★), not AgentScan, not hard AI ban, hunk class = **SQL/parser / storage-path / query-engine / DB-CLI bugs with regression tests** (not ecommerce apps, not pure client-driver farms, not sqlite.org).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 59 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 3 | Explicit AI-assisted / disclosure language |

Proceed: **46** · Leave: **16** · Appended to `survey/scored.jsonl` with `band: "1k-5k"`.

## Hard leaves (playbook — even if outside this band sample)

- `sqlite/sqlite` — AGENTS.md does not accept agentic code (higher band; already scored leave)
- SQLCipher / sqlite-culture guilt-by-fork — leave unless cleared
- Ecommerce apps / RAG apps in raw dump — wrong class

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `m3db/m3` | 4895 | silent | Distributed TSDB + query engine; Prom/Graphite surface | PromQL/tsdb path/query edge + Go tests |
| `rosedblabs/rosedb` | 4887 | silent | Embedded k-v storage engine; WAL/path edges | WAL/path/compaction edge + Go tests |
| `tidwall/buntdb` | 4867 | silent | Embedded k-v store; index/path edges | index/key path edge + Go tests |
| `apache/age` | 4805 | silent | Postgres graph extension; Cypher/SQL edges — ASF | Cypher/SQL parse edge + tests |
| `cberner/redb` | 4777 | disclosure | Embedded Rust DB; AGENTS disclosure trailer; page/path edges | page/path/tx edge + Rust tests — disclose AI trailer if used |
| `pgcentralfoundation/pgrx` | 4774 | silent | Postgres extension framework in Rust | extension SQL/SPI/path edge + Rust tests |
| `ydb-platform/ydb` | 4771 | silent | Distributed SQL DB; YQL/path edges — large but product | YQL/parse/path edge + tests |
| `prest/prest` | 4615 | silent | Postgres REST API; SQL/path/config edges | SQL/route/config edge + Go tests |
| `nalgeon/redka` | 4569 | silent | Redis reimplemented on SQL; cmd/SQL edges | Redis cmd/SQL edge + Go tests |
| `CrunchyData/postgres-operator` | 4445 | silent | Postgres operator; path/config/backup edges | operator path/config/backup edge + Go tests |
| `typedb/typedb` | 4444 | silent | TypeDB query engine; typeql parse edges | TypeQL parse/path edge + tests |
| `tair-opensource/RedisShake` | 4432 | silent | Redis data sync/migration CLI; addr/path edges | sync addr/path/filter edge + Go tests |
| `apache/kvrocks` | 4421 | silent | Redis-compatible RocksDB store; cmd/path edges | Redis cmd/path/storage edge + C++ tests |
| `Qovery/Replibyte` | 4408 | silent | DB seed/dump CLI; path/filter edges | dump path/filter/transform edge + Rust tests |
| `memgraph/memgraph` | 4406 | silent | In-memory graph DB; Cypher/query edges | Cypher/query/index edge + C++ tests |
| `canonical/dqlite` | 4374 | silent | Embedded replicated SQLite engine (Canonical) | raft/SQL/path edge + C tests |
| `nalgeon/sqlean` | 4368 | silent | SQLite extension set (not sqlite.org); SQL/func edges | SQL extension/func edge + tests |
| `pgbackrest/pgbackrest` | 4363 | silent | Postgres backup/restore CLI; path/stanza edges | backup path/stanza/config edge + C tests |
| `jorgerojas26/lazysql` | 4278 | silent | SQL TUI client; DSN/query/path edges | DSN/query/path edge + Go tests |
| `wal-g/wal-g` | 4242 | silent | DB archival/restore CLI; path/storage edges | archive path/storage edge + Go tests |
| `orioledb/orioledb` | 4185 | silent | Postgres table-access-method engine; storage edges | TAM/storage/path edge + C tests |
| `ledisdb/ledisdb` | 4114 | silent | Redis-like DB on LevelDB/RocksDB; cmd/path edges | cmd/path/storage edge + Go tests |
| `cozodb/cozo` | 4107 | silent | Embedded Datalog/graph DB; query/path edges | Datalog query/path edge + Rust tests |
| `timescale/pg_textsearch` | 3969 | silent | Postgres BM25 full-text extension | textsearch/SQL edge + C tests |
| `xo/dbtpl` | 3895 | silent | DB code generator CLI; schema/path edges | schema/path/template edge + Go tests |
| `vlcn-io/cr-sqlite` | 3784 | silent | CRDT SQLite extension (not sqlite.org) | CRDT/SQL virtual-table edge + tests |
| `alicebob/miniredis` | 3609 | silent | In-process Redis mock; command/parse edges | Redis command/parse edge + Go tests |
| `nutsdb/nutsdb` | 3578 | silent | Embedded k-v store; tx/path edges | tx/key path edge + Go tests |
| `hashicorp/go-memdb` | 3474 | silent | In-memory database built on go-immutable-radix | index/txn edge + Go tests |
| `apache/datafusion-sqlparser-rs` | 3449 | disclosure | SQL parser (DataFusion); ASF AGENTS disclosure | SQL dialect/parse edge + Rust tests — ASF generative-tooling |
| `rubenv/sql-migrate` | 3419 | silent | SQL migrations library/CLI; path/embed edges | migration path/embed edge + Go tests |
| `slatedb/slatedb` | 3391 | silent | Embedded DB on object storage; path/SST edges | SST/object-path edge + Rust tests |
| `PeerDB-io/peerdb` | 3263 | silent | Postgres CDC/ETL; SQL/slot/path edges | CDC slot/SQL/path edge + Go tests |
| `duckdb/pg_duckdb` | 3222 | silent | DuckDB as Postgres extension; SQL/type edges | SQL/type/extension edge + C++ tests |
| `danvergara/dblab` | 3200 | silent | DB TUI client; DSN/query edges | DSN/query/path edge + Go tests |
| `sqldef/sqldef` | 3153 | silent | Idempotent schema migration CLI; SQL diff edges | SQL DDL diff/path edge + Go tests |
| `gluesql/gluesql` | 3117 | silent | Rust SQL database; SQL parse/plan edges | SQL parse/plan edge + Rust tests |
| `lindb/lindb` | 3066 | silent | TSDB; ingest/query/path edges | ingest/query/path edge + Go tests |
| `redis/rueidis` | 2973 | silent | Redis Go client with strong protocol surface; RESP edges | RESP/protocol/path edge + Go tests |
| `dolthub/go-mysql-server` | 2656 | silent | MySQL-compatible SQL engine in Go | SQL parse/plan/path edge + Go tests |
| `sfu-db/connector-x` | 2649 | silent | Fast DB→DataFrame load; SQL/path edges | SQL/cursor/path edge + Rust tests |
| `jarulraj/sqlcheck` | 2522 | silent | SQL anti-pattern linter; parse/rule edges | SQL lint rule/parse edge + C++ tests |
| `man-group/ArcticDB` | 2509 | silent | DataFrame storage engine; path/version edges | storage path/version edge + C++/Py tests |
| `indradb/indradb` | 2460 | silent | Graph database; query/path edges | graph query/path edge + Rust tests |
| `bytedance/terarkdb` | 2154 | silent | RocksDB-derived storage engine | SST/compaction/path edge + C++ tests |
| `duckdb/duckdb-wasm` | 2118 | silent | DuckDB in WASM; SQL/FS path edges | SQL/VFS path edge + tests |

### Tier notes

**Best first homes (small testable parser/path/format hunks):** start near the top of the proceed table; one home at a time; stay after a merge.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `uptrace/bun` | 4963 | silent | Go ORM — prefer SQL engines/CLIs over ORM wrappers |
| `Qihoo360/Atlas` | 4617 | silent | MySQL proxy — stale relative signal / Chinese-maintainer queue |
| `rusqlite/rusqlite` | 4383 | silent | SQLite Rust bindings — satellite-ish; sqlite.org agentic culture adjacent |
| `redis-rs/redis-rs` | 4249 | silent | Redis client library — not storage engine product |
| `Netflix/dynomite` | 4213 | silent | Dynamo proxy layer — quieter / ops-heavy |
| `go-mysql-org/go-mysql-elasticsearch` | 4146 | silent | MySQL→ES sync — pipeline glue not DB engine |
| `rust-postgres/rust-postgres` | 3999 | silent | Postgres Rust driver — client library |
| `upper/db` | 3657 | silent | Go ORM — weak engine/parser hunk fit |
| `ClickHouse/clickhouse-go` | 3338 | disclosure | ClickHouse Go driver — client not engine; AI_POLICY disclosure |
| `polardb/PolarDB-for-PostgreSQL` | 3200 | silent | Alibaba Postgres fork — heavy; unclear outsider process |
| `mkleehammer/pyodbc` | 3080 | silent | ODBC driver binding — not DB product core |
| `fnc12/sqlite_orm` | 2693 | silent | SQLite ORM — not engine; sqlite-culture adjacent |
| `google/googlesql` | 2638 | silent | SQL library surface — unclear outsider home vs engines |
| `rust-rocksdb/rust-rocksdb` | 2176 | silent | RocksDB Rust bindings — binding satellite |
| `denisenkom/go-mssqldb` | 1883 | silent | MSSQL driver — client library |
| `mongodb/mongo-rust-driver` | 1517 | silent | Mongo driver — not engine; prefer engine homes |

## Sector synthesis

- Midband (1k-5k) deep sample: **62** curated product repos.
- Proceed **46** / Leave **16**.
- Disclosure repos: `cberner/redb`, `apache/datafusion-sqlparser-rs`, `ClickHouse/clickhouse-go`.
- No AgentScan / fish-style / sqlite-agentic hits inside this midband sample (those hard leaves live in higher-star scored set).
- Method: policy files via `raw.githubusercontent.com` (CONTRIBUTING*/AI*/AGENTS*/PR templates); local AgentScan blacklist only.
- No fork / PR / tracker comment performed.

## Deepen pass (2026-09-08, +40 scored)

Account: `vulragrag-star` · Curated product midband slice from remaining unscored `databases-storage-midband` raw · Policy via `raw.githubusercontent.com` · **31** proceed / **9** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 38, 'disclosure': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `go-mysql-org/go-mysql` | 4964 | silent | MySQL toolset (binlog/replication/dump); protocol/SQL edges | binlog/SQL/protocol parse edge + Go tests |
| `s3tools/s3cmd` | 4908 | silent | S3-compatible object storage CLI; path/ACL/url edges | S3 path/ACL/URL encode edge + py tests |
| `superfly/litefs` | 4877 | silent | FUSE SQLite replication filesystem; path/lease edges | FUSE path/lease/replication edge + Go tests |
| `sorintlab/stolon` | 4827 | silent | Postgres cloud-native HA; config/keeper/path edges | keeper/config/path edge + Go tests |
| `Maxteabag/sqlit` | 4813 | silent | SQL multi-engine TUI; DSN/query/path edges | DSN/query/path edge + py tests |
| `infiniflow/infinity` | 4704 | silent | AI-native hybrid search DB; query/index/path edges | query/index/path edge + C++ tests |
| `deuxfleurs-org/garage` | 4475 | silent | S3-compatible geo-distributed object store; path/key edges | S3 path/key/layout edge + Rust tests |
| `pgbouncer/pgbouncer` | 4350 | silent | Postgres connection pooler; auth/DSN/config edges | auth/DSN/config edge + C tests |
| `k1LoW/tbls` | 4340 | silent | CI-friendly DB schema doc CLI; path/schema edges | schema/path/doc edge + Go tests |
| `unum-cloud/USearch` | 4292 | silent | Vector search/clustering engine; metric/path edges | index/metric/path edge + C++ tests |
| `coleifer/sqlite-web` | 4155 | silent | Web SQLite browser (not sqlite.org); SQL/path edges | SQL/path/web edge + py tests |
| `postgresml/pgcat` | 4011 | silent | Postgres pooler with sharding/failover; config/route edges | pool route/config/path edge + Rust tests |
| `offen/docker-volume-backup` | 4002 | silent | Docker volume backup to S3/WebDAV; path/storage edges | backup path/storage edge + Go tests |
| `bruin-data/ingestr` | 3950 | silent | Cross-database copy CLI; source/URI/path edges | source URI/path/transform edge + Go tests |
| `RedisJSON/RedisJSON` | 3947 | silent | Redis JSON data type module; path/JSON cmd edges | JSON path/cmd edge + Rust tests |
| `maplibre/martin` | 3898 | silent | PostGIS/MBTiles tile server; path/SQL edges | tile path/SQL/source edge + Rust tests |
| `citusdata/pg_cron` | 3883 | silent | Postgres job scheduler extension; SQL/schedule edges | cron SQL/schedule edge + C tests |
| `HDT3213/godis` | 3835 | silent | Go Redis server/cluster; RESP/cmd/path edges | RESP/cmd/path edge + Go tests |
| `go-jet/jet` | 3791 | silent | Type-safe SQL builder + codegen; SQL/dialect edges | SQL dialect/builder edge + Go tests |
| `oliver006/redis_exporter` | 3687 | silent | Prometheus exporter for Redis/Valkey; metric/addr edges | metric/addr/config edge + Go tests |
| `frectonz/sql-studio` | 3684 | silent | Multi-engine SQL explorer; DSN/query/path edges | DSN/query/path edge + Rust tests |
| `spdk/spdk` | 3664 | silent | Storage Performance Development Kit; NVMe/path edges | NVMe/path/config edge + C tests |
| `yandex/odyssey` | 3622 | silent | Scalable Postgres connection pooler; auth/route edges | auth/route/config edge + C tests |
| `prometheus-community/postgres_exporter` | 3609 | silent | Postgres Prometheus exporter; query/metric edges | collector query/metric edge + Go tests |
| `mergestat/mergestat-lite` | 3520 | silent | Query git repos with SQL; SQL/git path edges | SQL/git path edge + Go tests |
| `olric-data/olric` | 3495 | silent | Distributed in-memory KV/cache; key/partition edges | key/partition/path edge + Go tests |
| `documentdb/documentdb` | 3437 | disclosure | MongoDB-compatible document engine; query/path edges | query/BSON/path edge + C tests |
| `roapi/roapi` | 3433 | silent | Read-only API over datasets; SQL/path/format edges | SQL/path/format edge + Rust tests |
| `lakehq/sail` | 3358 | silent | Spark-replacement engine in Rust; SQL/plan edges | SQL/plan/path edge + Rust tests |
| `supabase/pg_graphql` | 3347 | silent | GraphQL for Postgres; GraphQL/SQL edges | GraphQL/SQL resolve edge + Rust tests |
| `facebook/mcrouter` | 3335 | silent | Memcached protocol router; route/config edges | route/config/path edge + C++ tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `skyzh/mini-lsm` | 4161 | silent | Learning/course LSM storage engine — not production home |
| `aws/aws-sdk-pandas` | 4120 | silent | AWS pandas SDK integration — not DB product core |
| `go-redsync/redsync` | 4044 | silent | Redis distributed lock library — not storage engine |
| `talent-plan/tinykv` | 3988 | silent | Course to build KV on TiKV model — educational, not product |
| `ponyorm/pony` | 3818 | silent | Python ORM — prefer SQL engines/CLIs over ORM wrappers |
| `pgadmin-org/pgadmin4` | 3781 | disclosure | Heavy multi-surface admin GUI — weak small hunk/outsider fit |
| `psycopg/psycopg2` | 3654 | silent | Postgres Python driver — client binding, not engine |
| `nullptrlabs/pgmodeler` | 3593 | silent | Postgres GUI data-modeling tool — prefer SQL/CLI engines |
| `tikv/raft-rs` | 3386 | silent | Raft consensus library — not a DB/storage product home |

Notes: `documentdb/documentdb` PR template checkbox “No AI tools were used” is disclosure UX, not a ban — CONTRIBUTING welcomes AI-assisted with transparency. Keep sqlite.org culture leaves intact; `coleifer/sqlite-web` is not sqlite.org.

