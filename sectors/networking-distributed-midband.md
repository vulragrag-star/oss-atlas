# Sector survey: networking-distributed (mid-band 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/networking-distributed-midband.jsonl` (486 repos) · Deep-sampled **155** networking-ish repos (policy via `raw.githubusercontent.com` + `gh api` workflows) · Scored **154** lines (**93** proceed / **61** leave) · Band: `1k-5k` · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **protocol / CLI / path / quoting bugs with regression tests** (DNS, proxies, tunnels, HTTP/QUIC CLIs — not ML frameworks, not awesome-lists, not offensive/circumvention kits).

## Policy histogram (deep sample of 155)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 148 | No hard ban in common CONTRIBUTING/AI paths |
| disclosure | 4 | pomerium, nut, ferron, avahi (PowerDNS/iPXE reclassified after deep read) |
| hard_ban | 2 | `PowerDNS/pdns` (no AI code), `ipxe/ipxe` (no AI-generated PRs/issues) |
| hostility_risk | 1 | `meshbird/meshbird` AGENTS.md for autonomous agents |
| **agentscan** | 0 | No sample repo/owner on local adopters/blacklist |

Proceed: **93** · Leave: **61** · Scored lines appended to `survey/scored.jsonl` with `band:"1k-5k"`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class (protocol/CLI/path/quoting + tests). Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `pomerium/pomerium` | 4997 | disclosure | Identity-aware access proxy; AI_POLICY requires disclose + human understanding | redirect/URL path or policy rule edge + go tests — disclose AI |
| `NLnetLabs/unbound` | 4859 | silent | Validating recursive DNS resolver — classic protocol product | conf/ACL/path or DNSSEC edge + tests |
| `microsoft/msquic` | 4775 | silent | IETF QUIC C implementation — protocol framing surface | QUIC frame/path or API edge + tests |
| `antoniomika/sish` | 4712 | silent | SSH HTTP/TCP tunnel CLI (ngrok-class) | CLI flag/URL path or reverse tunnel edge + go tests |
| `acassen/keepalived` | 4680 | silent | VRRP/HA daemon — conf path/protocol edges | keepalived.conf path/VRRP edge + tests |
| `openziti/zrok` | 4668 | silent | Zero-trust sharing / reverse proxy CLI | share/token/path CLI edge + go tests |
| `ktr0731/evans` | 4493 | silent | Expressive gRPC client CLI — proto/path/flag classic | CLI flag/proto descriptor/path edge + go tests |
| `novnc/websockify` | 4446 | silent | WebSocket↔TCP bridge — path/URL proxy product | WS URL/path or target dial edge + tests |
| `openziti/ziti` | 4381 | silent | OpenZiti zero-trust network fabric CLI/runtime | identity/config path or dial edge + go tests |
| `networkupstools/nut` | 4329 | disclosure | Network UPS Tools protocol stack; disclose AI in PR/commit | driver/path or ups.conf quoting edge + tests — disclose |
| `FRRouting/frr` | 4279 | silent | Routing protocol suite (BGP/OSPF/…) — conf/CLI edges | vtysh/conf path or route-map edge + tests |
| `monasticacademy/httptap` | 4177 | silent | HTTP/HTTPS capture CLI via netns/TUN | CLI flag/path or filter edge + go tests |
| `nextdns/nextdns` | 4162 | silent | NextDNS DoH proxy CLI | CLI/config path or DoH upstream edge + go tests |
| `octelium/octelium` | 4039 | silent | Self-hosted zero-trust secure access platform | policy/path or gateway edge + go tests |
| `zhaojh329/rtty` | 4035 | silent | Web remote tty / HTTP proxy for devices | token/path or proxy dial edge + tests |
| `kumahq/kuma` | 3998 | silent | CNCF service mesh control plane (Envoy) | mesh/policy path or zone config edge + go tests |
| `willnorris/imageproxy` | 3990 | silent | Caching/resizing image HTTP proxy | URL/path or allowlist edge + go tests |
| `DNSControl/dnscontrol` | 3934 | silent | DNS-as-code CLI — provider/path/quoting classic | DSL/path or provider record edge + go tests |
| `fastly/pushpin` | 3856 | silent | HTTP push/streaming proxy (Fanout core) | route/path or pub/sub edge + tests |
| `IrineSistiana/mosdns` | 3733 | silent | DNS forwarder/proxy with DoH/DoT/DoQ | plugin/config path or matcher edge + go tests |
| `fortio/fortio` | 3724 | silent | HTTP/gRPC load-test CLI + echo server | CLI argv/URL/path edge + go tests |
| `sozu-proxy/sozu` | 3721 | silent | Rust HTTP reverse proxy, runtime config | config/path or cluster routing edge + rust tests |
| `kevwan/tproxy` | 3707 | silent | TCP proxy/analyze CLI | CLI flag/addr/path edge + go tests |
| `nadoo/glider` | 3701 | silent | Multi-protocol forward proxy + DNS/DHCP | proxy URL/scheme or dns listen path + go tests |
| `pgrok/pgrok` | 3644 | silent | Multi-tenant HTTP/TCP reverse tunnel via SSH | tunnel path/OIDC/config edge + go tests |
| `darkk/redsocks` | 3618 | silent | Transparent TCP→proxy redirector | redsocks.conf path/quoting edge + tests |
| `ory/oathkeeper` | 3599 | silent | Identity & Access Proxy / decision API | rules/path or authenticator edge + go tests |
| `abhinavsingh/proxy.py` | 3549 | silent | Lightweight pluggable HTTP/HTTPS/SOCKS proxy | plugin/path or TLS intercept edge + py tests |
| `bojand/ghz` | 3353 | silent | gRPC load-test CLI | proto/path/flag edge + go tests |
| `mmatczuk/go-http-tunnel` | 3332 | silent | Tunnels over HTTP/2 | tunnel URL/path or auth edge + go tests |
| `AdguardTeam/dnsproxy` | 3322 | silent | DNS proxy with DoH/DoT/DoQ/DNSCrypt | upstream/bootstrap path or protocol edge + go tests |
| `the-tcpdump-group/tcpdump` | 3235 | silent | Packet capture CLI — argv/filter path classic | pcap filter/path or argv edge + tests |
| `progrium/localtunnel` | 3227 | silent | Expose localhost tunnel CLI | CLI URL/path edge + go tests |
| `vnt-dev/vnt` | 3202 | silent | P2P VPN / NAT traversal CLI (Rust) | config/path or peer addr edge + cargo tests |
| `amalshaji/portr` | 3185 | silent | Local HTTP/TCP/WS expose CLI (ngrok-class) | CLI flag/URL path edge + go tests |
| `the-tcpdump-group/libpcap` | 3168 | silent | pcap capture library used by tcpdump | filter/path or device name edge + tests |
| `squid-cache/squid` | 3090 | silent | HTTP caching proxy — conf/ACL path product | squid.conf ACL/path edge + tests |
| `rtr7/router7` | 2768 | silent | Home router in Go (gokrazy) | net/DHCP/path config edge + go tests |
| `mehrdadrad/mylg` | 2718 | silent | Network diagnostic CLI (ping/BGP/…) | CLI argv/path edge + go tests |
| `dlundquist/sniproxy` | 2717 | silent | SNI/Host-based TLS/HTTP proxy | sniproxy.conf path/table edge + tests |
| `dannagle/PacketSender` | 2675 | silent | TCP/UDP/SSL/HTTP packet utility CLI/GUI | CLI argv/URL/path edge + tests |
| `nanomq/nanomq` | 2610 | silent | Lightweight MQTT broker for edge | topic/config path edge + tests |
| `zhboner/realm` | 2587 | silent | Network relay tool (Rust) | rule/config path or listen edge + cargo tests |
| `containernetworking/plugins` | 2571 | silent | CNI reference networking plugins | CNI conf/path or IPAM edge + go tests |
| `hmgle/graftcp` | 2566 | silent | Redirect TCP/UDP/DNS to SOCKS5/HTTP proxies | proxy target/path or DNS redirect edge + tests |
| `jedisct1/piknik` | 2518 | silent | Copy/paste over network CLI | CLI path/URL edge + go tests |
| `natesales/q` | 2516 | silent | Tiny multi-protocol DNS client CLI (DoH/DoT/DoQ) | CLI flag/server/path edge + go tests |
| `dndx/phantun` | 2382 | silent | UDP→fake-TCP transformer for NAPT | CLI/config path edge + rust tests |
| `gsliepen/tinc` | 2245 | silent | Mesh VPN daemon | tinc.conf path/subnet edge + tests |
| `mozilla/neqo` | 2233 | silent | Firefox QUIC/HTTP3 (Rust) | QUIC/HTTP3 frame or qlog path edge + rust tests |
| `c-ares/c-ares` | 2190 | silent | Async DNS C library | name/resolve or option edge + tests |
| `ferronweb/ferron` | 2131 | disclosure | HTTP server; Assisted-by footer; no autonomous agent PRs | vhost/path or config edge + rust tests — Assisted-by |
| `heiher/hev-socks5-tunnel` | 2013 | silent | tun2socks lightweight tunnel | tun/DNS/path config edge + tests |
| `yyyar/gobetween` | 1986 | silent | Modern L4/L7 load balancer | balancer config/path or discovery edge + go tests |
| `apache/trafficserver` | 1981 | silent | Apache Traffic Server HTTP cache proxy | remap/path or config edge + tests |
| `dswd/vpncloud` | 1976 | silent | P2P mesh VPN (Rust) | peer/config path edge + cargo tests |
| `heiher/natmap` | 1953 | silent | Full-cone NAT TCP/UDP port mapping CLI | CLI argv/path edge + tests |
| `mochi-mqtt/server` | 1924 | silent | Embeddable MQTT v5 broker | topic/path or auth edge + go tests |
| `alibaba/xquic` | 1916 | silent | Alibaba QUIC/HTTP3 library | QUIC frame/path edge + tests |
| `litespeedtech/lsquic` | 1869 | silent | LiteSpeed QUIC/HTTP3 library | QUIC/HTTP3 parse edge + tests |
| `vergoh/vnstat` | 1769 | silent | Network traffic monitor CLI | db/path or iface config edge + tests |
| `mholt/caddy-l4` | 1766 | silent | Caddy Layer4 TCP/UDP app | Caddyfile L4 route/path edge + go tests |
| `alebeck/boring` | 1667 | silent | SSH tunnel manager CLI | tunnel config/path edge + go tests |
| `miniupnp/miniupnp` | 1602 | silent | UPnP IGD / NAT-PMP implementation | config/path or SSDP edge + tests |
| `EmbarkStudios/quilkin` | 1588 | silent | UDP proxy for game servers | filter/config path edge + rust tests |
| `kffl/speedbump` | 1558 | silent | TCP latency-injection proxy CLI | CLI latency/path edge + go tests |
| `txthinking/zoro` | 1547 | silent | Expose local TCP/UDP/HTTP tunnel | tunnel path/CLI edge + go tests |
| `avahi/avahi` | 1544 | disclosure | mDNS/DNS-SD; human-in-the-loop for LLM content | service/path or browse edge + tests — review LLM output |
| `azimjohn/jprq` | 1539 | silent | Quick public tunnel (ngrok-class) | tunnel URL/path CLI edge + go tests |
| `ngtcp2/ngtcp2` | 1510 | silent | IETF QUIC C library | QUIC packet/frame edge + tests |
| `moq-dev/moq` | 1500 | silent | Media over QUIC | moq path/session edge + rust tests |
| `ContentSquare/chproxy` | 1481 | silent | ClickHouse HTTP proxy/LB | auth/path or query ACL edge + go tests |
| `wiresock/proxifyre` | 1479 | silent | Windows SOCKS5 proxifier (NDISAPI) | rule/path or process match edge + tests |
| `litespeedtech/openlitespeed` | 1476 | silent | OpenLiteSpeed HTTP server | vhost/path or config edge + tests |
| `GoogleCloudPlatform/cloud-sql-proxy` | 1434 | silent | Cloud SQL Auth Proxy CLI | instance/path or flag edge + go tests |
| `Tencent/tquic` | 1429 | silent | Tencent QUIC library (Rust) | QUIC frame/path edge + rust tests |
| `looterz/grimd` | 1415 | silent | DNS proxy that blackholes ads/malware | blocklist/path or listen edge + go tests |
| `rosenpass/rosenpass` | 1411 | silent | Post-quantum WireGuard key exchange VPN helper | config/path or peer key edge + rust tests |
| `tun2proxy/tun2proxy` | 1407 | silent | TUN→SOCKS/HTTP proxy tunnel | tun/proxy URL path edge + rust tests |
| `boringproxy/boringproxy` | 1383 | silent | Self-hosted tunneling reverse proxy + auto HTTPS | tunnel/path or TLS edge + go tests |
| `jvns/dnspeep` | 1383 | silent | Spy on local DNS queries CLI | pcap/filter/path edge + rust tests |
| `aws/s2n-quic` | 1370 | silent | AWS s2n QUIC implementation | QUIC frame/path edge + rust tests |
| `mullvad/gotatun` | 1366 | silent | Userspace WireGuard in Rust | config/path or peer endpoint edge + rust tests |
| `stripe/smokescreen` | 1334 | silent | Egress HTTP proxy that fogs naughty URLs | allowlist/path or CONNECT edge + go tests |
| `pouriyajamshidi/tcping` | 1333 | silent | TCP ping CLI | CLI host/port/argv edge + go tests |
| `jamesmcm/vopono` | 1323 | silent | App-in-netns VPN tunnel CLI (WG/OpenVPN) | provider/config path edge + rust tests |
| `DNSCrypt/encrypted-dns-server` | 1321 | silent | Encrypted DNS server proxy (DoH/DNSCrypt) | stamp/config path edge + rust tests |
| `umputun/reproxy` | 1309 | silent | Simple edge reverse proxy | route/path config edge + go tests |
| `opengnb/opengnb` | 1204 | silent | Decentralized P2P SDVN / layer-3 overlay | node/config path edge + tests |
| `pendulum-project/ntpd-rs` | 1140 | silent | Full NTP/NTS daemon (Rust) | config/path or NTS edge + rust tests |
| `ngtcp2/nghttp3` | 1137 | silent | HTTP/3 (QPACK) C library | QPACK/frame edge + tests |
| `DNSCrypt/doh-server` | 1067 | silent | DoH/ODoH server proxy (Rust) | config/path or upstream edge + rust tests |
| `aramperes/onetun` | 1041 | silent | Userspace WireGuard port-forward CLI | peer/port-forward path edge + rust tests |

