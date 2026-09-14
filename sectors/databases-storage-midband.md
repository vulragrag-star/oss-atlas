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

## Product deepen-2 midband subset (2026-09-10, +55 scored)

Account: `vulragrag-star` · Curated product DB/storage homes still missing after prior databases-storage passes · Policy via `raw.githubusercontent.com` · **38** proceed / **17** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 53, 'disclosure': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `livestorejs/livestore` | 3698 | silent | Reactive SQLite state framework; sync/SQL edges | SQL/sync/path edge + TS tests |
| `holistics/dbml` | 3690 | silent | Database Markup Language; parse/schema edges | DBML parse/schema edge + JS tests |
| `danfengcao/binlog2sql` | 3554 | silent | MySQL binlog→SQL parser CLI; binlog/SQL edges | binlog/SQL parse edge + py tests |
| `uber/aresdb` | 3076 | silent | GPU analytics storage/query engine; ingest/path edges | ingest/query/path edge + Go tests |
| `heavyai/heavydb` | 3060 | silent | GPU SQL analytics DB (ex-MapD); SQL/path edges | SQL/path/storage edge + C++ tests |
| `oceanbase/seekdb` | 2916 | silent | AI-native hybrid search DB; vector/SQL edges | vector/SQL/path edge + C++ tests |
| `orbitinghail/sqlsync` | 2912 | silent | Collaborative offline-first SQLite wrapper; sync/SQL edges | sync/SQL/path edge + Rust tests |
| `armink/FlashDB` | 2840 | silent | Ultra-light embedded KV/TSDB; path/KV edges | KV/TS path edge + C tests |
| `pipelinedb/pipelinedb` | 2663 | silent | Postgres continuous aggregation extension; SQL edges | SQL continuous-agg edge + C tests |
| `sqlpage/SQLPage` | 2558 | silent | SQL-only app builder; SQL/route/path edges | SQL/route/path edge + Rust tests |
| `griddb/griddb` | 2475 | silent | IoT time-series DB; query/path edges | TS query/path edge + C++ tests |
| `noborus/trdsql` | 2173 | silent | SQL over CSV/JSON/YAML CLI; dialect/path edges | SQL dialect/path edge + Go tests |
| `RedisGraph/RedisGraph` | 2040 | silent | Redis graph module; Cypher/cmd edges | Cypher/cmd/path edge + C tests |
| `Mooncake-Labs/pg_mooncake` | 2004 | silent | Real-time analytics on Postgres tables; SQL edges | SQL/analytics extension edge + Rust tests |
| `asg017/sqlite-vss` | 1998 | silent | SQLite vector-search extension (Faiss); SQL/vtab edges | vtab/SQL/vector edge + C++ tests |
| `yinqiwen/ardb` | 1847 | silent | Redis-protocol store on LevelDB/RocksDB; cmd/path edges | cmd/path/storage edge + C++ tests |
| `mathaou/termdbms` | 1821 | silent | DB TUI for viewing/editing; DSN/query edges | DSN/query/path edge + Go tests |
| `alibaba/MongoShake` | 1820 | silent | MongoDB oplog replication platform; oplog/path edges | oplog/filter/path edge + Go tests |
| `RedisBloom/RedisBloom` | 1783 | silent | Redis probabilistic datatypes module; cmd edges | Bloom/cmd edge + C tests |
| `citusdata/cstore_fdw` | 1783 | silent | Postgres columnar FDW; SQL/storage edges | columnar FDW/SQL edge + C tests |
| `TuGraph-family/tugraph-db` | 1759 | silent | High-performance graph DB; Cypher/path edges | Cypher/query/path edge + C++ tests |
| `cnosdb/cnosdb` | 1756 | silent | Cloud-native distributed TSDB; SQL/path edges | TS SQL/path edge + Rust tests |
| `4paradigm/OpenMLDB` | 1711 | silent | ML feature database; SQL/path edges | SQL/feature/path edge + C++ tests |
| `osm2pgsql-dev/osm2pgsql` | 1682 | disclosure | OSM→PostGIS importer; SQL/path edges | import path/SQL edge + C++ tests |
| `cswinter/LocustDB` | 1648 | silent | Fast analytics DB; query/path edges | query/path/ingest edge + Rust tests |
| `mgartner/pg_flame` | 1620 | silent | Postgres EXPLAIN flamegraph generator; plan/parse edges | EXPLAIN parse/path edge + Go tests |
| `losfair/mvsqlite` | 1576 | silent | Distributed MVCC SQLite on FoundationDB; SQL edges | MVCC/SQL/path edge + Rust tests |
| `polarsignals/frostdb` | 1546 | silent | Embeddable columnar DB in Go; path/schema edges | column/path/schema edge + Go tests |
| `nfrastack/db-backup` | 1537 | silent | Multi-backend DB backup/restore CLI; path edges | backup path/URI edge + Go tests |
| `BemiHQ/BemiDB` | 1533 | silent | Postgres-compatible analytics warehouse; SQL edges | SQL/warehouse path edge + Go tests |
| `Softmotions/ejdb` | 1481 | silent | Embeddable JSON DB; query/path edges | JSON query/path edge + C tests |
| `Mithril-mine/libmdbx` | 1460 | silent | Transactional KV storage engine (MDBX); path edges | txn/path/map edge + C tests |
| `cybertec-postgresql/pg_timetable` | 1396 | silent | Advanced Postgres job scheduler; SQL/schedule edges | schedule/SQL/path edge + Go tests |
| `apache/cloudberry` | 1394 | disclosure | MPP Postgres-fork analytics DB; SQL/path edges | SQL/path/MPP edge + C tests |
| `hapostgres/pg_auto_failover` | 1386 | silent | Postgres HA failover extension/service; config edges | failover/config/path edge + C tests |
| `sqls-server/sqls` | 1334 | silent | SQL language server; dialect/parse edges | SQL parse/LSP edge + Go tests |
| `kndndrj/nvim-dbee` | 1312 | silent | Neovim interactive DB client; DSN/query edges | DSN/query/path edge + Go tests |
| `PoloDB/PoloDB` | 1233 | silent | Embedded document database; query/path edges | doc query/path edge + Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `sqlectron/sqlectron` | 4758 | silent | Desktop SQL client GUI — prefer CLI/engine homes |
| `sidorares/node-mysql2` | 4384 | silent | MySQL Node driver — client binding, prefer engines/CLIs |
| `liyupi/sql-mother` | 4366 | silent | Interactive SQL tutorial site — not product engine |
| `whoiskatrin/sql-translator` | 4320 | silent | NL→SQL translator app — not DB/storage core |
| `bigchaindb/bigchaindb` | 4033 | silent | Archived/stale blockchain DB culture — weak modern fit |
| `bytebase/dbhub` | 3475 | silent | DB MCP server for agents — agent-product adjacency, leave |
| `undb-io/undb` | 2976 | silent | No-code BaaS database app — web/product app, not engine |
| `ServiceStack/redis-windows` | 2730 | silent | Windows Redis port/Vagrant packaging — leave ports |
| `sewenew/redis-plus-plus` | 1984 | silent | Redis C++ client library — not storage product |
| `bsm/redislock` | 1767 | silent | Redis lock helper library — not storage engine |
| `huandu/go-sqlbuilder` | 1727 | silent | SQL string builder/ORM helper — prefer engines/CLIs |
| `CovenantSQL/CovenantSQL` | 1527 | silent | Blockchain SQL experiment — not mainstream product home |
| `Grokzen/docker-redis-cluster` | 1517 | silent | Docker Redis cluster packaging — not product core |
| `2shady4u/godot-sqlite` | 1431 | silent | Godot SQLite wrapper — engine plugin, wrong surface |
| `PumpkinDB/PumpkinDB` | 1402 | silent | Inactive educational immutable KV — weak velocity |
| `prodrigestivill/docker-postgres-backup-local` | 1194 | silent | Docker backup wrapper — packaging, not DB product |
| `n0b0dyCN/redis-rogue-server` | 1171 | silent | Redis RCE exploit demo — security toy, leave |

