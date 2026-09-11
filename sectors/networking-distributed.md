# Sector survey: networking-distributed

Account: `vulragrag-star` · Input: `survey/raw/networking-distributed.jsonl` (165 repos, noisy ML/frontend dump) · Deep-sampled **75** networking-ish repos (policy files via `gh api` + GraphQL after core rate-limit) · Scored **82** lines (35 proceed / 47 leave) · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **protocol / CLI / path / quoting bugs with regression tests** (DNS, proxies, tunnels, HTTP/QUIC CLIs — not ML frameworks, not awesome-lists, not offensive tooling).

## Policy histogram (deep sample of 75)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 67 | No hard ban in common CONTRIBUTING/AI paths |
| disclosure | 4 | caddy, oauth2-proxy, zeek, rust-libp2p — disclose AI / human accountable |
| hostility_risk | 2 | telepresence AGENTS-for-AI; meshtastic copilot-instructions heavy |
| hard_ban | 2 | `qemu/qemu` (playbook QEMU-pattern), `GNOME/gimp` (no-genAI) |
| **agentscan** | 0 | No sample repo/owner on local adopters/blacklist |

Proceed: **35** · Leave: **47** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class (protocol/CLI/path/quoting + tests). Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `caddyserver/caddy` | 75563 | disclosure | HTTP/1-3 server; MUST disclose AI in CONTRIBUTING; Caddyfile path/matcher edges | Caddyfile matcher/path or reverse_proxy dial edge + tests — disclose model |
| `probelabs/goreplay` | 19319 | silent | HTTP traffic capture/replay CLI; middleware path | middleware path/HTTP rewrite edge + go tests |
| `slackhq/nebula` | 18310 | silent | Overlay mesh; cert/config path; active Slack maintainers | config/cert path or lighthouse DNS edge + go tests |
| `jpillora/chisel` | 16506 | silent | TCP/UDP tunnel over HTTP; CLI flags/path; small Go surface | CLI flag/URL path or reverse tunnel edge + tests |
| `hyperium/hyper` | 16313 | silent | Rust HTTP lib; URI/header parse with strong tests | URI/header parse edge + rust tests |
| `oauth2-proxy/oauth2-proxy` | 14929 | disclosure | Auth reverse proxy; CONTRIBUTING AI use allowed with human review + Assisted-by style | redirect/URL path or cookie domain edge + go tests |
| `coturn/coturn` | 14391 | silent | TURN/STUN server; conf path/realm edges | turnserver.conf path/realm edge + tests |
| `coredns/coredns` | 14299 | silent | CNCF DNS server; plugin/config/path edges; strong Go tests | DNS plugin config/path or zone parse edge + go tests |
| `rathole-org/rathole` | 14123 | silent | NAT reverse proxy CLI in Rust; TOML path/config | TOML config path/service name edge + cargo tests |
| `DNSCrypt/dnscrypt-proxy` | 13647 | silent | Encrypted DNS proxy CLI; source/stamp/path config surface | stamp/config path or resolver list quoting + tests |
| `fullstorydev/grpcurl` | 12803 | silent | gRPC curl CLI — proto/path/flag quoting is exact playbook class | CLI flag/path/proto descriptor edge + go tests |
| `cloudflare/quiche` | 11814 | silent | QUIC/HTTP3; AGENTS.md present (no ban); protocol framing edges | QUIC frame/path or qlog path edge + rust tests |
| `pymumu/smartdns` | 11299 | silent | Local DNS; conf path/domain rule edges | conf domain-rule/path edge + tests |
| `panjf2000/gnet` | 11245 | silent | Go event-driven net; addr/path edge cases | addr parse / event-loop edge + go tests |
| `shadowsocks/shadowsocks-rust` | 10848 | silent | SS proxy CLI; SIP003 plugin path/quoting classic | SIP003 plugin path/quoting or ACL path + cargo tests |
| `rofl0r/proxychains-ng` | 10680 | silent | Classic LD_PRELOAD proxy wrapper — conf path/quoting bugs are native class | proxychains.conf path/quoting or DNS resolve edge + tests |
| `flannel-io/flannel` | 9532 | silent | K8s network fabric; subnet/backend path config | backend config/path or subnet lease edge + go tests |
| `kubernetes-sigs/external-dns` | 9083 | silent | K8s→DNS sync; provider path/TXT ownership edges | DNS record ownership/TXT path edge + go tests |
| `miekg/dns` | 8769 | silent | Go DNS library; message/parse/EDNS edges with table tests | DNS message/EDNS parse or name compression edge + go tests |
| `esnet/iperf` | 8742 | silent | iperf3 CLI bandwidth tool; argv/path/JSON output edges | CLI argv/JSON report path edge + tests |
| `metallb/metallb` | 8343 | silent | K8s LB; IP/CIDR/config path | CIDR/config path edge + go tests |
| `yarrick/iodine` | 7962 | silent | DNS tunnel; encoding/path classic protocol tool | DNS encoding/password path edge + tests |
| `zeek/zeek` | 7945 | disclosure | NIDS framework; AI_POLICY requires disclosure + human understanding | script/path or protocol analyzer edge + tests — disclose AI |
| `twitchtv/twirp` | 7528 | silent | RPC over HTTP; path prefix/protoc plugin | HTTP path prefix / protoc plugin edge + go tests |
| `libcpr/cpr` | 7425 | silent | C++ Requests; URL/path/proxy options | URL/proxy option edge + tests |
| `davecheney/httpstat` | 7188 | silent | curl -v style CLI timing; URL/header path | URL/header timing edge + go tests |
| `tokio-rs/mio` | 7093 | silent | Metal I/O; interest/path fd edges | mio interest/poll edge + rust tests |
| `erebe/wstunnel` | 7030 | silent | WS/HTTP2 tunnel CLI; URL/path/flag surface | tunnel URL/path or TLS SNI edge + rust tests |
| `zmap/zmap` | 6371 | silent | Fast network scanner; conf/blacklist path | blacklist/conf path edge + tests |
| `JoeDog/siege` | 6217 | silent | HTTP load tester CLI; URL file path quoting | URL-file path/quoting edge + tests |
| `emmett-framework/granian` | 5618 | silent | Rust HTTP server for Python; path/ASGI edges | mount path / worker CLI edge + tests |
| `libp2p/rust-libp2p` | 5612 | disclosure | Ask AI disclosure; keep AI text brief; multiaddr/path edges | multiaddr/protocol parse edge + rust tests — disclose |
| `tonarino/innernet` | 5544 | silent | WireGuard private net; invite/CIDR/path CLI | invite/CIDR/path CLI edge + rust tests |
| `3proxy/3proxy` | 5453 | silent | Tiny proxy server; ACL/path/config | ACL/config path edge + tests |
| `yrutschle/sslh` | 5111 | silent | Protocol multiplexer (SSH+HTTPS share port); probe/path config | protocol probe/config path edge + tests |