### Tier notes

**Best first homes (small testable protocol/CLI/path hunks):**

1. `natesales/q` / `AdguardTeam/dnsproxy` / `DNSControl/dnscontrol` / `nextdns/nextdns` / `IrineSistiana/mosdns` / `DNSCrypt/doh-server` / `DNSCrypt/encrypted-dns-server` / `jvns/dnspeep` / `looterz/grimd` / `NLnetLabs/unbound` / `c-ares/c-ares` — DNS CLI/proxy/resolver cluster.
2. `ktr0731/evans` / `bojand/ghz` / `fortio/fortio` — gRPC/HTTP load & client CLIs (flag/proto/path).
3. `antoniomika/sish` / `pgrok/pgrok` / `amalshaji/portr` / `azimjohn/jprq` / `boringproxy/boringproxy` / `alebeck/boring` / `mmatczuk/go-http-tunnel` / `progrium/localtunnel` / `txthinking/zoro` — tunnel/expose CLIs.
4. `kevwan/tproxy` / `darkk/redsocks` / `dlundquist/sniproxy` / `hmgle/graftcp` / `nadoo/glider` / `abhinavsingh/proxy.py` / `tun2proxy/tun2proxy` / `stripe/smokescreen` / `umputun/reproxy` / `sozu-proxy/sozu` — proxy conf/URL/path.
5. `monasticacademy/httptap` / `pouriyajamshidi/tcping` / `kffl/speedbump` / `jedisct1/piknik` / `dannagle/PacketSender` / `the-tcpdump-group/tcpdump` — small capture/HTTP/TCP CLIs.
6. `microsoft/msquic` / `mozilla/neqo` / `ngtcp2/ngtcp2` / `ngtcp2/nghttp3` / `aws/s2n-quic` — QUIC/HTTP3 protocol libs.
7. `aramperes/onetun` / `mullvad/gotatun` / `rosenpass/rosenpass` / `jamesmcm/vopono` / `gsliepen/tinc` / `dswd/vpncloud` / `openziti/ziti` / `openziti/zrok` — VPN/overlay CLIs.
8. `pomerium/pomerium` — **must disclose** AI; `networkupstools/nut` — disclose; `ferronweb/ferron` — `Assisted-by:`; `avahi/avahi` — human review of LLM content.

