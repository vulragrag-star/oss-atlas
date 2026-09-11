# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2656**
- Proceed: **1814**
- Mid-band (1k–5k★) scored: **1402** (proceed 1022)
- By sector: {'python-tooling': 353, 'security-crypto': 363, 'cli-systems': 290, 'editors-devex': 353, 'compilers-runtimes': 287, 'databases-storage': 335, 'networking-distributed': 356, 'devops-build': 319}
- Policy mix: {'silent': 2339, 'hard_ban': 33, 'disclosure': 232, 'hostility_risk': 33, 'agentscan': 19}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **security-crypto midband product deepen** (+93 scored, 53 proceed) — server, fail2ban, supertokens-core, git-secrets, jjwt, django-allauth, ModSecurity, testssl.sh, secretive, lesspass, boulder, opal, authlib,…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Security-crypto midband product deepen scored PKI/TLS/IAM/secrets/SBOM/SAST/WAF/authZ homes (fail2ban/boulder/secretive/cerbos/keto/opal/coraza/dependency-track/hayabusa/kubesec/sops-nix/sudo-rs/git-secrets/talisman/certspotter/testssl/memguard/SimpleWebAuthn/bitwarden-server). Leave Casbin language bindings, thin JWT middleware, frontend OIDC clients, badssl content site, SPIFFE specs-only, recon scanners (zgrab2), framework auth satellites. Disclosure: keto, cerbos, sudo-rs, cartography, keepassxc-browser, stackrox.
Prior editors midband + devops/python/DB/networking/compilers/security highband deepens remain scored; continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff/unplugin/gritql), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3 / Python deepen-2 leaves retained. DevOps deepen-2: kueue scanner hard_ban overridden to disclosure (K8s AI policy); s6-overlay disclosure overridden to hard_ban (no LLM contrib). Editors midband deepen: rolldown/tsdown NO-AI, loeffel-io/ls-lint NO-AI. Security midband deepen: no new hard_ban/agentscan in this curated slice.

## Next
Next: SHORTLIST maintenance or deepen remaining thin midband (cli-systems / compilers-runtimes) / selective universe gap fills; contribution cadence remains separate from atlas literature work.
