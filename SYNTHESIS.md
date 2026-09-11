# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2255**
- Proceed: **1547**
- Mid-band (1k–5k★) scored: **1140** (proceed 849)
- By sector: {'python-tooling': 216, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 283, 'compilers-runtimes': 287, 'databases-storage': 335, 'networking-distributed': 356, 'devops-build': 218}
- Policy mix: {'silent': 1975, 'hard_ban': 30, 'disclosure': 202, 'hostility_risk': 32, 'agentscan': 16}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **databases-storage product deepen-3** (+118 scored, 78 proceed) — redis, meilisearch, ClickHouse, orm, milvus, duckdb, tidb, gorm, leveldb, typeorm, restic, drizzle-orm, seaweedfs, qdrant, surrealdb, rocksd…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Databases-storage product deepen-3 scored engines/modules/SQL CLIs/ORMs/search/TSDB/vector/object-storage/backup/migrate (redis/valkey/dragonfly, ClickHouse/duckdb/tidb/vitess, meilisearch/typesense/qdrant/milvus, loki/mimir/tempo/thanos/VictoriaMetrics, restic/borg/kopia/gh-ost, goose/flyway/atlas/sqlc, rocksdb/leveldb/pebble/juicefs/seaweedfs, arrow/iceberg/delta). Leave PostgREST Gentoo-ban, polars agent-forbidden, sqlfluff AgentScan, sqlglot hostility, client-only drivers, compression codecs, Spark/Flink/Hadoop/Ceph/Postgres megas. Disclosure: meilisearch/ClickHouse/duckdb/qdrant/turso/timescale/arrow/cassandra/iceberg/quickwit/diesel/borg/databend/prisma/milvus/tempo.
Networking + compilers + editors + security product deepens remain scored; full terminal emulators stay leave. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3: PostgREST Gentoo ban; polars agents-forbidden; databend/numpy scanner NO-AI hits were false positives (disclosure/HITL); redis/go-redis "No AI-attribution trailer" overridden to silent (still leave as client-only).

## Next
Next: SHORTLIST maintenance / remaining thin sectors (python-tooling/devops-build) or midband fill; rebuild SHORTLIST/SYNTHESIS already refreshed this pass. Contribution cadence remains separate from atlas literature work.