### Tier notes

**Best first homes (small testable protocol/CLI/path hunks):**

1. `fullstorydev/grpcurl` — gRPC curl CLI; flag/proto/path edges; silent policy; classic outsider-testable surface.
2. `coredns/coredns` / `DNSCrypt/dnscrypt-proxy` / `miekg/dns` / `pymumu/smartdns` — DNS parse/config/path cluster; strong Go test culture on coredns/miekg.
3. `jpillora/chisel` / `rathole-org/rathole` / `erebe/wstunnel` / `tonarino/innernet` — tunnel/overlay CLIs; TOML/flag/URL path edges.
4. `rofl0r/proxychains-ng` / `shadowsocks/shadowsocks-rust` / `3proxy/3proxy` — proxy conf path/quoting (SIP003 plugin path is a known class).
5. `yrutschle/sslh` / `esnet/iperf` / `davecheney/httpstat` / `JoeDog/siege` — small C/Go CLIs; argv/URL-file quoting.
6. `oauth2-proxy/oauth2-proxy` — AI allowed with human review; redirect/URL path edges.
7. `caddyserver/caddy` — high impact; **must disclose** AI per CONTRIBUTING; Caddyfile matcher/path edges.
8. `cloudflare/quiche` — QUIC framing; AGENTS.md present but no ban found.

**Proceed with process friction:**

