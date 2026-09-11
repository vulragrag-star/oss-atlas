# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2137**
- Proceed: **1469**
- Mid-band (1k–5k★) scored: **1140** (proceed 849)
- By sector: {'python-tooling': 216, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 283, 'compilers-runtimes': 287, 'databases-storage': 217, 'networking-distributed': 356, 'devops-build': 218}
- Policy mix: {'silent': 1881, 'hard_ban': 29, 'disclosure': 182, 'hostility_risk': 30, 'agentscan': 15}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **networking-distributed product deepen** (+120 scored, 83 proceed) — kong, headscale, curl, Xray-core, sing-box, v2ray-core, mihomo, k6, consul, locust, nsq, vegeta, websocket, fasthttp, pangolin, hysteria, li…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Networking-distributed product deepen scored DNS/lookup CLIs, HTTP/QUIC/gRPC protocol+CLI (curl/trurl/quic-go/fasthttp/reqwest/buf/grpc-gateway/quinn), tunnels/overlays (headscale/hysteria/sing-box/xray/v2ray/brook/netmaker/EasyTier/iroh/gluetun/mihomo), reverse proxies/ingress (apisix/kong/contour/envoy-gateway), WebRTC/SFU (pion/mediasoup/livekit/mediamtx), load CLIs (vegeta/hey/k6), messaging (nats/mosquitto/emqx/nsq), K8s CNI (calico/cni/multus/kube-vip), BGP (gobgp), Consul/serf/raft. Leave grpc/rabbitmq/kube-router NO-AI, AgentScan undici, GUIs (v2rayN/insomnia), offensive scanners, web frameworks, kafka/etcd/wireshark process megas. Disclosure: headscale/nats/calico/quinn/pangolin/thrift/hashicorp serf/memberlist/raft.
Compilers-runtimes + editors-devex + security-crypto product deepens remain scored; full terminal emulators stay leave. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Note: certbot/authentik scanner NO-AI hits were false positives (AI allowed with disclosure/HITL); Zettlr CoC-only AI mention overridden to silent. Networking deepen hard leaves: grpc/grpc + grpc-go + grpc-rust NO-AI, rabbitmq-server NO-AI, kube-router NO-AI; AgentScan undici.

## Next
Next: SHORTLIST maintenance / remaining thin sectors or midband fill; rebuild SHORTLIST/SYNTHESIS already refreshed this pass. Contribution cadence remains separate from atlas literature work.