Notes: Prefer SQL/CLI/engine edges (trdsql, termdbms, frostdb, BemiDB, pg_timetable, sqls, PoloDB, mvsqlite, sqlite-vss, RedisBloom/Graph). Leave redis clients/locks, blockchain SQL toys, Godot wrappers, exploit demos, and inactive educational KV engines.

## Midband product deepen (2026-09-12, +83 scored)

Account: `vulragrag-star` · Curated databases-storage midband (1k–5k★) product engines/KV/TSDB/vector/search/object-storage/backup/migrate/SQL-CLI/ORM homes still missing after prior DB midband + product deepens · Policy via `raw.githubusercontent.com` · **57** proceed / **26** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 79, 'disclosure': 3, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `crate/crate` | 4435 | disclosure | Distributed SQL DB for machine data — disclose | SQL/distributed query edge + Java tests |
| `facebookincubator/velox` | 4209 | silent | Composable C++ execution engine | expr/vectorized exec edge + C++ tests |
| `tarantool/tarantool` | 3666 | silent | In-memory computing + DB platform (product) | Lua/SQL/storage edge + C tests |
| `terminusdb/terminusdb` | 3411 | silent | Collaborative graph DB | WOQL/document/path edge + Prolog tests |
| `delta-io/delta-rs` | 3298 | silent | Native Rust Delta Lake library | transaction/log/path edge + Rust tests |
| `storj/storj` | 3282 | silent | Decentralized S3-compatible object storage | object key/path/ACL edge + Go tests |
| `mydumper/mydumper` | 3223 | silent | MySQL logical dump/restore CLI | dump/restore/path edge + C tests |
| `Tencent/Tendis` | 3157 | silent | Redis-compatible distributed storage on RocksDB | cmd/storage/path edge + C++ tests |
| `timescale/pgvectorscale` | 3127 | silent | Postgres DiskANN vector extension | index/search/SQL edge + tests |
| `hydra-db/hydradb` | 3083 | silent | Graph database on object storage | graph/query/object-store edge + tests |
| `hydradatabase/columnar` | 3042 | silent | Postgres-native columnar storage extension | columnar scan/storage edge + tests |
| `pgpartman/pg_partman` | 2821 | silent | Postgres partition management extension | partition/maintain SQL edge + tests |
| `maxpert/marmot` | 2819 | silent | Distributed SQLite with MySQL wire | SQLite/replication/wire edge + Go tests |
| `XiaoMi/Gaea` | 2764 | silent | MySQL proxy (Xiaomi) | route/auth/SQL edge + Go tests |
| `postgres-ai/database-lab-engine` | 2710 | silent | Postgres thin-clone / branching engine | clone/ZFS/path edge + Go tests |
| `paypal/junodb` | 2636 | silent | PayPal consistent HA KV store | KV/replication/path edge + tests |
| `multigres/multigres` | 2616 | disclosure | Vitess-for-Postgres — disclose | shard/route/SQL edge + Go tests |
| `Altinity/clickhouse-operator` | 2563 | silent | ClickHouse Kubernetes operator | CRD/config/path edge + Go tests |
| `tidwall/pogocache` | 2516 | silent | Low-latency caching/KV software product | cmd/latency path edge + C tests |
| `rbatis/rbatis` | 2485 | silent | Compile-time async dynamic SQL ORM | SQL/ORM/compile edge + C++ tests |
| `wiredtiger/wiredtiger` | 2424 | silent | WiredTiger storage engine | page/storage/tx edge + C tests |
| `VexDB-THU/VexDB-Lite` | 2378 | silent | Cross-platform embedded vector DB | vector/query/path edge + tests |
| `supabase/etl` | 2329 | silent | Postgres replication engine in Rust | logical repl/CDC path edge + Rust tests |
| `fjall-rs/fjall` | 2317 | silent | Embeddable LSM key-value engine in Rust | LSM/compaction/path edge + Rust tests |
| `symisc/unqlite` | 2315 | silent | Embedded NoSQL transactional DB engine | doc/KV/tx edge + C tests |
| `reorg/pg_repack` | 2303 | silent | Online Postgres table repack | rewrite/lock/path edge + C tests |
| `apache/datafusion-ballista` | 2134 | silent | Distributed DataFusion query engine | scheduler/query/path edge + Rust tests |
| `feldera/feldera` | 2085 | silent | Incremental computation / streaming SQL engine | pipeline/SQL edge + Rust tests |
| `TileDB-Inc/TileDB` | 2077 | silent | Universal array storage engine | array/fragment/path edge + C++ tests |
| `toeverything/OctoBase` | 2065 | silent | Local-first DB behind AFFiNE | CRDT/storage/path edge + Rust tests |
| `twitter/pelikan` | 1957 | silent | Twitter unified cache backend (KV) | protocol/cache path edge + C tests |
| `microsoft/DiskANN` | 1923 | silent | DiskANN vector indexing library | graph/index/path edge + C++ tests |
| `SeekStorm/SeekStorm` | 1909 | silent | Vector + lexical search engine/library | index/query/path edge + Rust tests |
| `pmwkaa/sophia` | 1887 | silent | Transactional key-value/row storage library | MVCC/storage path edge + C tests |
| `oxigraph/oxigraph` | 1877 | silent | SPARQL graph database | SPARQL/RDF/path edge + Rust tests |
| `arkdb/inception` | 1873 | silent | MySQL audit/execute/backup ops tool | SQL audit/backup edge + tests |
| `fabianlindfors/reshape` | 1849 | silent | Zero-downtime Postgres schema migration | migrate/lock/SQL edge + Rust tests |
| `radondb/radon` | 1795 | silent | Cloud-native sharded MySQL | shard/SQL/proxy edge + Go tests |
| `supervc-stack/VectorChord` | 1789 | silent | Disk-friendly Postgres vector search | index/search/SQL edge + tests |
| `hanchuanchuan/goInception` | 1744 | silent | Go MySQL audit/execute/backup tool | SQL audit/backup edge + Go tests |
| `LadybugDB/ladybug` | 1738 | silent | Graph database product | graph/query/path edge + tests |
| `EnterpriseDB/repmgr` | 1711 | silent | Postgres replication manager | standby/failover/config edge + C tests |
| `HypoPG/hypopg` | 1710 | silent | Hypothetical indexes for Postgres | planner/index edge + tests |
| `chaisql/chai` | 1704 | silent | Modern embedded SQL database | SQL/parser/storage edge + Go tests |
| `pgaudit/pgaudit` | 1703 | silent | Postgres audit extension | audit log/SQL edge + tests |
| `rust-db/refinery` | 1700 | silent | Rust SQL migration toolkit | migrate/path/SQL edge + Rust tests |
| `lesovsky/pgcenter` | 1625 | silent | Postgres admin/observability CLI | stats/query/path edge + Go tests |
| `tonbo-io/tonbo` | 1619 | silent | Embedded DB for serverless/edge | LSM/arrow/path edge + Rust tests |
| `percona/percona-xtrabackup` | 1556 | silent | Hot backup for InnoDB/XtraDB | backup/restore/path edge + tests |
| `percona/percona-toolkit` | 1549 | silent | Advanced MySQL/Postgres ops toolkit | pt-tool path/SQL edge + Perl tests |
| `mariadb-corporation/MaxScale` | 1496 | silent | Intelligent DB proxy | route/filter/protocol edge + C++ tests |
| `skeema/skeema` | 1381 | silent | Declarative MySQL/MariaDB schema CLI | diff/migrate/path edge + Go tests |
| `rwynn/monstache` | 1332 | silent | MongoDB→Elasticsearch sync daemon | change-stream/mapping edge + Go tests |
| `apache/impala` | 1287 | disclosure | Apache Impala MPP SQL — disclose | SQL/scan/fragment edge + tests |
| `percona/percona-server` | 1270 | silent | Percona MySQL server fork product | SQL/storage/config edge + tests |
| `openGemini/openGemini` | 1174 | silent | CNCF distributed time-series DB | TSDB ingest/query edge + Go tests |
| `RedisTimeSeries/RedisTimeSeries` | 1070 | silent | Redis time-series module | TS cmd/retention edge + C tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `objectbox/objectbox-java` | 4622 | silent | Mobile/JVM embedded DB client SDK — leave |
| `toshi-search/Toshi` | 4256 | silent | Stale educational full-text engine — leave |
| `eyebluecn/tank` | 3235 | silent | Cloud-disk / file manager GUI — leave GUI managers |
| `LMDB/lmdb` | 3039 | silent | Read-only OpenLDAP mirror; issues/PRs ignored — leave |
| `nicolasff/webdis` | 2965 | silent | Thin Redis HTTP interface wrapper — leave thin gateway |
| `Forceu/Gokapi` | 2862 | silent | Self-hosted file-share app — leave share/GUI class |
| `HouzuoGuo/tiedot` | 2724 | silent | Rudimentary unmaintained document DB toy — leave |
| `rbock/sqlpp11` | 2625 | silent | C++ SQL template library — leave client/template lib |
| `neilotoole/sq` | 2564 | hard_ban | AGENTS.md NO-AI — hard leave data wrangler CLI |
| `Tencent/phxsql` | 2445 | silent | Legacy unmaintained MySQL HA cluster — leave |
| `apache/geode` | 2383 | silent | In-memory data-grid platform mega — leave platform class |
| `armink/EasyFlash` | 2366 | silent | IoT firmware KV/IAP on flash — leave embedded firmware |
| `alibaba/tair` | 2314 | silent | Legacy Alibaba KV (stale contrib surface) — leave |
| `Meituan-Dianping/DBProxy` | 2266 | silent | Legacy empty-desc MySQL proxy — leave |
| `jiangwenyuan/nuster` | 1903 | silent | HTTP proxy cache / RESTful NoSQL cache — networking spill |
| `baidu/tera` | 1902 | silent | Legacy Internet-scale DB (stale) — leave |
| `ttionya/vaultwarden-backup` | 1876 | silent | Thin vaultwarden backup packaging script — leave |
| `foyer-rs/foyer` | 1804 | silent | Hybrid cache library — leave cache abstraction class |
| `julien040/anyquery` | 1774 | silent | Multi-tool SQL connector / Text-to-SQL-ish app — leave |
| `SeaQL/sea-query` | 1758 | silent | SQL query builder library (sea-orm is the product home) |
| `gobuffalo/pop` | 1524 | silent | Thin Go ORM/helper — leave lightweight wrapper |
| `kelindar/column` | 1512 | silent | In-memory columnar store library — leave library class |
| `sist2app/sist2` | 1301 | silent | Filesystem indexer/search — not DB/storage product |
| `citusdata/postgresql-hll` | 1230 | silent | Narrow HyperLogLog datatype extension — leave niche |
| `mdbtools/mdbtools` | 1172 | silent | MS Access reader toolkit — niche format leave |
| `realm/realm-core` | 1053 | silent | Realm mobile database core — leave mobile client class |