- `caddyserver/caddy` — disclose agent/model; verify no plagiarized/incompatibly-licensed AI output.
- `zeek/zeek` — AI_POLICY: disclose tool + extent; human must fully understand code without AI aid.
- `libp2p/rust-libp2p` — disclose AI; keep generated text brief for reviewers.
- `kubernetes-sigs/external-dns` / `flannel-io/flannel` / `metallb/metallb` — K8s SIG/CNCF norms; prefer small tested config edges over feature PRs.
- `slackhq/nebula` / `coturn/coturn` — production networking; match existing test layout tightly.

**Clusters to farm leftovers (one home at a time):**

| Cluster | Repos | Hunk shape |
|---|---|---|
| DNS | coredns, dnscrypt-proxy, miekg/dns, smartdns, external-dns, iodine | zone/stamp/EDNS/config path |
| Tunnels | chisel, rathole, wstunnel, innernet, nebula | CLI flag / TOML / CIDR / URL |
| Proxies | proxychains-ng, shadowsocks-rust, 3proxy, oauth2-proxy | conf quoting / SIP003 / redirect URL |
| HTTP/QUIC CLI | grpcurl, httpstat, siege, iperf, goreplay, quiche, hyper | argv / URI / proto path |
| K8s net | flannel, metallb, external-dns | CIDR / record ownership / backend path |

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `vuejs/vue` | 212070 | silent | Wrong-class noise in raw dump (frontend) |
| `tensorflow/tensorflow` | 199338 | silent | Wrong-class noise (ML framework) |
| `DigitalPlatDev/FreeDomain` | 198101 | silent | Docs/domain marketing — not product networking code |
| `pytorch/pytorch` | 102851 | silent | Wrong-class noise (ML framework) |
| `gin-gonic/gin` | 89187 | silent | HTTP framework — weak CLI/path/quoting product surface for this sector pass |
| `binhnguyennus/awesome-scalability` | 73795 | silent | Awesome-list — not product |
| `bettercap/bettercap` | 19944 | silent | Offensive network Swiss-army — security-sector / ethics leave for this account |
| `jeessy2/ddns-go` | 17317 | silent | DDNS web panel — mostly provider glue; weak protocol hunk |
| `snail007/goproxy` | 17132 | silent | Commercial-leaning proxy product; outsider merge culture unclear |
| `julienschmidt/httprouter` | 17129 | silent | Router library only — not protocol/CLI product |
| `zerotier/ZeroTierOne` | 17083 | silent | Commercial overlay core; CLA/process friction likely |
| `qemu/qemu` | 13695 | hard_ban | Playbook QEMU-pattern: live docs DECLINE AI-derived patches |
| `safing/portmaster` | 13686 | silent | Desktop privacy app — large UI surface; weak hunk class |
| `hibiken/asynq` | 13684 | silent | Task queue — distributed but not networking protocol/CLI class |
| `alibaba/tengine` | 13351 | silent | Nginx fork — heavy C; prefer smaller CLI/DNS homes first |
| `capnproto/capnproto` | 13173 | silent | RPC/serialization — possible but C++ high bar; defer |
| `twitter/twemproxy` | 12337 | silent | Mostly dormant redis/memcache proxy |
| `vanhauser-thc/thc-hydra` | 12246 | silent | Password cracker — do not contribute from this account |
| `kubeshark/kubeshark` | 12072 | silent | eBPF k8s observability — heavy product; not path/quoting CLI first home |
| `BishopFox/sliver` | 11796 | silent | Adversary emulation — leave |
| `openresty/lua-nginx-module` | 11789 | silent | Nginx C module — satellite-ish to OpenResty; high bar |
| `h2o/h2o` | 11541 | silent | HTTP server C — high bar; prefer caddy/quiche first |
| `zeromq/libzmq` | 10989 | silent | ZMTP engine — C++ high bar; defer |
| `git-bug/git-bug` | 10023 | silent | Distributed bug tracker — wrong sector class |
| `ValveSoftware/GameNetworkingSockets` | 9894 | silent | Game UDP stack — Valve CLA / game-net class |
| `klzgrad/naiveproxy` | 9437 | silent | Chromium-tied circumvention proxy — awkward contrib |
| `cadence-workflow/cadence` | 9433 | silent | Workflow orchestration — distributed but not protocol/CLI/path class |
| `redpanda-data/connect` | 8740 | silent | Stream connectors — AGENTS soft AI mention; not protocol CLI home |
| `roadrunner-server/roadrunner` | 8505 | silent | PHP app server — weak networking protocol/CLI fit |
| `cyfdecyf/cow` | 8411 | silent | Stale HTTP proxy; low maintenance signal |
| `p4gefau1t/trojan-go` | 8387 | silent | Circumvention proxy; archived-ish contrib risk / wrong home |
| `facebook/proxygen` | 8379 | silent | Meta C++ HTTP stack — CLA/high bar; not first home |
| `meshtastic/firmware` | 8270 | hostility_risk | Heavy agent/copilot-instructions; firmware not CLI/protocol-path home |
| `lightningnetwork/lnd` | 8188 | silent | Lightning daemon — crypto/finance process; leave this pass |
| `antirez/disque` | 8075 | silent | Archived-ish message broker; low velocity |
| `haad/proxychains` | 7954 | silent | Legacy proxychains — prefer proxychains-ng mainline |
| `telepresenceio/telepresence` | 7293 | hostility_risk | AGENTS.md aimed at AI assistants; process unknown — skip this pass |
| `TelegramMessenger/MTProxy` | 6916 | silent | Telegram MTProxy — opaque contrib / weak test culture signal |
| `libp2p/go-libp2p` | 6880 | silent | Prefer rust-libp2p (clearer AI disclosure) or smaller CLI first |
| `elazarl/goproxy` | 6755 | silent | Library-only HTTP proxy — prefer product CLIs |
| `beanstalkd/beanstalkd` | 6701 | silent | Work queue — not protocol/CLI networking home |
| `OISF/suricata` | 6616 | silent | IDS — heavy C; prefer zeek if NIDS; not first home |
| `GNOME/gimp` | 6400 | hard_ban | GIMP strict no-genAI (policy-map Loupe-family) |
| `baidu/dperf` | 5603 | silent | DPDK load tester — specialized hardware; weak outsider path |
| `cjdelisle/cjdns` | 5409 | silent | Encrypted IPv6 mesh — niche; contrib culture unclear |
| `fluvio-community/fluvio` | 5249 | silent | Stream processing — closer to data; leave networking pass |
| `http-rs/tide` | 5094 | silent | Async HTTP framework; lower activity / weak CLI surface |

