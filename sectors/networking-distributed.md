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
