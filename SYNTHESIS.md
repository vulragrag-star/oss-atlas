# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1806**
- Proceed: **1249**
- Mid-band (1k–5k★) scored: **1065** (proceed 792)
- By sector: {'python-tooling': 216, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 175, 'compilers-runtimes': 184, 'databases-storage': 217, 'networking-distributed': 236, 'devops-build': 218}
- Policy mix: {'silent': 1609, 'hard_ban': 19, 'disclosure': 144, 'hostility_risk': 29, 'agentscan': 5}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **security-crypto product deepen** (+104 scored, 66 proceed) — vaultwarden, traefik, acme.sh, trivy, AdGuardHome, keycloak, tailscale, vault, certbot, jumpserver, nuclei, openssl, better-auth, gitleaks, …
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Security-crypto product deepen scored secrets/PKI/IAM/SBOM/SAST/access homes (vaultwarden, vault, trivy, gitleaks, keycloak, authentik, OPA, teleport, falco, scorecard). Leave offensive scanners/crackers, RE frameworks, VPN install recipes, mesh megas (istio/envoy/cilium), and wrong-sector (renovate/golangci/kibana). Disclosure/careful: openssl, keycloak, authentik, certbot, keepassxc, ory/*, better-auth, anubis, traefik, opa, external-secrets.
Famous shells/editors gap fill remains scored; full terminal emulators stay leave. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed. Note: certbot/authentik scanner NO-AI hits were false positives (AI allowed with disclosure/HITL).

## Next
Next thin tails: editors-devex product deepen, or rebuild SHORTLIST/SYNTHESIS after more scores. Contribution cadence remains separate from atlas literature work.