### Leave themes

- **Hard ban:** `qemu/qemu` (DECLINE AI-derived), `GNOME/gimp` (no-genAI).
- **Wrong-class raw noise:** vue/tensorflow/pytorch/FreeDomain/awesome-scalability — ignore for this sector.
- **Offensive / circumvention homes:** bettercap, hydra, sliver, trojan-go, MTProxy, naiveproxy — do not farm from this account.
- **Framework-only:** gin, httprouter, tide, elazarl/goproxy — prefer product CLIs.
- **Heavy C++/commercial:** tengine, proxygen, ZeroTier, libzmq, capnproto — defer until a home-repo exists elsewhere.
- **Distributed-but-not-net-CLI:** cadence, asynq, beanstalkd, disque, fluvio, lnd, git-bug.

## Method notes

- Policy scan: common CONTRIBUTING/AI/AGENTS/PR-template paths; workflow dir names for AgentScan; GraphQL batch after REST core hit 0/5000.
- Fit filter: protocol/CLI/path/quoting with tests (playbook METHOD.md quoting/subprocess/path class).
- Predecessor closed queues / AgentScan circle: none hit in this sample.
- Before any future PR: `python scripts/repo-gate.py` + `agentscan-check.py --refresh` + `hostility-scan.py`; sample 10 merged outsider PRs for voice.

_Survey finished 2026-09-08 (UTC+8 afternoon)._

## Product deepen (≥5k★ subset) (2026-09-11, +94 scored)

