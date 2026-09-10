# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1702**
- Proceed: **1183**
- Mid-band (1k–5k★) scored: **1040** (proceed 777)
- By sector: {'python-tooling': 216, 'security-crypto': 166, 'cli-systems': 290, 'editors-devex': 175, 'compilers-runtimes': 184, 'databases-storage': 217, 'networking-distributed': 236, 'devops-build': 218}
- Policy mix: {'silent': 1522, 'hard_ban': 19, 'disclosure': 127, 'hostility_risk': 29, 'agentscan': 5}
- Language mix (universe top): {'Go': 2520, 'C++': 2413, 'Python': 2287, 'TypeScript': 2252, 'Rust': 2133, 'C': 2093, 'JavaScript': 2009, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **devops-build product deepen** (+66 scored, 56 proceed) — moby, act, ansible, container, compose, firecracker, k3s, podman, dokku, minikube, helm, opentofu, harbor, vcpkg, vagrant, bazel, pulumi, argo-cd, containerd, g…
- Mid-band language fill: TypeScript **2252**, JavaScript **2009**, Zig **51**, Rust **2133**, Go **2520** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
DevOps-build product deepen scored container/runtime/IaC/GitOps/build CLIs (moby, podman, helm, opentofu, pulumi, argo-cd, buildkit, kamal, act, vcpkg, bazel, gradle, flyctl). Leave PaaS GUIs (coolify/dokploy/portainer/dockge/caprover), jenkins mega, rancher platform UI, actions/runner, and cloud-hypervisor (hostility_risk). Disclosure/careful: ansible, podman AGENTS, pulumi/crossplane/gradle AI_POLICY, k3s/containerd/runc/kata/CMake.
Famous shells/editors gap fill remains scored; full terminal emulators stay leave. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed.

## Next
Next thin tails: security-crypto or editors-devex midband, or rebuild SHORTLIST/SYNTHESIS after more scores. Contribution cadence remains separate from atlas literature work.