Notes: Prefer midband product DB/storage homes (engines/KV/TSDB/vector/search/object-storage/backup/migrate/SQL-CLI/ORM). Disclosure: crate/multigres/impala. Hard leave: neilotoole/sq (NO-AI). Leave cache libs (caffeine/ristretto/foyer), mobile ORMs (greenDAO/objectbox/realm), GUI/share apps (tank/Gokapi), data-grid platforms (geode/hazelcast/ignite), analytics transform (dbt), Text-to-SQL/connectors (anyquery), mirrors (LMDB/xapian), legacy proxies, thin wrappers.

## Midband product deepen-2 (2026-09-13, +105 scored)

Account: `vulragrag-star` · Curated databases-storage midband (1k–5k★) leftover product engines/KV/TSDB/vector/search/object-storage/backup/migrate/SQL-CLI/ORM/proxy homes after prior databases-storage midband product deepen · Policy via `raw.githubusercontent.com` · **60** proceed / **45** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 99, 'disclosure': 5, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `malisper/pgrust` | 4992 | silent | Postgres rewritten in Rust (engine leftover) | SQL/parser/storage path edge + rust tests |
| `orientechnologies/orientdb` | 4985 | silent | Multi-model DBMS (graph/document) | query/schema/path edge + java tests |
| `google/pebble` | 4961 | silent | Google Pebble KV/LSM storage engine | compaction/WAL/path edge + C tests |
| `catfan/Medoo` | 4950 | silent | Lightweight PHP database framework | query builder/path edge + php tests |
| `pudo/dataset` | 4872 | silent | Python SQL data handling library | SQL load/query/path edge + python tests |
| `tokio-rs/mini-redis` | 4785 | silent | Educational Redis client/server in Tokio | RESP/protocol/path edge + rust tests |
| `doctrine/migrations` | 4766 | silent | Doctrine DB migrations library | migration/version/path edge + php tests |
| `h2database/h2database` | 4628 | silent | Embeddable Java RDBMS | SQL/engine/path edge + java tests |
| `cakephp/phinx` | 4540 | silent | PHP database migrations for everyone | migration/path edge + php tests |
| `praeclarum/sqlite-net` | 4459 | silent | Cross-platform SQLite client+ORM | SQLite ORM/path edge + csharp tests |
| `oceanbase/miniob` | 4416 | silent | Compact teaching/research database | executor/storage/path edge + C++ tests |
| `dotnetcore/FreeSql` | 4405 | silent | .NET AOT ORM multi-DB | ORM mapping/path edge + csharp tests |
| `isar/hive` | 4392 | silent | Dart/Flutter key-value database | KV path/serialize edge + dart tests |
| `isar/isar` | 4024 | silent | Async Dart NoSQL database | NoSQL query/path edge + dart tests |
| `borisdj/EFCore.BulkExtensions` | 3999 | silent | EF Core bulk/batch extensions | bulk SQL/path edge + csharp tests |
| `ravendb/ravendb` | 3998 | silent | ACID document database | doc store/query/path edge + csharp tests |
| `mongodb/mongoid` | 3914 | silent | Official Ruby ODM for MongoDB | ODM query/path edge + ruby tests |
| `apache/kylin` | 3773 | silent | Apache Kylin OLAP engine | cube/query/path edge + java tests |
| `go-gorp/gorp` | 3744 | silent | Go ORM-ish persistence library | ORM mapping/path edge + go tests |
| `apache/arrow-rs` | 3607 | silent | Official Rust Apache Arrow | Arrow IPC/array/path edge + rust tests |
| `Netflix/atlas` | 3562 | silent | In-memory dimensional TSDB | timeseries query/path edge + scala tests |
| `apache/lucene` | 3554 | disclosure | Apache Lucene search library | index/query/path edge + java tests |
| `fluentmigrator/fluentmigrator` | 3511 | silent | .NET fluent migrations framework | migration/path edge + csharp tests |
| `JasperFx/marten` | 3453 | silent | .NET document DB + event store on Postgres | doc/event/path edge + csharp tests |
| `sqlkata/querybuilder` | 3379 | silent | C# SQL query builder | SQL builder/path edge + csharp tests |
| `linq2db/linq2db` | 3326 | silent | LINQ to database provider | LINQ/SQL path edge + csharp tests |
| `adelsz/pgtyped` | 3280 | silent | Typesafe SQL in TypeScript | SQL codegen/path edge + ts tests |
| `simolus3/drift` | 3273 | silent | Reactive Dart persistence library | SQLite/query/path edge + dart tests |
| `EnterpriseDB/barman` | 3236 | disclosure | Postgres backup & recovery manager | backup/WAL/path edge + python tests |
| `jaredwray/keyv` | 3200 | silent | Simple multi-backend key-value storage | KV adapter/path edge + js tests |
| `teamtnt/tntsearch` | 3196 | silent | PHP full-text search engine | index/search/path edge + php tests |
| `vortex-data/vortex` | 3193 | disclosure | Extensible columnar storage framework | columnar codec/path edge + rust tests |
| `apache/hugegraph` | 3175 | silent | Large-scale graph database | graph query/path edge + java tests |
| `sqitchers/sqitch` | 3158 | silent | Sensible database change management | migrate/deploy/path edge + perl tests |
| `apache/parquet-java` | 3079 | silent | Apache Parquet Java | Parquet read/write/path edge + java tests |
| `dresende/node-orm2` | 3043 | silent | Node.js ORM | ORM mapping/path edge + js tests |
| `doug-martin/goqu` | 2675 | silent | Go SQL builder and query library | SQL builder/path edge + go tests |
| `db-migrate/node-db-migrate` | 2343 | silent | Node database migration framework | migration/path edge + js tests |
| `borgmatic-collective/borgmatic` | 2324 | disclosure | Config-driven Borg backup wrapper | backup config/path edge + python tests |
| `tidwall/redcon` | 2306 | silent | Redis-compatible server framework (Go) | RESP server/path edge + go tests |
| `speedment/speedment` | 2092 | silent | Java Stream ORM toolkit | Stream ORM/path edge + java tests |
| `apache/drill` | 2023 | silent | Apache Drill MPP query layer | SQL/query/path edge + java tests |
| `schemacrawler/SchemaCrawler` | 1828 | silent | DB schema discovery tooling | schema crawl/path edge + java tests |
| `stephenafamo/bob` | 1778 | silent | Go SQL query builder + ORM generator | SQL/ORM gen/path edge + go tests |
| `SOCI/soci` | 1622 | silent | C++ database access library | DB access/path edge + C++ tests |
| `xormplus/xorm` | 1554 | silent | Go ORM library (xorm fork) | ORM mapping/path edge + go tests |
| `salsita/node-pg-migrate` | 1482 | silent | Node Postgres migration manager | migration/path edge + ts tests |
| `peterbourgon/diskv` | 1454 | silent | Disk-backed key-value store | KV disk/path edge + go tests |
| `yongman/tidis` | 1442 | silent | Distributed transactional Redis-protocol NoSQL | txn/KV/path edge + go tests |
| `Tencent/TBase` | 1442 | silent | Enterprise distributed HTAP database | HTAP/SQL/path edge + C tests |
| `pgRouting/pgrouting` | 1431 | silent | Postgres routing extension | graph routing SQL/path edge + C++ tests |
| `xitongsys/parquet-go` | 1431 | silent | Pure Go Parquet read/write | Parquet codec/path edge + go tests |
| `apache/iceberg-rust` | 1404 | disclosure | Apache Iceberg Rust | Iceberg table/path edge + rust tests |
| `akrylysov/pogreb` | 1349 | silent | Embedded KV for read-heavy workloads | KV embed/path edge + go tests |
| `dotnetcore/sharding-core` | 1286 | silent | EFCore sharding solution | shard routing/path edge + csharp tests |
| `sbdchd/squawk` | 1173 | silent | Linter for Postgres migrations & SQL | SQL lint/path edge + rust tests |
| `go-gormigrate/gormigrate` | 1173 | silent | Minimal Gorm migration helper | migration/path edge + go tests |
| `ArcadeData/arcadedb` | 1153 | silent | Multi-model database | multi-model query/path edge + java tests |
| `sqliteai/sqlite-vector` | 1140 | silent | SQLite vector extension | vector index/path edge + C tests |
| `apache/iceberg-python` | 1131 | silent | PyIceberg | Iceberg table/path edge + python tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `gajus/slonik` | 4941 | silent | typed Postgres client library; thin client surface |
| `backup/backup` | 4856 | silent | generic UNIX full-stack backup gem; not DB-specific |
| `SPLWare/esProc` | 4685 | silent | SPL programming language for data; language/tooling spill |
| `spatie/laravel-query-builder` | 4469 | silent | Laravel Eloquent API query builder; framework glue |
| `autobase-tech/autobase` | 4379 | silent | automated Postgres DBaaS platform; PaaS mega class |
| `apache/lucene-solr` | 4365 | silent | archived Solr+Lucene monorepo mirror; prefer apache/lucene |
| `zendesk/maxwell` | 4260 | silent | MySQL binlog→Kafka producer; messaging spill |
| `sjqzhang/go-fastdfs` | 4138 | silent | private cloud DFS; object-storage-adjacent but ops platform |
| `fastmonkeys/stellar` | 3851 | silent | dev DB snapshot tool; quiet/stale |
| `mevdschee/php-crud-api` | 3739 | silent | single-file PHP REST API over SQL; thin CRUD scaffold |
| `schemaspy/schemaspy` | 3719 | silent | DB schema documentation GUI/site generator |
| `phiresky/sql.js-httpvfs` | 3698 | silent | read-only sqlite-over-HTTP vfs novelty |
| `linkedin/databus` | 3682 | silent | stale LinkedIn CDC; largely unmaintained legacy |
| `rsnapshot/rsnapshot` | 3668 | silent | generic rsync backup; not DB/storage product primary |
| `scenic-views/scenic` | 3624 | silent | Rails DB views helper; framework glue |
| `laurent22/rsync-time-backup` | 3608 | silent | generic Time Machine-style rsync; not DB product |
| `dalibo/pev2` | 3592 | silent | Postgres explain visualizer UI |
| `wal-e/wal-e` | 3463 | silent | legacy Postgres WAL archiver; prefer wal-g; quiet |
| `towhee-io/towhee` | 3451 | silent | ML embedding pipeline framework; vector-adjacent not DB engine |
| `codemix/ts-sql` | 3306 | silent | SQL-in-TypeScript-types novelty; not product DB |
| `Wisser/Jailer` | 3198 | silent | DB subsetting/browsing GUI tool |
| `alibaba/cobar` | 3187 | silent | legacy MySQL sharding proxy; superseded by other proxies |
| `dosco/graphjin` | 3167 | silent | GraphQL/MCP over DB for AI agents; agent-kit adjacency |
| `geohot/minikeyvalue` | 3153 | silent | toy distributed KV under 1000 lines; novelty |
| `shshemi/tabiew` | 3100 | silent | tabular data TUI viewer; CLI-systems spill |
| `man-group/arctic` | 3087 | silent | finance tick datastore; niche quant spill |
| `PomeloFoundation/Pomelo.EntityFrameworkCore.MySql` | 2974 | silent | EF Core MySQL provider; thin driver/provider |
| `dataplat/dbatools` | 2831 | silent | SQL Server DBA automation suite; Windows DBA mega toolkit |
| `aimeos/upscheme` | 2726 | silent | PHP schema helper; thin niche |
| `apache/parquet-format` | 2572 | silent | Parquet format spec thrift; specs-only |
| `supabase/cli` | 2411 | silent | Supabase platform CLI; BaaS/devops spill |
| `opencurve/curve` | 2389 | silent | CNCF distributed storage; devops/infra spill mega-adjacent |
| `gocraft/dbr` | 1848 | silent | thin Go database/sql helper additions |
| `Tencent/paxosstore` | 1714 | silent | WeChat paxos store; low external contrib surface |
| `dain/leveldb` | 1556 | silent | Java LevelDB port; quiet mirror-ish |
| `ilyakatz/data-migrate` | 1549 | silent | Rails data-migrate gem; framework glue |
| `tj/node-migrate` | 1544 | silent | abstract node migrate framework; thin/generic |
| `georgysavva/scany` | 1521 | silent | Go DB scan helper library; thin adjacency |
| `levelgraph/levelgraph` | 1520 | silent | JS graph-on-LevelDB; quiet niche |
| `basho/bitcask` | 1419 | silent | legacy Riak bitcask engine; quiet/unmaintained |
| `neo4jrb/activegraph` | 1405 | silent | Rails Neo4j OGM wrapper; framework glue |
| `couchbase/forestdb` | 1332 | silent | legacy ForestDB; quiet Couchbase engine |
| `ByteStorage/FlyDB` | 1232 | silent | small bitcask KV engine; thin novelty |
| `charles-001/dolphie` | 1195 | hard_ban | CLAUDE.md NO-AI phrase |
| `neo4j-contrib/neomodel` | 1089 | silent | Neo4j OGM library; thin mapper |