Account: `vulragrag-star` · Curated compiler/runtime/Wasm/language product homes still missing after midband + famous-CLI passes · Policy via `raw.githubusercontent.com` · **61** proceed / **33** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 78, 'disclosure': 11, 'hard_ban': 4, 'agentscan': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `Kong/kong` | 44123 | silent | Kong API gateway; route/plugin/path edges | route/plugin/path edge + tests |
| `juanfont/headscale` | 43745 | disclosure | Tailscale-compatible control plane — disclose AI | ACL/config/path or DERP edge + go tests — disclose AI |
| `curl/curl` | 42829 | silent | curl CLI; URL/path/quoting/protocol classic playbook surface | URL/path/quoting or transfer edge + tests |
| `XTLS/Xray-core` | 41519 | silent | VLESS/XTLS core; inbound/path/config edges | inbound/path/config edge + go tests |
| `SagerNet/sing-box` | 37853 | silent | Universal proxy platform; rule/path/config edges | rule/config path or outbound edge + go tests |
| `v2fly/v2ray-core` | 34569 | silent | V2Ray core; protocol/path/config edges | protocol/config path edge + go tests |
| `MetaCubeX/mihomo` | 33993 | silent | Clash Meta core; rule/path/config edges | rule/config path edge + tests |
| `grafana/k6` | 31440 | silent | Load testing CLI/JS; script/path/HTTP edges | script/path or HTTP edge + go tests |
| `hashicorp/consul` | 30063 | silent | Consul service mesh control; ACL/path/config | ACL/config path or DNS edge + go tests |
| `locustio/locust` | 28142 | silent | Python load tester; task/path/HTTP edges | task/path/HTTP edge + tests |
| `nsqio/nsq` | 25777 | silent | Realtime distributed messaging; topic/path edges | topic/channel/path edge + go tests |
| `tsenart/vegeta` | 25185 | silent | HTTP load testing CLI; target/path/quoting edges | target URL/path quoting edge + go tests |
| `gorilla/websocket` | 24866 | silent | Go WebSocket lib; upgrade/path edges | upgrade/path/frame edge + go tests |
| `valyala/fasthttp` | 23469 | silent | Fast HTTP server/client; header/path parse edges | header/path/URI parse edge + go tests |
| `fosrl/pangolin` | 22706 | disclosure | Identity-aware proxy tunnel — disclose AI in PR | auth/proxy path edge + tests — disclose AI |
| `HyNetworks/hysteria` | 22465 | silent | QUIC proxy/tunnel CLI; config/path/protocol edges | config/QUIC path or auth edge + go tests |
| `livekit/livekit` | 20843 | silent | Realtime WebRTC SFU; room/path/config edges | room/path/config edge + go tests |
| `nats-io/nats-server` | 20693 | disclosure | NATS server — disclose AI assist | subject/config/path edge + go tests — disclose AI |
| `rakyll/hey` | 20258 | silent | HTTP load CLI; URL/header/path edges | URL/header/path edge + go tests |
| `bluenviron/mediamtx` | 20100 | silent | Media-over-QUIC/RTSP/WebRTC server; path/config | path/config or protocol edge + go tests |
| `grpc-ecosystem/grpc-gateway` | 20002 | silent | gRPC↔JSON gateway; HTTP path/proto mapping edges | HTTP path/proto mapping edge + go tests |
| `apache/brpc` | 17601 | silent | bRPC framework; protocol/path edges | protocol/path edge + tests |
| `joewalnes/websocketd` | 17464 | silent | WebSocket↔stdio bridge CLI; path/argv edges | path/argv quoting edge + go tests |
| `ipfs/kubo` | 17131 | silent | IPFS Kubo node; path/CID/config edges | CID/path/config edge + go tests |
| `apache/apisix` | 17110 | silent | Apache APISIX gateway; route/plugin/path edges | route/plugin path edge + tests |
| `skywind3000/kcp` | 16903 | silent | KCP ARQ protocol; segment/path edges | segment/conv path edge + tests |
| `pion/webrtc` | 16773 | silent | Pure Go WebRTC; SDP/ICE/path edges | SDP/ICE/path edge + go tests |
| `emqx/emqx` | 16705 | silent | EMQX MQTT broker; rule/path/config edges | rule/config path edge + tests |
| `shadowsocks/shadowsocks-c` | 16177 | silent | Shadowsocks C impl; plugin/path/ACL edges | plugin path/ACL edge + tests |
| `passteque/gluetun` | 15464 | silent | VPN client container CLI; provider/path config | provider/config path edge + go tests |
| `txthinking/brook` | 15175 | silent | Programmable network tool CLI; dial/path edges | CLI dial/path or socks edge + go tests |
| `sogou/workflow` | 14421 | silent | C++ async networking framework; URI/path edges | URI/path/task edge + tests |
| `AlexxIT/go2rtc` | 14157 | silent | Camera streaming; source/path/config edges | source/path/config edge + go tests |
| `EasyTier/EasyTier` | 13592 | silent | Decentralized mesh VPN; peer/path/config edges | peer/config path edge + rust tests |
| `SoftEtherVPN/SoftEtherVPN` | 13543 | silent | Multi-protocol VPN; config/path edges | config/path or protocol edge + tests |
| `cesanta/mongoose` | 13038 | silent | Embedded TCP/HTTP/MQTT stack; path/URI edges | URI/path or MQTT edge + tests |
| `n0-computer/iroh` | 12481 | silent | QUIC+NAT traversal lib; dial-key/path edges | dial-key/QUIC path edge + rust tests |
| `libevent/libevent` | 11949 | silent | Evented net lib; bufferevent/path edges | bufferevent/path edge + tests |
| `seanmonstar/reqwest` | 11815 | silent | Rust HTTP client; URL/proxy/redirect edges | URL/proxy/redirect edge + rust tests |
| `gravitl/netmaker` | 11779 | silent | WireGuard mesh control plane; node/CIDR/path edges | node/CIDR/config path edge + go tests |
| `quic-go/quic-go` | 11765 | silent | QUIC protocol lib; frame/path/config edges with tests | QUIC frame/path or dial edge + go tests |
| `bufbuild/buf` | 11427 | silent | Protobuf/buf CLI; path/module/config edges | proto path/module config edge + go tests |
| `eclipse-mosquitto/mosquitto` | 11186 | silent | MQTT broker; conf/path/ACL edges | conf/ACL path edge + tests |
| `apache/thrift` | 10957 | disclosure | Apache Thrift — disclose AI trailer | IDL/path/transport edge + tests — disclose AI |
| `hashicorp/raft` | 9120 | disclosure | Raft consensus lib — disclose AI | log/path or snapshot edge + go tests — disclose AI |
| `smallnest/rpcx` | 8316 | silent | Go RPCX; service/path/codec edges | service/path/codec edge + go tests |
| `cloudwego/kitex` | 8035 | silent | RPC framework; IDL/path/codec edges | IDL/path/codec edge + go tests |
| `go-gost/gost` | 7459 | silent | GOST tunnel/proxy CLI; chain/path/config edges | chain/config path edge + go tests |
| `cloudwego/hertz` | 7361 | silent | HTTP framework; route/path/middleware edges | route/path middleware edge + go tests |
| `versatica/mediasoup` | 7360 | silent | SFU WebRTC; transport/path edges | transport/path edge + tests |
| `projectcalico/calico` | 7351 | disclosure | Calico CNI/network — disclose AI policy | IPAM/policy path edge + go tests — disclose AI |
| `cloudflare/boringtun` | 7190 | silent | Userspace WireGuard; config/path edges | WG config/path or key edge + rust tests |
| `google/gopacket` | 6795 | silent | Packet decode framework; layer/path edges | layer decode/path edge + go tests |
| `nats-io/nats.go` | 6745 | silent | NATS Go client; subject/path edges | subject/path edge + go tests |
| `gobwas/ws` | 6466 | silent | Go WebSocket; upgrade/path edges | upgrade/path edge + go tests |
| `containernetworking/cni` | 6113 | silent | CNI spec/libs; conf/path edges | CNI conf/path edge + go tests |
| `hashicorp/serf` | 6072 | disclosure | Serf gossip membership — disclose AI | member/event path edge + go tests — disclose AI |
| `coder/websocket` | 5460 | silent | Minimal WebSocket lib; dial/path edges | dial/path/frame edge + go tests |
| `yggdrasil-network/yggdrasil-go` | 5405 | silent | Overlay mesh; admin/API/path edges | admin socket/path or peer edge + go tests |
| `quinn-rs/quinn` | 5254 | disclosure | QUIC in Rust — disclose AI per CONTRIBUTING | QUIC stream/path edge + rust tests — disclose AI |
| `nginx/kubernetes-ingress` | 5077 | silent | NGINX Ingress Controller; annotation/path edges | annotation/path config edge + go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `2dust/v2rayN` | 115884 | silent | Windows GUI client for Xray — leave GUI class |
| `axios/axios` | 109224 | silent | JS HTTP client in web ecosystem — weak protocol edge; leave |
| `etcd-io/etcd` | 52244 | silent | etcd mega; Kubernetes control-plane process — leave |
| `lysine-dev/okhttp` | 47065 | silent | JVM HTTP client (ex-square) — client-only leave |
| `grpc/grpc` | 45303 | hard_ban | CONTRIBUTING NO-AI — hard leave |
| `gofiber/fiber` | 40143 | silent | Go web framework — leave web-app class |
| `Kong/insomnia` | 40003 | silent | API client GUI — leave; prefer Kong gateway product |
| `netty/netty` | 35048 | silent | Netty mega framework — leave |
| `apache/kafka` | 33701 | disclosure | Kafka mega; process-heavy — leave for outsider agent cadence |
| `tokio-rs/tokio` | 33118 | silent | Tokio runtime mega — leave; prefer protocol satellites |
| `labstack/echo` | 32706 | silent | Go web framework — leave web-app class |
| `facebook/folly` | 30535 | silent | Folly C++ utility mega — leave |
| `jitsi/jitsi-meet` | 29903 | silent | Jitsi Meet web/app frontend — leave GUI; prefer videobridge |
| `libuv/libuv` | 27165 | silent | libuv runtime mega — leave |
| `tokio-rs/axum` | 27080 | silent | Rust web framework — leave web-app class |
| `actix/actix-web` | 24822 | silent | Rust web framework — leave web-app class |
| `grpc/grpc-go` | 23052 | hard_ban | CONTRIBUTING NO-AI — hard leave |
| `apache/rocketmq` | 22588 | silent | RocketMQ mega — leave |
| `ZLMediaKit/ZLMediaKit` | 17519 | silent | Media server mega; prefer smaller SFU/CLI homes |
| `Qv2ray/Qv2ray` | 16906 | silent | Cross-platform V2Ray GUI — leave GUI |
| `avwo/whistle` | 15686 | silent | HTTP debug proxy with web UI — leave GUI/debug surface |
| `v2rayA/v2rayA` | 15550 | silent | Web GUI client for Project V — leave GUI |
| `apache/pulsar` | 15328 | disclosure | Pulsar messaging mega — leave |
| `owasp-amass/amass` | 15142 | silent | Attack-surface mapping — leave recon/offensive |
| `amnezia-vpn/amnezia-client` | 14960 | silent | VPN desktop/mobile client GUI — leave |
| `OJ/gobuster` | 14106 | silent | Dir/DNS busting tool — leave offensive class |
| `rabbitmq/rabbitmq-server` | 13849 | hard_ban | AGENTS.md NO-AI — hard leave |
| `grpc/grpc-rust` | 12467 | hard_ban | CONTRIBUTING NO-AI (tonic home) — hard leave |
| `wireshark/wireshark` | 9859 | disclosure | Wireshark mega; Gerrit/process-heavy — leave for outsider cadence |
| `apache/jmeter` | 9528 | silent | JMeter Java GUI load mega — leave; prefer vegeta/hey/k6 |
| `ntop/ntopng` | 8149 | silent | ntopng monitoring UI product — leave UI/ops mega |
| `nodejs/undici` | 7693 | agentscan | AgentScan adopter — leave Node circle |
| `projectdiscovery/naabu` | 6238 | silent | Port scanner — leave offensive/recon class |

Notes: Prefer DNS/lookup CLIs, HTTP/QUIC/gRPC protocol+CLI (curl/trurl/quic-go/fasthttp/reqwest/buf/grpc-gateway/quinn/h2), tunnels/overlays (headscale/hysteria/sing-box/xray/v2ray/brook/netmaker/EasyTier/iroh/gluetun/mihomo/gost), reverse proxies/ingress (apisix/kong/contour/envoy-gateway), WebRTC/SFU (pion/mediasoup/livekit/mediamtx/go2rtc), load CLIs (vegeta/hey/k6), messaging brokers (nats/mosquitto/emqx/nsq), K8s CNI (calico/cni/multus/kube-vip/antrea), BGP (gobgp/exabgp), Consul/serf/raft. Disclosure: headscale/nats/calico/quinn/pangolin/thrift/hashicorp serf/memberlist/raft. Leave grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici, GUIs (v2rayN/v2rayA/Qv2ray/insomnia), offensive scanners, web frameworks, kafka/etcd megas, wireshark process.

