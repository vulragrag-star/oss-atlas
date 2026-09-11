# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2493**
- Proceed: **1714**
- Mid-band (1k–5k★) scored: **1254** (proceed 936)
- By sector: {'python-tooling': 353, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 283, 'compilers-runtimes': 287, 'databases-storage': 335, 'networking-distributed': 356, 'devops-build': 319}
- Policy mix: {'silent': 2187, 'hard_ban': 31, 'disclosure': 225, 'hostility_risk': 33, 'agentscan': 17}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **devops-build product deepen-2** (+101 scored, 75 proceed) — colima, faas, slim, lima, cadvisor, kubespray, sealos, jib, distrobox, talos, kompose, keda, reviewdog, atlantis, autoscaler, linuxkit, kube…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
DevOps-build product deepen-2 scored container/runtime CLIs (colima/lima/distrobox/cri-o/slim/talos/incus/k3d), k8s installer/autoscaler/CLI plugins (kubespray/kompose/eksctl/karpenter/helmfile/kubefwd/kubectl-tree), IaC PR automation (atlantis/digger/driftctl/terracognita), Nix env/deploy (devenv/nh/colmena/deploy-rs/attic), serverless CLIs (openfaas/fn/nuclio/sam-cli/knative). Leave GUIs (awx/devtron/scope), provider plugins, PaaS megas (tsuru/kubefirst), hard_ban s6-overlay, agent workflows (gh-aw). Disclosure: gateway-api/kueue/sam-cli/digger/nh/apptainer.
Prior python/DB/networking/compilers/editors/security deepens remain scored; continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3 / Python deepen-2 leaves retained. DevOps deepen-2: kueue scanner hard_ban overridden to disclosure (K8s AI policy); s6-overlay disclosure overridden to hard_ban (no LLM contrib).

## Next
Next: SHORTLIST maintenance or midband fill in thinner slices; contribution cadence remains separate from atlas literature work.