**Proceed with process friction:**

- `pomerium/pomerium` — Ghostty-forked AI_POLICY: disclose tool+extent; human must explain without AI.
- `networkupstools/nut` — PR template asks AI disclosure in commits.
- `ferronweb/ferron` — Assisted-by footer; no autonomous agent-opened PRs.
- `avahi/avahi` — LLVM-style human-in-the-loop for substantial LLM content.
- Apache (`trafficserver`) — generative tooling guidance / Apache license provenance.
- `kumahq/kuma` / `octelium/octelium` — prefer small tested config edges over feature PRs.

**Clusters to farm leftovers (one home at a time):**

| Cluster | Repos | Hunk shape |
|---|---|---|
| DNS | unbound, dnsproxy, mosdns, nextdns, dnscontrol, q, doh-server, encrypted-dns-server, grimd, dnspeep, c-ares, avahi | zone/stamp/DoH/config path |
| Tunnels | sish, pgrok, portr, jprq, boringproxy, boring, go-http-tunnel, localtunnel, zoro, hev-socks5-tunnel, natmap, onetun | CLI flag / URL / SSH / port-forward |
| Proxies | glider, proxy.py, redsocks, sniproxy, graftcp, smokescreen, reproxy, sozu, squid, trafficserver, chproxy, pushpin, oathkeeper, imageproxy, realm, proxifyre, tun2proxy | conf quoting / SNI / allowlist / route |
| HTTP/QUIC CLI | evans, ghz, fortio, httptap, msquic, neqo, ngtcp2, nghttp3, s2n-quic, xquic, lsquic, tquic, moq, ferron | argv / proto / frame / QPACK |
| VPN/overlay | gotatun, rosenpass, vopono, tinc, vpncloud, ziti, zrok, vnt, opengnb, pomerium | conf / peer / CIDR / identity path |
| Classic protocol | tcpdump, libpcap, frr, keepalived, ntpd-rs, nut, vnstat, mylg, tcping, PacketSender, piknik, speedbump | argv / filter / conf path |

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `IAmStoxe/wirehole` | 4971 | silent | docker-compose glue (WG+pihole+unbound) — not product source |
| `CrowCpp/Crow` | 4966 | silent | C++ web microframework — not protocol/CLI product home |
| `xinliangnote/Go` | 4961 | silent | Go tutorial notes — not product |
| `nicocha30/ligolo-ng` | 4927 | silent | Offensive pivoting/TUN tunnel — leave |
| `apache/iggy` | 4830 | silent | Message streaming — distributed but not DNS/proxy/tunnel/CLI class this pass |
| `dkron-io/dkron` | 4736 | silent | Distributed cron — not networking protocol/CLI home |
| `cloudwego/netpoll` | 4603 | silent | RPC-oriented netpoll framework lib — prefer product CLIs |
| `ntop/nDPI` | 4595 | silent | DPI toolkit — security-sector adjacent; defer |
| `smoltcp-rs/smoltcp` | 4591 | silent | Embedded TCP/IP stack — high bar; defer vs CLI homes |
| `NVlabs/tiny-cuda-nn` | 4533 | silent | ML/CUDA neural net — wrong-class noise |
| `projectdiscovery/interactsh` | 4524 | silent | Bug-bounty OOB interaction server — leave |
| `mosn/mosn` | 4508 | silent | Heavy service-mesh data plane — prefer smaller CLI first |
| `PowerDNS/pdns` | 4464 | hard_ban | AI_POLICY forbids AI tools for code contributions |
| `WireGuard/wireguard-go` | 4388 | silent | Mirror-only (canonical at git.zx2c4.com) — no GH PR home |
| `cbeuw/Cloak` | 4081 | silent | Censorship circumvention pluggable transport — leave |
| `connectrpc/connect-go` | 4064 | silent | RPC framework library — prefer evans/ghz CLIs |
| `apache/httpd` | 4054 | silent | GitHub mirror; issues/PRs on ASF — not GH contrib home |
| `openthread/openthread` | 4027 | silent | Thread IoT stack — embedded firmware class |
| `emitter-io/emitter` | 4005 | silent | MQTT pubsub platform — closer to messaging; defer |
| `apache/guacamole-server` | 3981 | silent | Remote desktop proxy — heavy C; not first path/quoting home |
| `BenedictKing/ccx` | 3971 | silent | Claude/Codex/Gemini API proxy — AI glue not networking product |
| `EvilGenius-dot/RustMinerSystem` | 3880 | silent | Miner proxy malware-adjacent — leave |
| `9seconds/mtg` | 3671 | silent | Telegram MTPROTO proxy — leave (MTProxy class) |
| `dunglas/vulcain` | 3593 | silent | HTTP API early-hints pattern — weak CLI/protocol home |
| `meshbird/meshbird` | 3526 | hostility_risk | AGENTS.md for autonomous agents; weak maintenance signal |
| `TrustTunnel/TrustTunnel` | 3450 | silent | Obfuscated VPN protocol — circumvention-leaning |
| `ph4ntonn/Stowaway` | 3416 | silent | Pentest multi-hop proxy — leave |
| `basil00/WinDivert` | 3288 | silent | Windows packet divert — dual-use / Windows-only; leave |
| `DhavalKapil/icmptunnel` | 3253 | silent | ICMP tunnel often used for bypass; prefer iodine already proceed elsewhere |
| `iqiyi/dpvs` | 3242 | silent | DPDK L4 LB — specialized hardware; weak outsider path |
| `Devolutions/IronRDP` | 3153 | silent | RDP stack — remote desktop class; defer |
| `projectdiscovery/proxify` | 3067 | silent | Security MITM capture toolkit — leave this account |
| `slact/nchan` | 3065 | silent | Nginx pubsub module — satellite to nginx |
| `risinek/esp32-wifi-penetration-tool` | 3061 | silent | Wi-Fi attack tool — leave |
| `facebook/wdt` | 2956 | silent | Meta data-transfer tool — CLA/high bar |
| `favonia/cloudflare-ddns` | 2886 | silent | DDNS updater glue — weak protocol hunk (cf. ddns-go leave) |
| `knadh/dns.toys` | 2826 | silent | Novelty DNS utilities — weak product home |
| `skydive-project/skydive` | 2798 | silent | Network topology analyzer — heavy observability product |
| `srl-labs/containerlab` | 2796 | silent | Lab orchestration — not protocol/CLI product hunk home |
| `paullouisageneau/libdatachannel` | 2734 | silent | WebRTC C++ lib — high bar; defer |
| `libpnet/libpnet` | 2592 | silent | Low-level packet lib — prefer product CLIs |
| `wangyu-/tinyfecVPN` | 2586 | silent | Lossy-link VPN often used for circumvention — awkward home |
| `webserver-llc/angie` | 2566 | silent | Nginx drop-in commercial fork — prefer caddy/sozu first |
| `enfein/mieru` | 2534 | silent | Censorship-bypass socks/HTTP proxy — leave |
| `x90skysn3k/brutespray` | 2528 | silent | Credential brute-forcer — leave |
| `SpectoLabs/hoverfly` | 2512 | silent | API simulation/mock — not networking protocol home |
| `SoftEtherVPN/SoftEtherVPN_Stable` | 2227 | silent | not in scored set |
| `mtcp-stack/mtcp` | 2136 | silent | Userspace TCP stack — research/high bar; defer |
| `FoxIO-LLC/ja4` | 2079 | silent | JA4 fingerprint standards — security-sector adjacent |
| `ipxe/ipxe` | 2043 | hard_ban | CONTRIBUTING bans AI-generated issues/PRs with permanent ban |
| `editso/fuso` | 1950 | silent | CN NAT penetrate tool — circumvention-leaning |
| `sysdream/ligolo` | 1788 | silent | Pentest reverse tunnel — leave |
| `Watfaq/clash-rs` | 1710 | silent | Clash-class circumvention proxy — leave |
| `labstack/armor` | 1659 | silent | HTTP server; lower activity / weak signal vs sozu/reproxy |
| `doxx/darkflare` | 1596 | silent | Firewall-piercing TCP-over-CDN — leave |
| `uNetworking/uSockets` | 1494 | silent | Eventing/crypto networking lib — framework-only |
| `inlets/inlets-operator` | 1436 | silent | K8s operator wrapper — prefer tunnel CLIs |
| `hyperium/http` | 1380 | silent | HTTP types crate only — prefer hyper/quiche product surfaces |
| `cfal/shoes` | 1218 | silent | Multi-protocol circumvention proxy (naive/hysteria/…) — leave |
| `orbien-org/orbien` | 1211 | silent | CN NAT tunnel multi-protocol — circumvention-leaning |
| `plabayo/rama` | 1193 | silent | Composable networking service framework — not CLI product first |

