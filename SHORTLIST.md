# Shortlist (100 / target 100)

Sector-balanced from proceed rows (not pure megastar sort). Primary weight: cli-systems + devops-build; elevated editors-devex after TS/JS DevEx scoring; security-crypto and databases-storage no longer token-represented.

Mix: cli-systems=18, editors-devex=14, devops-build=14, python-tooling=12, databases-storage=12, compilers-runtimes=10, security-crypto=10, networking-distributed=10

| Repo | Stars | Sector | Policy | Bug class hint |
|---|---|---|---|---|
| ohmyzsh/ohmyzsh | 189625 | cli-systems | disclosure | plugin path / quoting edge + shell tests |
| Genymobile/scrcpy | 149109 | cli-systems | silent | adb path / argv edge + C tests |
| microsoft/PowerToys | 138490 | cli-systems | silent | module path/config edge + C#/C++ tests |
| microsoft/TypeScript | 110981 | compilers-runtimes | disclosure | TS parse/check/path edge + tests - disclose AI assist |
| fatedier/frp | 109273 | cli-systems | silent | proxy config/path edge + Go tests |
| microsoft/terminal | 104843 | cli-systems | silent | settings JSON path / escape edge + C++ tests |
| neovim/neovim | 102213 | editors-devex | disclosure | path/option/Lua runtime edge + tests |
| nvbn/thefuck | 97772 | cli-systems | silent | command rule / argv edge + Python tests |
| oven-sh/bun | 95915 | compilers-runtimes | silent | runtime CLI/path/Node-compat edge + tests |
| nvm-sh/nvm | 95020 | cli-systems | silent | NODE_VERSION path / shell quoting + shell tests |
| zed-industries/zed | 89921 | editors-devex | disclosure | path/project-open or config parse + tests |
| astral-sh/uv | 89622 | python-tooling | disclosure | resolver/path/venv edge + Rust tests |
| junegunn/fzf | 82865 | cli-systems | silent | shell/argv/path + Go tests |
| jesseduffield/lazygit | 82122 | cli-systems | disclosure | git path/config edge + Go tests |
| coder/code-server | 79236 | editors-devex | silent | path/proxy/config edge + tests |
| apache/superset | 74677 | databases-storage | disclosure | SQL parse/Jinja/template edge with tests |
| Eugeny/tabby | 74387 | cli-systems | disclosure | SSH config / profile path edge + TS tests — check AI level box |
| pallets/flask | 73584 | python-tooling | silent | cli/path/config edge + tests |
| BurntSushi/ripgrep | 68078 | cli-systems | disclosure | path/glob/ignore edge + Rust tests |
| tw93/Mole | 66556 | cli-systems | silent | path / shell quoting edge + shell tests |
| prometheus/prometheus | 66005 | databases-storage | silent | PromQL/textparse quoting or tsdb path + table tests |
| scrapy/scrapy | 64240 | python-tooling | silent | URL/path/selector edge + tests |
| FuelLabs/sway | 61454 | compilers-runtimes | silent | parser/typecheck edge + tests |
| pi-hole/pi-hole | 60796 | cli-systems | silent | script path / gravity list edge + shell tests |
| sharkdp/bat | 60389 | cli-systems | silent | path/theme config edge + Rust tests |
| starship/starship | 59811 | cli-systems | disclosure | config.toml path/module edge + Rust tests |
| rclone/rclone | 59639 | cli-systems | disclosure | remote path/quoting edge + Go tests |
| FiloSottile/mkcert | 59563 | cli-systems | silent | CAROOT path / hostname edge + Go tests |
| PowerShell/PowerShell | 55292 | cli-systems | silent | path/quoting / parser edge + C# tests |
| mozilla/pdf.js | 53846 | editors-devex | silent | parser edge + unit tests |
| dockur/windows | 53197 | devops-build | silent | entrypoint shell path/quoting or env parse edge + shell tests |
| jesseduffield/lazydocker | 52756 | devops-build | silent | docker host path / compose project path edge + Go tests |
| prettier/prettier | 52240 | editors-devex | silent | parser/printer fixture edge + tests |
| astral-sh/ruff | 49545 | python-tooling | disclosure | lint rule/path/parse edge + fixtures |
| helix-editor/helix | 46159 | editors-devex | silent | config/LSP/path edge + Rust tests |
| pyenv/pyenv | 45085 | python-tooling | silent | shim/PATH/quoting edge + bats/shell tests |
| charmbracelet/bubbletea | 44874 | editors-devex | silent | Elm-arch msg/cmd edge + Go tests |
| parcel-bundler/parcel | 44024 | editors-devex | silent | bundle resolve/path/config edge + tests |
| psf/black | 41834 | python-tooling | silent | AST/parse edge + regression fixtures |
| lapce/lapce | 38833 | editors-devex | silent | config/plugin/path edge + Rust tests |
| lerna/lerna | 36055 | devops-build | silent | workspace/publish/path edge + tests |
| typicode/husky | 35309 | editors-devex | silent | hook path/config edge + tests |
| python-poetry/poetry | 34295 | python-tooling | silent | lockfile/path/env resolver edge + tests |
| tqdm/tqdm | 31330 | python-tooling | silent | progress format/path/iterable edge + py tests |
| micro-editor/micro | 29555 | editors-devex | silent | config/plugin/path edge + Go tests |
| postcss/postcss | 28974 | editors-devex | silent | CSS plugin/parse/path edge + tests |
| celery/celery | 28874 | python-tooling | silent | config/path/serializer edge + py tests |
| pydantic/pydantic | 28753 | python-tooling | silent | model parse/coerce/schema edge + py tests |
| eslint/eslint | 27499 | editors-devex | silent | lint rule/AST/path edge + tests |
| rollup/rollup | 26309 | editors-devex | silent | bundle resolve/path/plugin edge + tests |
| cookiecutter/cookiecutter | 25081 | python-tooling | silent | template path/hook quoting + tests |
| mkdocs/mkdocs | 22426 | python-tooling | silent | config/path/plugin edge + py tests |
| ahmetb/kubectx | 19978 | devops-build | silent | kubeconfig context/namespace path parse edge + Go/shell tests |
| google/gvisor | 19245 | devops-build | silent | OCI path / mount path edge + Go tests — Google CLA |
| bytecodealliance/wasmtime | 18607 | compilers-runtimes | disclosure | wasm/WASI/CLI path edge + tests |
| tinygo-org/tinygo | 17707 | compilers-runtimes | silent | target/linker/wasm export edge + tests |
| tursodatabase/libsql | 17208 | databases-storage | silent | SQL parser / savepoint edge + tests |
| argoproj/argo-workflows | 16959 | devops-build | disclosure | workflow template path / artifact path edge + Go tests — AI declaration |
| tikv/tikv | 16836 | databases-storage | silent | format/parse or path edge in compact-log-backup + tests |
| rust-lang/rust-analyzer | 16825 | compilers-runtimes | disclosure | analysis/IDE edge + tests — avoid E-easy |
| apple/foundationdb | 16677 | databases-storage | silent | simulation knob/path edge + tests |
| kubernetes/kops | 16670 | devops-build | silent | cluster YAML path / cloud flag edge + Go tests — open issue first |
| dagger/dagger | 16230 | devops-build | silent | module path / pipeline arg edge + Go tests — claim issue first |
| goreleaser/goreleaser | 16023 | devops-build | disclosure | config path/template quoting or archive name edge + Go tests — disclose AI |
| GoogleContainerTools/skaffold | 15888 | devops-build | silent | skaffold.yaml profile/path or artifact sync edge + Go tests |
| alibaba/zvec | 15847 | databases-storage | silent | vector index/path edge + C++ tests |
| dgraph-io/badger | 15758 | databases-storage | silent | SST path/corruption / compaction edge + tests |
| kubernetes-sigs/kind | 15478 | devops-build | silent | node image path / kubeadm config edge + Go tests |
| rust-lang/cargo | 15460 | devops-build | silent | path dep / lockfile / quoting edge + Rust tests — high bar |
| go-sql-driver/mysql | 15282 | databases-storage | silent | DSN/param/quoting/TINYINT edge + dsn_test |
| zitadel/zitadel | 14959 | security-crypto | disclosure | OIDC/login path or config parse edge + tests |
| benbjohnson/litestream | 14358 | databases-storage | disclosure | path/config DSN/replica path + go test |
| amir20/dozzle | 14300 | devops-build | silent | container filter / log path edge + Go tests |
| cert-manager/cert-manager | 14069 | security-crypto | silent | cert path/DNSName/CSR encode edge + unit tests |
| openresty/openresty | 14028 | compilers-runtimes | silent | build/path/LuaJIT packaging edge + tests |
| Jguer/yay | 13742 | devops-build | silent | PKGBUILD path/quoting or AUR RPC parse edge + Go tests |
| rook/rook | 13645 | databases-storage | disclosure | path/ceph volume mount + unit tests |
| gopherjs/gopherjs | 13183 | compilers-runtimes | silent | compiler/js-runtime edge + tests |
| drakkan/sftpgo | 12498 | databases-storage | silent | path sanitize / virtual folder edge + tests |
| manticoresoftware/manticoresearch | 11993 | databases-storage | silent | SQL/fulltext parse edge + tests |
| kubescape/kubescape | 11722 | security-crypto | silent | control/framework JSON parse or path edge + tests |
| linkerd/linkerd2 | 11487 | security-crypto | silent | CLI flag/path or identity name normalize + tests |
| dexidp/dex | 11083 | security-crypto | silent | OIDC connector config / redirect URI parse + tests |
| quay/clair | 11057 | security-crypto | silent | matcher/index path or purl parse edge + tests |
| foundry-rs/foundry | 10583 | compilers-runtimes | disclosure | CLI flag/path/tool edge + tests |
| golang-jwt/jwt | 9217 | security-crypto | silent | JWT claim/time/audience parse edge + table tests |
| wasm-bindgen/wasm-bindgen | 9145 | compilers-runtimes | silent | bindgen attribute/path parse edge + tests |
| smallstep/certificates | 8843 | security-crypto | silent | ACME/path/SAN parsing edge + go tests |
| aquasecurity/kube-bench | 8176 | security-crypto | silent | check YAML/config path edge + go tests |
| kyverno/kyverno | 8120 | security-crypto | disclosure | policy YAML parse / path match edge + unit tests |
| pomerium/pomerium | 4997 | networking-distributed | disclosure | redirect/URL path or policy rule edge + go tests — disclose AI |
| NLnetLabs/unbound | 4859 | networking-distributed | silent | conf/ACL/path or DNSSEC edge + tests |
| microsoft/msquic | 4775 | networking-distributed | silent | QUIC frame/path or API edge + tests |
| antoniomika/sish | 4712 | networking-distributed | silent | CLI flag/URL path or reverse tunnel edge + go tests |
| acassen/keepalived | 4680 | networking-distributed | silent | keepalived.conf path/VRRP edge + tests |
| openziti/zrok | 4668 | networking-distributed | silent | share/token/path CLI edge + go tests |
| ktr0731/evans | 4493 | networking-distributed | silent | CLI flag/proto descriptor/path edge + go tests |
| novnc/websockify | 4446 | networking-distributed | silent | WS URL/path or target dial edge + tests |
| openziti/ziti | 4381 | networking-distributed | silent | identity/config path or dial edge + go tests |
| networkupstools/nut | 4329 | networking-distributed | disclosure | driver/path or ups.conf quoting edge + tests — disclose |