Notes: Prefer midband databases-storage leftover product homes (engines/KV/TSDB/vector/search/object-storage/backup/migrate/SQL-CLI/ORM/proxy). Disclosure: apache/lucene, EnterpriseDB/barman, vortex-data/vortex, borgmatic-collective/borgmatic, apache/iceberg-rust. Hard ban: charles-001/dolphie (NO-AI). Leave thin clients/drivers, framework glue (Rails/Laravel/Nest providers), GUIs/explain UIs, generic rsync backups, legacy quiet proxies/engines, agent/BaaS kits, Kafka-CDC spills, specs-only.

## Midband product deepen-3 (2026-09-14, +120 scored)

Account: `vulragrag-star` · Curated databases-storage midband TS/JS (1k–5k★) leftover SQL/ORM/migration/KV/Redis/Mongo/SQLite/backup/CDC/schema homes after databases-storage deepen-2 and other sector deepen-3s · Policy via `raw.githubusercontent.com` · **52** proceed / **68** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 117, 'disclosure': 3}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `jlongster/absurd-sql` | 4321 | silent | SQLite3 persisted in IndexedDB product | sqlite/vfs/path edge + js tests |
| `bee-queue/bee-queue` | 4036 | silent | Redis-backed job/task queue for Node.js | Redis queue/path edge + js tests |
| `joeferner/redis-commander` | 4003 | silent | Redis management GUI/CLI product written in Node | Redis admin/path edge + js tests |
| `timgit/pg-boss` | 3950 | silent | Postgres-backed job queue for Node | job queue/SQL path edge + js tests |
| `parse-community/parse-dashboard` | 3806 | silent | Dashboard for managing Parse Server (Mongo-backed BaaS) | Parse admin/path edge + js tests |
| `animir/node-rate-limiter-flexible` | 3585 | silent | Atomic counters/rate limits with Redis/Mongo/Memcached backends | storage counter/path edge + js tests |
| `vitaly-t/pg-promise` | 3553 | silent | PostgreSQL interface library for Node.js | pg query/path edge + js tests |
| `nosqlclient/nosqlclient` | 3468 | silent | Self-hosted MongoDB management GUI product | Mongo admin/path edge + js tests |
| `remult/remult` | 3211 | silent | Full-stack CRUD with SSOT TypeScript entities (ORM-ish) | entity CRUD/path edge + ts tests |
| `multiprocessio/datastation` | 2954 | silent | Desktop app to query/script/visualize data from many DBs | SQL query/path edge + ts tests |
| `sequelize/sequelize-auto` | 2923 | silent | Generate Sequelize models from live database schemas | schema reverse/path edge + js tests |
| `typegoose/mongodb-memory-server` | 2844 | silent | Spin up MongoDB server binaries for tests | Mongo binary/path edge + ts tests |
| `yy0931/sqlite3-editor` | 2755 | silent | SQLite3 editor / schema tooling product | SQLite schema/path edge + ts tests |
| `cars10/elasticvue` | 2746 | silent | Elasticsearch GUI (desktop/extension/docker) | ES admin/path edge + ts tests |
| `le0pard/pgtune` | 2740 | silent | Tune PostgreSQL config by hardware profile | pg config/path edge + js tests |
| `graphile/worker` | 2385 | silent | High-performance Node.js/PostgreSQL job queue | job queue/SQL path edge + ts tests |
| `oguimbal/pg-mem` | 2367 | silent | In-memory Postgres instance for unit tests | SQL engine/path edge + ts tests |
| `sequelize/umzug` | 2210 | silent | Framework-agnostic Node.js migration tool | migration/path edge + ts tests |
| `brody2consult/cordova-sqlite-storage` | 2161 | silent | Cordova/PhoneGap plugin for SQLite databases | SQLite plugin/path edge + js tests |
| `jaredwray/cacheable` | 2007 | silent | Multi-backend caching packages (Keyv-adjacent storage) | cache adapter/path edge + ts tests |
| `mike-marcacci/node-redlock` | 1981 | silent | Redis Redlock distributed lock implementation | Redis lock/path edge + js tests |
| `diego3g/rocketredis` | 1946 | silent | Redis GUI client product | Redis GUI/path edge + ts tests |
| `eveningkid/denodb` | 1919 | silent | Deno multi-DB ORM (MySQL/SQLite/Postgres/Mongo) | ORM mapping/path edge + ts tests |
| `mickhansen/graphql-sequelize` | 1883 | silent | GraphQL & Relay over MySQL/Postgres via Sequelize | Sequelize GraphQL/path edge + js tests |
| `smrchy/rsmq` | 1819 | silent | Redis Simple Message Queue | Redis queue/path edge + js tests |
| `variety/variety` | 1762 | silent | MongoDB schema analyzer CLI product | schema sample/path edge + js tests |
| `Portabase/portabase` | 1717 | silent | Multi-DB backup & restore CLI/product (Postgres/MySQL/MsSQL/SQLite) | backup/restore/path edge + tests |
| `thevahidal/soul` | 1684 | silent | Automatic SQLite RESTful + realtime API server | SQLite REST/path edge + js tests |
| `Level/level` | 1674 | silent | Universal abstract-level key-value database for Node/browsers | KV level/path edge + js tests |
| `Paxa/postbird` | 1638 | silent | Open-source PostgreSQL GUI client (macOS/Linux/Windows) | pg GUI query/path edge + js tests |
| `js-data/js-data` | 1613 | silent | Framework-agnostic data layer / ORM-ish resource library | data mapper/path edge + js tests |
| `ts-safeql/safeql` | 1567 | silent | Validate and auto-generate TypeScript types from raw SQL | SQL typecheck/path edge + ts tests |
| `jly8866/archer` | 1565 | silent | Automated SQL ops platform (Inception-based execute/audit) | SQL audit/path edge + js tests |
| `HeyPuter/kv.js` | 1530 | silent | Advanced in-memory key-value cache for JavaScript | KV cache/TTL path edge + js tests |
| `Meteor-Community-Packages/meteor-autoform` | 1427 | silent | Meteor AutoForm UI helpers over Mongo collections | Mongo form/path edge + js tests |
| `jawj/zapatos` | 1403 | silent | Zero-abstraction Postgres TypeScript SQL library (non-ORM) | SQL codegen/path edge + ts tests |
| `supabase/storage` | 1324 | silent | S3-compatible object storage with Postgres metadata | object storage/path edge + ts tests |
| `supabase/postgres-meta` | 1241 | silent | RESTful API for managing Postgres schemas/roles/tables | schema meta/path edge + ts tests |
| `adonisjs/lucid` | 1221 | silent | AdonisJS SQL ORM (Postgres/MySQL/SQLite/MSSQL) | ORM query/path edge + ts tests |
| `valtyr/prisma-kysely` | 1188 | silent | Generate Kysely types from Prisma schema | schema codegen/path edge + ts tests |
| `saintedlama/passport-local-mongoose` | 1164 | silent | Mongoose plugin for Passport-Local auth (Mongo user store) | Mongo auth plugin/path edge + js tests |
| `sergeyksv/tingodb` | 1157 | silent | Embedded Node.js database upward-compatible with MongoDB | embedded Mongo/path edge + js tests |
| `davidyaha/graphql-redis-subscriptions` | 1118 | silent | GraphQL subscriptions pub/sub via Redis | Redis pubsub/path edge + js tests |
| `neumino/thinky` | 1111 | silent | JavaScript ORM for RethinkDB | RethinkDB ORM/path edge + js tests |
| `stripe/sync-engine` | 1079 | silent | Stripe account → Postgres CDC/sync engine | CDC sync/path edge + ts tests |
| `bradleyboy/tuql` | 1076 | silent | Auto GraphQL server from SQLite database or SQL file | SQLite GraphQL/path edge + js tests |
| `mongoosastic/mongoosastic` | 1073 | silent | Index Mongoose models into Elasticsearch automatically | ES index sync/path edge + js tests |
| `biggora/caminte` | 1073 | silent | Cross-database ORM for NodeJS | ORM mapping/path edge + js tests |
| `nijikokun/generate-schema` | 1072 | silent | Convert JSON objects to MySQL/Mongoose/JSON Schema | schema infer/path edge + js tests |
| `seppevs/migrate-mongo` | 1030 | silent | MongoDB database migration tool for Node | migration/version/path edge + js tests |
| `Meteor-Community-Packages/meteor-collection2` | 1015 | silent | Mongo.Collection schema validation extension for Meteor | Mongo schema/path edge + js tests |
| `alfateam/orange-orm` | 1014 | silent | Node/TypeScript SQL ORM product | ORM mapping/query path edge + ts tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `ElasticHQ/elasticsearch-HQ` | 4993 | silent | Elasticsearch monitoring web dashboard; ops UI not product engine |
| `searchkit/searchkit` | 4854 | silent | React/Vue search UI for ES/Opensearch; frontend UI kit |
| `jamiewilson/form-to-google-sheets` | 4750 | silent | HTML form → Google Sheets; not DB/storage product |
| `supabase/supabase-js` | 4562 | silent | Supabase BaaS client SDK; thin client / platform spill |
| `tapexyz/tape` | 4454 | silent | media-sharing platform; not DB product |
| `meowtec/imgo` | 4417 | silent | image optimization desktop app; not DB |
| `graphif/project-graph` | 4413 | silent | node-based notes visualizer; not DB |
| `brocoders/nestjs-boilerplate` | 4387 | silent | NestJS boilerplate with TypeORM/Mongoose; starter template |
| `nestjsx/crud` | 4323 | silent | NestJS CRUD framework glue; not standalone DB product |
| `watsonbox/exportify` | 4225 | silent | Spotify playlist export; not DB |
| `open-legal-products/mike` | 4220 | silent | legal AI platform; agent/AI spill |
| `tmoroney/auto-subs` | 4205 | silent | DaVinci subtitle tool; not DB |
| `nilbuild/pennywise` | 3867 | silent | floating browser window app; not DB |
| `zhblue/hustoj` | 3792 | silent | online judge platform; MySQL-backed app not DB product |
| `apache/cordova-android` | 3788 | silent | Cordova Android platform; not DB |
| `LimeSurvey/LimeSurvey` | 3719 | silent | survey platform; not DB product |
| `chaskiq/chaskiq` | 3568 | silent | live chat/support platform; not DB |
| `marcj/deepkit` | 3544 | silent | modular TS framework mega; framework spill |
| `vantezzen/autoform` | 3493 | silent | auto form renderer UI; frontend spill |
| `antonycourtney/tad` | 3479 | silent | tabular data viewer desktop; viz UI not DB engine |
| `mlogclub/bbs-go` | 3475 | silent | community/forum app; not DB product |
| `jakearchibald/idb-keyval` | 3241 | silent | tiny IndexedDB keyval helper; thin library |
| `crawlab-team/artipub` | 3204 | silent | article publishing platform; not DB |
| `yourselfhosted/slash` | 3178 | silent | link sharing platform; not DB |
| `walinejs/waline` | 3116 | silent | comment system; app not DB product |
| `final-form/final-form` | 3045 | silent | form state library; frontend spill |
| `MacRimi/ProxMenux` | 2973 | silent | Proxmox VE toolkit; devops spill |
| `tj/connect-redis` | 2822 | silent | thin Redis session store for Connect; thin adapter |
| `socketio/socket.io-redis-adapter` | 2767 | silent | Socket.IO Redis adapter; networking spill |
| `disease-sh/API` | 2503 | silent | COVID/Influenza API; not DB product |
| `kentcdodds/kentcdodds.com` | 2494 | silent | personal website; not DB |
| `lana-k/sqliteviz` | 2354 | silent | browser SQL data visualisation UI; viz spill |
| `jquery/jquery-migrate` | 2091 | silent | jQuery migrate helper; not SQL migration |
| `lasting-yang/frida_dump` | 2071 | silent | Frida dump tool; RE/security spill |
| `Syngnat/GoNavi` | 1897 | silent | AI & MCP multi-data-source DB client; AI/MCP adjacency |
| `zws-im/zws` | 1848 | silent | URL shortener; not DB product |
| `wangweianger/zanePerfor` | 1799 | silent | frontend performance monitor; ops spill |
| `fbsamples/messenger-platform-samples` | 1750 | silent | Messenger samples; tutorial spill |
| `vfsfitvnm/frida-il2cpp-bridge` | 1738 | silent | Frida IL2CPP bridge; RE spill |
| `react-querybuilder/react-querybuilder` | 1735 | silent | React query-builder UI component; frontend kit |
| `tengge1/ShadowEditor` | 1706 | silent | 3D scene editor; Mongo-backed app not DB |
| `perftools/xhgui` | 1687 | silent | XHProf profiling UI; ops spill |
| `naomiaro/waveform-playlist` | 1677 | disclosure | CLAUDE.md AI mention; audio editor spill not DB product |
| `kuzzleio/kuzzle` | 1673 | silent | self-hostable backend platform; BaaS mega |
| `JackySoft/marsview` | 1650 | silent | low-code visual builder; not DB |
| `xuwujing/springBoot-study` | 1638 | silent | SpringBoot study tutorials; tutorial spill |
| `adminsyspro/proxcenter-ui` | 1619 | silent | Proxmox vCenter alternative UI; devops spill |
| `PegaProx/project-pegaprox` | 1569 | disclosure | CONTRIBUTING AI policy; Proxmox datacenter UI spill not DB |
| `garrylachman/ElectroCRUD` | 1549 | silent | Electron CRUD desktop over SQL; CRUD GUI app |
| `arpanghosh8453/open-dronelog` | 1525 | silent | drone log analyzer dashboard; not DB |
| `surmon-china/nodepress` | 1524 | silent | headless CMS API; CMS spill |
| `vueform/vueform` | 1510 | silent | Vue form framework; frontend spill |
| `wannabespace/conar` | 1443 | silent | AI-powered multi-DB tool; AI/agent adjacency |
| `event-driven-io/Pongo` | 1376 | disclosure | CONTRIBUTING/AGENTS/CLAUDE AI-assisted disclosure; Mongo-on-Postgres product otherwise leave for policy |
| `pierpo/react-archer` | 1343 | silent | draw arrows between React elements; UI kit |
| `openworkflowdev/openworkflow` | 1318 | silent | durable workflow framework; not DB product |
| `surrealdb/surrealist` | 1299 | silent | SurrealDB desktop management GUI; GUI spill |
| `emuell/restic-browser` | 1297 | silent | generic restic backup browser; not DB-specific |
| `nuxt-hub/core` | 1290 | silent | Nuxt Hub DB/KV/blob addon; framework glue |
| `digitallyinduced/thin-backend` | 1248 | silent | universal web app BaaS; platform spill |
| `layrjs/layr` | 1217 | silent | full-stack framework; framework spill |
| `simov/express-admin` | 1194 | silent | Express SQL admin panel; admin UI spill |
| `JKHeadley/rest-hapi` | 1181 | silent | RESTful API generator; scaffold spill |
| `mswjs/data` | 1064 | silent | data querying for JS tests/mocks; test kit |
| `vercel/nextjs-postgres-auth-starter` | 1053 | silent | Next.js + Drizzle starter template |
| `Rabithua/Rote` | 1037 | silent | personal note repository; notes app |
| `mohammed-bahumaish/prisma-editor` | 1036 | silent | Prisma schema visual editor UI; schema viz spill |
| `keonik/prisma-erd-generator` | 1033 | silent | Prisma ER diagram generator; diagram spill |

Notes: Prefer midband TS/JS databases-storage product homes (SQL/ORM with real SQL surface, migrations, Redis/KV stores, Mongo/SQLite/embedded DBs, backup/CDC/ETL CLIs, schema tools, object-storage with DB metadata). Leave ecommerce/CRUD apps, thin frontend dashboards, tutorials/starters, agent/AI kits, BaaS mega platforms, GUI-only admin panels, disclosure/hard_ban.