### Leave themes

- **Hard ban:** `PowerDNS/pdns` (AI_POLICY: AI tools for code contributions not allowed), `ipxe/ipxe` (no AI-generated issues/PRs; permanent ban).
- **Hostility risk:** `meshbird/meshbird` (AGENTS.md aimed at autonomous agents).
- **Offensive / circumvention:** ligolo-ng, ligolo, Stowaway, brutespray, esp32-wifi-pen, Cloak, mieru, clash-rs, darkflare, shoes, mtg, interactsh, proxify, miner proxies, tinyfecVPN/fuso/orbien/TrustTunnel-class.
- **Wrong-class noise:** Crow framework, Go tutorial notes, tiny-cuda-nn, wirehole compose, dkron, apache/iggy messaging, ccx AI API proxy.
- **Mirror / non-GH home:** `WireGuard/wireguard-go`, `apache/httpd` (ASF).
- **Defer high-bar / satellite / framework-only:** guacamole, IronRDP, WinDivert, dpvs, mtcp, libpnet, libdatachannel, nchan, hoverfly, containerlab, skydive, netpoll, connect-go, hyperium/http, uSockets, rama, nDPI.
- **AgentScan:** none in midband sample (re-check before fork).
- **Predecessor queues:** none of these midband repos are on the forever-out / open ledger for this account (`awesome-copilot` closed; `sharkdp/fd` open is other sector).

## Method notes

- Policy files fetched primarily via `raw.githubusercontent.com`; workflow names via `gh api repos/.../contents/.github/workflows`.
- Deep overrides after reading live AI_POLICY/CONTRIBUTING: PowerDNS + iPXE → hard_ban; meshbird → hostility_risk.
- No fork, PR, issue, or comment created.
- Hard leaves applied: QEMU/GIMP patterns (none in midband sample), AgentScan circle, predecessor closed queues, offensive/circumvention kits.
