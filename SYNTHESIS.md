# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **3133**
- Proceed: **2158**
- Mid-band (1k–5k★) scored: **1787** (proceed 1299)
- By sector: {'python-tooling': 353, 'security-crypto': 363, 'cli-systems': 378, 'editors-devex': 353, 'compilers-runtimes': 376, 'databases-storage': 446, 'networking-distributed': 444, 'devops-build': 420}
- Policy mix: {'silent': 2788, 'hard_ban': 37, 'disclosure': 256, 'hostility_risk': 33, 'agentscan': 19}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **networking-distributed midband product deepen** (+88 scored, 68 proceed) — tcpcopy, nng, wrk2, grpc-web, pwru, octodns, massdns, asterisk, skipper, OvenMediaEngine, assh, PcapPlusPlus, strongswan, PF_RING, kamailio, krakend-ce, volo, f…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Networking-distributed midband product deepen scored DNS/QUIC/gRPC/proxy/LB/tunnel/VPN/WebRTC/SFU/SIP/load-test/packet/MQTT/CNI leftovers (octodns/massdns/FTL/sdns/geodns, skipper/krakend/river/pingap/trickster/loxilb/openelb, strongswan/microsocks/assh/mole/sshpiper/kilo/reverst, OvenMedia/asterisk/kamailio/opensips/baresip/galene/stunner, wrk2/drill/tcpcopy/pwru/PcapPlusPlus/ptcpdump/sniffglue/tcpreplay/ngrep/dstp/asn, nng/hmq/aedes/comqtt/gmqtt/rmqtt/kafkactl, volo/srpc/drpc/grpc-web/rumqtt…). Leave thin SOCKS libs, VPN GUIs, novelty DNS, stale WG mgmt, quiet SFUs, young gateways, circumvention P2P. Disclosure: trickster, pwru, freeradius-server.
Prior cli-systems/editors/compilers/python/DB/networking/security/devops midband product deepens remain scored; continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff/unplugin/gritql), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3 / Python deepen-2 leaves retained. DevOps deepen-2: kueue scanner hard_ban overridden to disclosure (K8s AI policy); s6-overlay disclosure overridden to hard_ban (no LLM contrib). Editors midband deepen: rolldown/tsdown NO-AI, loeffel-io/ls-lint NO-AI. CLI-systems midband product deepen retained. Compilers-runtimes midband product deepen: hard_ban capstone-engine/capstone (forbids AI), FEX-Emu/FEX (NO-AI). DevOps-build midband product deepen: hard_ban getarcaneapp/arcane (NO-AI). Databases-storage midband product deepen: hard_ban neilotoole/sq (NO-AI). Networking-distributed midband product deepen: no new hard_ban/AgentScan in this pass; disclosure pwru/FreeRADIUS/trickster.

## Next
Next: remaining thin midband product deepens (python) or SHORTLIST maintenance; contribution cadence remains separate from atlas literature work.
