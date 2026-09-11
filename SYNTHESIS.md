# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2392**
- Proceed: **1639**
- Mid-band (1k–5k★) scored: **1206** (proceed 903)
- By sector: {'python-tooling': 353, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 283, 'compilers-runtimes': 287, 'databases-storage': 335, 'networking-distributed': 356, 'devops-build': 218}
- Policy mix: {'silent': 2094, 'hard_ban': 30, 'disclosure': 218, 'hostility_risk': 33, 'agentscan': 17}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **python-tooling product deepen-2** (+137 scored, 92 proceed) — loguru, faker, pybind11, fabric, Pillow, peewee, pdfplumber, gunicorn, pypdf, falcon, arrow, bottle, moto, asyncpg, auto-cpufreq, gitsome, a…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Python-tooling product deepen-2 scored packaging/CLI/HTTP/async/test/parser homes (gunicorn/hypercorn/falcon/bottle/waitress, pex/poethepoet/SCons, pytype/pyre/pydocstyle, Pillow/pypdf/lark/msgspec/yq/curl_cffi, asyncpg/beanie/tortoise/peewee, vcrpy/moto/testcontainers, pyinfra/fabric/jrnl/buku). Leave ML megas (sklearn/spacy/lightning/onnx), orchestration megas (airflow/prefect/dagster), Django circle, cloud SDKs, AgentScan aiomysql, sympy hostility_risk, furo theme. Disclosure: falcon/bottle/pypdf/loguru/twisted/strawberry/pyinfra/faker/SCons/microdot/socketio/matplotlib-policy-false-positive-overridden.
Prior DB/networking/compilers/editors/security deepens remain scored; continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3 leaves retained. Python deepen-2: matplotlib/faker/pyinfra scanner NO-AI hits overridden to disclosure; sympy overridden to hostility_risk; aio-libs/aiomysql AgentScan.

## Next
Next: devops-build product deepen-2 / midband fill, or SHORTLIST maintenance; rebuild SHORTLIST/SYNTHESIS already refreshed this pass. Contribution cadence remains separate from atlas literature work.
