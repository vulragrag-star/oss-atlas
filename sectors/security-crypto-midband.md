# Sector survey: security-crypto (mid-band 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/security-crypto-midband.jsonl` · Deep-sampled **82** real product repos (policy via `raw.githubusercontent.com` + workflow names) · Scored **82** lines (**52** proceed / **30** leave) · Band: `1k-5k` · No fork/PR/comment.

Playbook lens: famous main product (1k–5k★), not AgentScan, not hard AI ban, prefer **PKI / TLS / IAM / secrets CLI / SAST / ACME** with tests. Do **not** drive-by novel cryptography, consensus chains, phishing kits, or rootkits — stick to build/parser/path/config bugs with regression tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 81 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 1 | Explicit AI-assisted / disclosure language (or org AI policy) |

Proceed: **52** · Leave: **30** · Scored lines appended to `survey/scored.jsonl` with `band:"1k-5k"`.

## Hard leaves (playbook — even if outside this band sample)

- `kanidm/kanidm` — AGENTS.md does not condone LLMs/AI; PR template bans AI-generated content (higher band leave)
- `openbao/openbao` — AGENTS.md rejects all AI-generated contributions + robot-emoji honeypot (higher band leave)
- Consensus cryptocurrency cores / novel crypto primitives — leave
- Offensive / phishing / rootkit / deauth kits — leave
- AgentScan adopter orgs — leave entire owner tree

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `perplexityai/bumblebee` | 4989 | silent | Read-only supply-chain exposure scanner CLI | scan path/package metadata edge + Go tests |
| `diafygi/acme-tiny` | 4769 | silent | Tiny ACME/Let's Encrypt client script | ACME challenge/path edge + py tests |
| `aws/s2n-tls` | 4761 | silent | AWS TLS/SSL implementation — config/API edges only | TLS config/API edge + C tests — not novel crypto |
| `build-trust/ockam` | 4638 | silent | End-to-end encryption + identity orchestration | identity/route/path edge + Rust tests |
| `smallstep/cli` | 4326 | silent | step CLI for X509/OAuth/JWT/OATH | CLI path/cert/JWT edge + Go tests |
| `openssh/openssh-portable` | 3995 | silent | Portable OpenSSH — small path/config edges only | sshd_config/path or argv edge + tests |
| `nabla-c0d3/sslyze` | 3777 | silent | SSL/TLS scanning library/CLI | scan/CLI/path edge + py tests |
| `google/trillian` | 3747 | silent | Transparent verifiable log — API/path edges | log API/path/leaf edge + Go tests |
| `microcosm-cc/bluemonday` | 3717 | silent | Go HTML sanitizer | HTML allowlist/parse edge + Go tests |
| `WithSecureLabs/chainsaw` | 3655 | silent | Windows forensic artefact hunt CLI | rule/path/hunt edge + Rust tests |
| `e-m-b-a/emba` | 3651 | silent | Firmware security analyzer | firmware path/analyzer edge + tests |
| `go-oauth2/oauth2` | 3620 | silent | OAuth 2.0 server library (Go) | OAuth grant/config edge + Go tests |
| `google/OpenSK` | 3419 | silent | Open-source security key firmware | CTAP/config edge + Rust tests — hardware care |
| `deepfence/SecretScanner` | 3386 | silent | Secrets in container images/FS | scan path/rule edge + Go tests |
| `randombit/botan` | 3310 | silent | Cryptography toolkit — config/API only | config/API edge + C++ tests — not novel algos |
| `vouch/vouch-proxy` | 3284 | silent | SSO/OIDC auth_request proxy for Nginx | redirect/cookie/path edge + Go tests |
| `tellerops/teller` | 3230 | silent | Cloud-native secrets CLI | provider/path/config edge + Rust tests |
| `jhaals/yopass` | 3110 | silent | Secure one-time secret sharing | secret URL/path/TTL edge + Go tests |
| `C2SP/wycheproof` | 3104 | silent | Crypto test vectors against known attacks | test-vector/parse edge + Go tests |
| `baidu/openrasp` | 2989 | silent | Open-source RASP | hook/config/path edge + tests |
| `wolfSSL/wolfssl` | 2931 | silent | Embedded TLS library — config/API only (CLA required) | TLS config/API edge + tests — CLA first |
| `google/osv.dev` | 2916 | silent | Open Source Vulnerabilities DB/triage | purl/advisory parse edge + Go tests |
| `FiloSottile/yubikey-agent` | 2905 | silent | YubiKey ssh-agent | agent/path/pin entry edge + Go tests |
| `glauth/glauth` | 2846 | silent | Lightweight LDAP server | LDAP config/path edge + Go tests |
| `acme-dns/acme-dns` | 2826 | silent | Limited DNS server for ACME DNS-01 | API/DNS record/path edge + Go tests |
| `DefGuard/defguard` | 2821 | silent | Zero-trust access + WireGuard MFA | auth/config/path edge + Rust tests |
| `Bearer/bearer` | 2743 | silent | SAST for security/privacy data flows | rule/path/scan edge + Go tests |
| `rbsec/sslscan` | 2622 | silent | SSL/TLS cipher suite scanner CLI | CLI argv/TLS probe edge + tests |
| `ory/fosite` | 2615 | silent | OAuth2/OIDC SDK (Go) | OAuth grant/config edge + Go tests |
| `ory/ladon` | 2457 | silent | Access-control policy SDK | policy parse/match edge + Go tests |
| `square/certstrap` | 2453 | silent | Bootstrap CAs/CSRs/certs CLI | CA/path/CSR edge + Go tests |
| `cloudflare/gokey` | 2433 | silent | Vaultless password manager CLI | derive/path/CLI edge + Go tests |
| `lestrrat-go/jwx` | 2422 | silent | Complete JWx/JOSE implementation | JWS/JWE/JWT parse edge + Go tests |
| `crev-dev/cargo-crev` | 2332 | silent | Cryptographically verifiable cargo review | review/path/proof edge + Rust tests |
| `srvrco/getssl` | 2230 | silent | ACME SSL certificate automation | ACME/path/domain edge + shell tests |
| `jdx/fnox` | 2144 | disclosure | Encrypted/remote secret manager; AGENTS.md present | provider/path/config edge + Rust tests — follow AGENTS |
| `qvest-digital/loginsrv` | 1930 | silent | JWT login microservice | JWT/backend/config edge + Go tests |
| `zitadel/oidc` | 1887 | silent | Certified OIDC client/server library (Go) | OIDC flow/config edge + Go tests |
| `sniptt-official/ots` | 1845 | silent | One-time encrypted secret URLs | secret URL/TTL/path edge + Go tests |
| `privacyidea/privacyidea` | 1769 | silent | Multi-factor auth system (OTP/FIDO) | token/config/path edge + py tests |
| `fwdcloudsec/granted` | 1769 | silent | AWS access CLI | CLI profile/path/SSO edge + Go tests |
| `ossf/cve-bin-tool` | 1758 | silent | CVE binary composition scanner | scanner/path/purl edge + py tests |
| `murphysecurity/murphysec` | 1753 | silent | Software composition analysis CLI | SCA/path/purl edge + Go tests |
| `guacsec/guac` | 1540 | silent | Software security metadata graph | SBOM/purl ingest edge + Go tests |
| `Tongsuo-Project/Tongsuo` | 1526 | silent | Modern crypto/protocols library (Tongsuo) | config/API edge + tests — not invent algorithms |
| `libressl/portable` | 1491 | silent | LibreSSL portable build — config/build edges only | build/config/path edge + tests — not novel crypto |
| `mesalock-linux/mesalink` | 1483 | silent | OpenSSL-compat layer over Rust TLS | API compat/path edge + Rust tests |
| `infrahq/infra` | 1467 | silent | AuthN/Z for servers/Kubernetes | identity/config/path edge + Go tests |
| `ZupIT/horusec` | 1336 | silent | SAST vulnerability identification CLI | rule/path/scan edge + Go tests |
| `go-webauthn/webauthn` | 1330 | silent | FIDO2/WebAuthn/Passkey Go library | WebAuthn ceremony/parse edge + Go tests |
| `sebadob/rauthy` | 1313 | silent | SSO IAM via OIDC/OAuth2/PAM | OIDC/config/path edge + Rust tests |
| `square/sudo_pair` | 1272 | silent | sudo plugin requiring human co-approval | plugin/config/path edge + Rust tests |

### Tier notes

**Best first homes (tooling + clear process):** `smallstep/cli`, `acme-dns/acme-dns`, `diafygi/acme-tiny`, `vouch/vouch-proxy`, `tellerops/teller` / `jdx/fnox` / `jhaals/yopass` (secrets CLIs), `ossf/cve-bin-tool`, `Bearer/bearer` / `ZupIT/horusec` (SAST), `lestrrat-go/jwx` / `zitadel/oidc` / `go-webauthn/webauthn`, `aws/s2n-tls` (config/API only). **Avoid** inventing crypto; wolfSSL needs CLA; BoringSSL is Gerrit-only.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `Awarexone/Agentic-Bug-Hunter` | 4722 | silent | AI bug-bounty / offensive toolkit — leave |
| `google/security-research` | 4627 | silent | Advisory + PoC dump — not product contrib home |
| `firmianay/CTF-All-In-One` | 4498 | silent | CTF guide dump — not product |
| `XTLS/RealiTLScanner` | 4350 | silent | Reality TLS scanner — circumvention-adjacent optics |
| `marmotedu/iam` | 4209 | silent | Course/tutorial IAM project — not production product queue |
| `PurpleI2P/i2pd` | 4194 | silent | I2P anonymity daemon — high scrutiny / wrong first home |
| `samyk/magspoof` | 4148 | silent | Magnetic-stripe spoof hardware — offensive optics |
| `microsoft/SEAL` | 4028 | silent | Homomorphic encryption research lib — novel crypto leave |
| `evyatarmeged/Raccoon` | 4015 | silent | Offensive recon/vuln scanner — leave |
| `cifertech/ESP32-DIV` | 3975 | silent | Offensive wireless toolkit — leave |
| `syncsynchalt/illustrated-tls12` | 3513 | silent | Illustrated TLS docs — not product code |
| `golang/crypto` | 3347 | silent | Go x/crypto mirror — stdlib-adjacent process |
| `s0md3v/Smap` | 3296 | silent | Shodan-powered nmap replacement — offensive optics |
| `Legrandin/pycryptodome` | 3262 | silent | Core crypto library — unsolicited crypto changes hated |
| `homenc/HElib` | 3248 | silent | Homomorphic encryption library — novel crypto leave |
| `open-quantum-safe/liboqs` | 3059 | silent | Experimental PQ crypto primitives — leave for early queue |
| `Qianlitp/crawlergo` | 3037 | silent | Browser crawler for vuln scanners — offensive adjacent |
| `FISCO-BCOS/FISCO-BCOS` | 2603 | silent | Permissioned blockchain consensus — leave |
| `brendan-rius/c-jwt-cracker` | 2561 | silent | JWT brute-force cracker — offensive leave |
| `kpcyrd/sn0int` | 2528 | silent | OSINT framework — not playbook product class |
| `Idov31/Nidhogg` | 2475 | silent | Windows rootkit demo — leave |
| `m0nad/Diamorphine` | 2454 | silent | Linux LKM rootkit — leave |
| `conorpp/u2f-zero` | 2449 | silent | Hardware U2F token firmware — hardware process |
| `solokeys/solo1` | 2381 | silent | Solo1 hardware firmware — hardware process |
| `jaeles-project/jaeles` | 2370 | silent | Automated web app testing / offensive knife — leave |
| `google/boringssl` | 2266 | silent | Gerrit + Google CLA workflow — GitHub not merge path |
| `RustCrypto/hashes` | 2264 | silent | Crypto hash primitives — maintainers hate drive-by algo changes |
| `risc0/risc0` | 2187 | silent | zkVM platform — heavy / novel ZK leave for early queue |
| `cloudflare/circl` | 1715 | silent | CIRCL crypto primitives — prefer TLS/PKI tooling over novel algos |
| `ZenGo-X/multi-party-ecdsa` | 1085 | silent | Threshold ECDSA MPC — novel crypto leave |

## Sector synthesis

- Midband (1k-5k) deep sample: **82** curated product repos.
- Proceed **52** / Leave **30**.
- Disclosure repos: `jdx/fnox`.
- No AgentScan adopter/org hits inside this midband sample (local blacklist checked). Re-run `--refresh` before any future fork.
- Method: policy files via `raw.githubusercontent.com` (CONTRIBUTING*/AI*/AGENTS*/PR templates/SECURITY); `gh api` workflows when needed; local AgentScan blacklist.
- No fork / PR / tracker comment performed.

## Deepen pass (2026-09-09, +40 scored)

Account: `vulragrag-star` · Curated product midband slice from remaining unscored `security-crypto-midband` raw (+ a few midband fills via `gh`) · Policy via `raw.githubusercontent.com` · **31** proceed / **9** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'disclosure': 2, 'silent': 38}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `greenbone/openvas-scanner` | 4816 | disclosure | OpenVAS scanner component; scan/config/path edges — disclose AI-assist per PR template | scan/config/path edge + Rust tests — disclose if agent-assisted |
| `aquasecurity/tracee` | 4612 | silent | Runtime security eBPF tracing toolkit; policy/event/path edges | eBPF policy/event/path edge + Go tests |
| `spiffe/spire` | 2522 | silent | SPIFFE runtime environment; workload identity/path edges | SPIFFE identity/path/config edge + Go tests |
| `rspamd/rspamd` | 2522 | silent | Fast spam filtering system; rule/config/path edges | rule/config/path edge + C tests |
| `authorizerdev/authorizer` | 1997 | silent | Open-source authN/Z service; OAuth/config/path edges | OAuth/config/path edge + Go tests |
| `pyupio/safety` | 1996 | silent | Python dependency vulnerability checker CLI; package/path edges | advisory/package/path edge + py tests |
| `cossacklabs/themis` | 1974 | silent | Crypto framework for data protection — config/API edges only | config/API edge + C tests — not novel algorithms |
| `dghubble/gologin` | 1959 | silent | Go OAuth1/OAuth2 login handlers; provider/callback edges | OAuth callback/config edge + Go tests |
| `moul/sshportal` | 1940 | silent | SSH/telnet bastion server; config/ACL/path edges | bastion ACL/config/path edge + Go tests |
| `aquasecurity/trivy-operator` | 1935 | silent | Kubernetes-native Trivy operator; CRD/config/path edges | operator CRD/config/path edge + Go tests |
| `openshift/osin` | 1935 | silent | Golang OAuth2 server library; grant/config edges | OAuth grant/config edge + Go tests |
| `BishopFox/jsluice` | 1912 | silent | Extract URLs/paths/secrets from JavaScript; parse/path edges | JS parse/secret/path edge + Go tests |
| `zema1/watchvuln` | 1894 | silent | High-value vulnerability feed collector/pusher; source/config edges | feed/source/config edge + Go tests |
| `justinas/nosurf` | 1751 | silent | CSRF protection middleware for Go; token/header edges | CSRF token/header edge + Go tests |
| `pkg/sftp` | 1664 | silent | SFTP support for go.crypto/ssh; path/protocol edges | SFTP path/protocol edge + Go tests |
| `rust-openssl/rust-openssl` | 1645 | silent | OpenSSL bindings for Rust — API/build edges only | FFI/API/build edge + Rust tests — not novel crypto |
| `drduh/pwd.sh` | 1563 | silent | Bash+GnuPG secrets manager; path/gpg edges | gpg/path/secret edge + shell tests |
| `occlum/occlum` | 1533 | silent | SGX library OS; config/path/seccomp edges | SGX config/path edge + Rust tests |
| `pass-extension/pass-otp` | 1494 | silent | pass OTP extension; URI/path edges | otpauth URI/path edge + shell tests |
| `cossacklabs/acra` | 1492 | silent | DB security suite / field-level encryption proxy; SQL/config edges | SQL/proxy/config edge + Go tests |
| `polhenarejos/pico-fido` | 1482 | silent | FIDO passkey firmware for Pico/ESP32; CTAP/config edges | CTAP/config edge + C tests — hardware care |
| `Shopify/ejson` | 1481 | silent | Asymmetric encrypted secrets library/CLI; key/path edges | encrypt/key/path edge + Go tests |
| `cyphar/paperback` | 1480 | silent | Paper backup generator for long-term secrets; encode/path edges | backup encode/path edge + Rust tests |
| `qpoint-io/qtap` | 1458 | silent | eBPF agent capturing pre-encrypted egress context; path/policy edges | eBPF policy/path edge + C tests |
| `eljojo/rememory` | 1447 | disclosure | Multi-key digital safe; crypto/path edges — AGENTS/CONTRIBUTING present | multi-key/path edge + Go tests — follow AGENTS disclosure |
| `aserto-dev/topaz` | 1361 | silent | Cloud-native authorization for apps/APIs; policy/path edges | authZ policy/path edge + Go tests |
| `sorah/envchain` | 1326 | silent | Env vars meet Keychain/gnome-keyring; path/keychain edges | keychain/path/env edge + C tests |
| `FiloSottile/passage` | 1188 | silent | password-store fork using age; path/age edges | age/path/store edge + shell tests |
| `mufeedvh/binserve` | 1127 | silent | Static web server with TLS/routing; config/path/TLS edges | TLS/config/path edge + Rust tests |
| `kunai-project/kunai` | 1085 | silent | Linux threat-hunting tool; event/rule/path edges | event/rule/path edge + Rust tests |
| `rpgp/rpgp` | 1066 | silent | Pure-Rust OpenPGP; parse/packet edges — not invent algorithms | OpenPGP packet/parse edge + Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `ComodoSecurity/openedr` | 2718 | silent | Vendor EDR dump — weak outsider hunk fit / unclear contrib culture |
| `jaksi/sshesame` | 1742 | silent | SSH honeypot — leave (honeypot class, not product tool farm) |
| `dwisiswant0/crlfuzz` | 1562 | silent | CRLF vulnerability fuzzer — offensive scanner class; leave |
| `tillson/git-hound` | 1455 | silent | Broad GitHub recon/secret hunter — noisy drive-by recon class; leave |
| `aquasecurity/trivy-action` | 1410 | silent | GitHub Action wrapper satellite of Trivy — prefer main product repos |
| `rest-sh/restish` | 1371 | silent | General REST CLI — better fits cli-systems; weak security-sector fit here |
| `honeytrap/honeytrap` | 1308 | silent | Honeypot framework — not playbook product CLI/path class; stale activity |
| `httpsok/httpsok` | 1302 | silent | One-liner SSL renew script niche — weak testable product surface |
| `JonasAlfredsson/docker-nginx-certbot` | 1203 | silent | Compose recipe for nginx+certbot — not a product codebase |

Notes: Prefer PKI/TLS/IAM/secrets/SAST/auth product surfaces with regression tests. Leave honeypots, GitHub Action satellites, compose recipes, and offensive recon/fuzzer kits. Config/API edges only on crypto libraries — never invent algorithms. `greenbone/openvas-scanner` and `eljojo/rememory` need disclosure trailers when agent-assisted.

## Product deepen midband subset (2026-09-10, +25 scored)

Account: `vulragrag-star` · Curated PKI/TLS/IAM/secrets/SBOM/SAST/access product homes still missing after midband · Policy via `raw.githubusercontent.com` · **15** proceed / **10** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 25}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `open-policy-agent/gatekeeper` | 4273 | silent | K8s admission policy; constraint/path edges | constraint/template/path edge + Go tests |
| `google/nsjail` | 4091 | silent | Process isolation; config/path edges | config/path edge + C++ tests |
| `hashicorp/boundary` | 4057 | silent | Identity-based access; target/path/session edges | target/path/session edge + Go tests |
| `panva/node-oidc-provider` | 3807 | silent | OIDC provider; client/route/config edges | OIDC client/route/config edge + JS tests |
| `FairwindsOps/goldilocks` | 3341 | silent | K8s resource right-sizing; config/path edges | config/path edge + Go tests |
| `jedisct1/minisign` | 2815 | silent | Simple file signing CLI; path/key edges | sign/verify path/key edge + C tests |
| `Checkmarx/kics` | 2699 | silent | IaC security scanner; query/path edges | query/path edge + Go tests |
| `supabase/auth` | 2557 | silent | JWT auth API; user/token/path edges | user/token/path edge + Go tests |
| `cedar-policy/cedar` | 1714 | silent | Cedar policy language; parse/eval edges | policy parse/eval edge + Rust tests |
| `ossf/allstar` | 1450 | silent | GitHub App security policy enforcer; policy/path edges | policy/path edge + Go tests |
| `deepfence/YaraHunter` | 1320 | silent | Malware scanner CI; yara/path edges | yara/path edge + Go tests |
| `pyca/pynacl` | 1205 | silent | PyNaCl bindings — API edges only | API bind/edge + py tests — not invent crypto |
| `sigstore/rekor` | 1204 | silent | Sigstore transparency log; entry/path edges | log entry/path edge + Go tests |
| `dalek-cryptography/curve25519-dalek` | 1192 | silent | Curve25519 group ops — API/test edges only | API/test edge + Rust tests — not invent crypto |
| `square/certigo` | 1034 | silent | Cert examine/validate CLI; PEM/path/SAN edges | PEM/path/SAN edge + Go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `auth0/express-jwt` | 4513 | silent | Tiny express JWT middleware — satellite surface |
| `osohq/oso` | 3489 | silent | Deprecated authZ library — do not open new work |
| `google/honggfuzz` | 3377 | silent | Fuzzer — specialized; weak path/quoting playbook class |
| `padloc/padloc` | 2920 | silent | Password manager with no CONTRIBUTING in common paths — weak process |
| `projectdiscovery/dnsx` | 2863 | silent | DNS toolkit — recon-adjacent; prefer nuclei/httpx |
| `WireGuard/wireguard-linux` | 1985 | silent | Kernel mirror only — not GitHub contribution home |
| `nginx/njs` | 1596 | silent | nginx JS subset satellite — prefer main product homes |
| `Vector35/binaryninja-api` | 1308 | silent | Binary Ninja API satellite — RE tooling; leave |
| `wolfi-dev/os` | 1286 | silent | Distro package dump — not a single product codebase for drive-by |
| `hashicorp/vault-helm` | 1259 | silent | Helm chart satellite of Vault — prefer hashicorp/vault product |

Notes: Prefer sealed-secrets/ESO/scorecard/casbin/cedar/gosec/rekor/nsjail/bubblewrap edges. Leave toxiproxy chaos, dnsx/katana recon-adjacent, vault-helm satellite, wolfi package dump, WireGuard kernel mirror, and deprecated oso.

## Midband product deepen (2026-09-11, +78 scored)

Account: `vulragrag-star` · Curated security-crypto midband (1k–5k★) PKI/TLS/IAM/secrets/SBOM/SAST/WAF/authZ/password/CT/sandbox homes still missing after prior security product deepen · Policy via `raw.githubusercontent.com` · **39** proceed / **39** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 73, 'disclosure': 5}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `intelowlproject/IntelOwl` | 4703 | silent | Threat intel platform; analyzer/config/path edges | analyzer/config/path edge + Python tests |
| `cerbos/cerbos` | 4577 | disclosure | AuthZ policy engine; policy/path edges — disclose AI | policy/path/eval edge + Go tests |
| `trifectatechfoundation/sudo-rs` | 4463 | disclosure | Memory-safe sudo/su; argv/policy edges — disclose AI | sudo argv/policy edge + Rust tests |
| `jtesta/ssh-audit` | 4299 | silent | SSH audit CLI; banner/kex/cipher edges | SSH audit/parse edge + Python tests |
| `DependencyTrack/dependency-track` | 4195 | silent | SBOM/SCA platform; component/vuln/path edges | SBOM/component/path edge + Java tests |
| `RetireJS/retire.js` | 4170 | silent | JS dependency vuln scanner; path/repo edges | dep/path scan edge + JS tests |
| `briansmith/ring` | 4106 | silent | Crypto primitives — API/test edges only, never invent algos | API/test edge + Rust tests — not invent crypto |
| `cartography-cncf/cartography` | 4051 | disclosure | Infra asset graph; connector/path edges — disclose AI | connector/path edge + Python tests |
| `spotbugs/spotbugs` | 3940 | silent | Java SAST; detector/bug-pattern edges | detector/pattern edge + Java tests |
| `corazawaf/coraza` | 3792 | silent | OWASP Coraza WAF; rule/config/path edges | WAF rule/config/path edge + Go tests |
| `Neo23x0/Loki` | 3789 | silent | IOC/YARA scanner; rule/path edges | yara/IOC/path edge + Python tests |
| `aquasecurity/cloudsploit` | 3775 | silent | CSPM scanner; plugin/cloud/path edges | CSPM plugin/path edge + JS tests |
| `allinssl/allinssl` | 3586 | silent | SSL cert lifecycle tool; domain/path/deploy edges | cert deploy/path edge + Go tests |
| `iann0036/iamlive` | 3408 | silent | IAM policy generator from cloud activity; policy/path edges | IAM policy/path edge + Go tests |
| `Yamato-Security/hayabusa` | 3336 | silent | Sigma threat-hunting CLI; rule/path edges | sigma/rule/path edge + Rust tests |
| `django-oauth/django-oauth-toolkit` | 3335 | silent | Django OAuth2 provider; app/token/path edges | OAuth app/token/path edge + Django tests |
| `Mic92/sops-nix` | 3157 | silent | NixOS sops secrets; secret/path edges | sops/nix secret/path edge + Nix tests |
| `aliasvault/aliasvault` | 3104 | silent | Privacy-first password manager; vault/path edges | vault/path/email-alias edge + tests |
| `oauthlib/oauthlib` | 2980 | silent | OAuth lib; grant/token/parse edges | OAuth grant/token edge + Python tests |
| `opencve/opencve` | 2826 | silent | Vuln intelligence platform; CVE/feed/path edges | CVE/feed/path edge + Python tests |
| `authpass/authpass` | 2787 | silent | Flutter password manager; entry/path/import edges | entry/path/import edge + Dart tests |
| `awnumar/memguard` | 2758 | silent | Sensitive memory sandbox; alloc/lock edges | memguard alloc/lock edge + Go tests |
| `coreos/go-oidc` | 2475 | silent | Go OIDC client; discovery/verify edges | OIDC discovery/verify edge + Go tests |
| `find-sec-bugs/find-sec-bugs` | 2443 | silent | FindSecBugs SpotBugs plugin; detector edges | detector/pattern edge + Java tests |
| `panva/openid-client` | 2407 | silent | OIDC client; discovery/token/path edges | OIDC discovery/token edge + JS tests |
| `unrolled/secure` | 2355 | silent | Go secure headers middleware; header/config edges | secure header/config edge + Go tests |
| `MasterKale/SimpleWebAuthn` | 2341 | silent | WebAuthn library; ceremony/option edges | WebAuthn ceremony/option edge + TS tests |
| `keepassxreboot/keepassxc-browser` | 2327 | disclosure | KeePassXC browser bridge; native-msg/path edges — disclose AI | native messaging/path edge + JS tests |
| `thoughtworks/talisman` | 2098 | silent | Secrets pre-commit scanner; pattern/path edges | secret pattern/path edge + Go tests |
| `theupdateframework/python-tuf` | 1726 | silent | TUF Python reference; metadata/path edges | TUF metadata/path edge + Python tests |
| `FairwindsOps/rbac-manager` | 1667 | silent | K8s RBAC operator; role/path edges | RBAC role/path edge + Go tests |
| `controlplaneio/kubesec` | 1479 | silent | K8s manifest risk analysis; path/score edges | manifest/path/score edge + Go tests |
| `neuvector/neuvector` | 1334 | silent | Container security platform; policy/path edges | policy/path edge + Go tests |
| `zalando/go-keyring` | 1329 | silent | OS keyring helper; service/user/path edges | keyring service/path edge + Go tests |
| `stackrox/stackrox` | 1309 | disclosure | K8s security platform; policy/path edges — disclose AI | policy/path edge + Go tests |
| `gorilla/csrf` | 1210 | silent | Go CSRF middleware; token/header edges | CSRF token/header edge + Go tests |
| `Yubico/yubikey-manager` | 1186 | silent | YubiKey CLI/library; config/path edges | YubiKey config/path edge + Python tests |
| `SSLMate/certspotter` | 1173 | silent | CT log monitor; log/path edges | CT log/path edge + Go tests |
| `simplesamlphp/simplesamlphp` | 1140 | silent | SAML IdP/SP; config/metadata/path edges | SAML metadata/config edge + PHP tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `netlify/gotrue` | 4476 | silent | Supabase/Netlify GoTrue — often satellite of larger auth platforms; process unclear here |
| `jazzband/djangorestframework-simplejwt` | 4333 | silent | DRF JWT helper — thin library; prefer IdP/OIDC homes |
| `aarondl/authboss` | 4197 | silent | Go auth toolkit with weak CONTRIBUTING surface |
| `simov/grant` | 4168 | silent | Generic OAuth proxy middleware — prefer dedicated IdP/OIDC homes |
| `thephpleague/oauth2-client` | 3821 | silent | PHP OAuth client satellite — prefer IdP/OIDC product homes |
| `maxcountryman/flask-login` | 3675 | silent | Tiny Flask session helper — prefer authlib/allauth class |
| `JosephSilber/bouncer` | 3580 | silent | Laravel abilities package — app-framework satellite |
| `lynndylanhurley/devise_token_auth` | 3569 | silent | Rails token auth add-on — prefer main devise/IdP homes |
| `jaredhanson/oauth2orize` | 3534 | silent | Legacy Node OAuth2 toolkit — stale/process unclear |
| `ueberauth/guardian` | 3514 | silent | Elixir token lib — niche; prefer broader auth platforms |
| `laravel/passport` | 3417 | silent | Laravel OAuth server plugin — framework satellite |
| `auth0/jwt-decode` | 3399 | silent | Tiny JWT decode helper — satellite surface |
| `OAuthSwift/OAuthSwift` | 3331 | silent | iOS OAuth helper — mobile satellite surface |
| `workos/authkit` | 3329 | silent | Auth UI kit / login box — weak systems product hunk fit |
| `chromium/badssl.com` | 3047 | silent | TLS test content site — not a product codebase for drive-by patches |
| `appleboy/gin-jwt` | 2974 | silent | Thin Gin JWT middleware — satellite; prefer product auth homes |
| `apache/casbin-node-casbin` | 2915 | silent | Casbin Node binding satellite — prefer main casbin |
| `rs/cors` | 2898 | silent | Tiny CORS middleware — prefer fuller security product homes |
| `omab/python-social-auth` | 2801 | silent | Legacy meta-package — prefer social-app-django / maintained forks |
| `sunscrapers/djoser` | 2678 | silent | Django REST auth helper — prefer allauth/simplejwt/IdP |
| `apache/casbin-jcasbin` | 2652 | silent | Casbin Java binding satellite — prefer main casbin |
| `lexik/LexikJWTAuthenticationBundle` | 2609 | silent | Symfony JWT bundle satellite |
| `jwt-dotnet/jwt` | 2191 | silent | Thin .NET JWT helper — weak outsider hunk surface |
| `ruby-oauth/oauth2` | 2179 | silent | Thin Ruby OAuth2 gem — prefer fuller IdP/OIDC homes |
| `zmap/zgrab2` | 2174 | silent | Internet-wide banner scanner — recon-adjacent optics; leave |
| `python-social-auth/social-app-django` | 2144 | silent | Social-auth Django adapter — prefer django-allauth |
| `authts/oidc-client-ts` | 1948 | silent | Browser OIDC client — frontend satellite; prefer server auth homes |
| `spiffe/spiffe` | 1851 | silent | SPIFFE specs/docs home — not a single product implementation |
| `apache/casbin-pycasbin` | 1767 | silent | Casbin language binding satellite — prefer apache/casbin main |
| `keepassium/KeePassium` | 1689 | silent | iOS KeePass client — mobile App Store surface; weak CI outsider fit |
| `projectdiscovery/notify` | 1611 | silent | Generic notify CLI — weak security-sector product fit |
| `simonrob/email-oauth2-proxy` | 1470 | silent | Niche email OAuth proxy — weak testable product farm |
| `passwordless-lib/fido2-net-lib` | 1451 | silent | .NET FIDO2 lib — niche binding; prefer broader WebAuthn homes |
| `lepture/flask-oauthlib` | 1446 | silent | Stale Flask OAuth helper — prefer authlib |
| `php-casbin/php-casbin` | 1337 | silent | Casbin PHP binding satellite — prefer main casbin |
| `apache/casbin-Casbin.NET` | 1334 | silent | Casbin .NET binding satellite — prefer main casbin |
| `waiting-for-dev/devise-jwt` | 1291 | silent | Thin Devise JWT add-on — prefer main auth product homes |
| `damienbod/angular-auth-oidc-client` | 1238 | silent | Angular OIDC client — frontend satellite |
| `auth0/go-jwt-middleware` | 1205 | silent | Thin Go JWT middleware satellite of Auth0 samples |

Notes: Prefer midband PKI/TLS/IAM/secrets/SBOM/SAST/WAF/authZ homes (fail2ban/boulder/secretive/cerbos/keto/opal/coraza/dependency-track/hayabusa/kubesec/sops-nix/sudo-rs/git-secrets/talisman/certspotter/testssl/memguard/SimpleWebAuthn). Disclosure: keto/cerbos/sudo-rs/cartography/keepassxc-browser/stackrox. Leave Casbin language bindings, thin JWT middleware, frontend OIDC clients, badssl content site, SPIFFE specs-only, recon scanners (zgrab2), and framework auth satellites.

## Midband product deepen-2 (2026-09-12, +60 scored)

Account: `vulragrag-star` · Curated security-crypto midband (1k–5k★) IAM/secrets/PKI/SAST/CSPM/runtime/firewall leftovers after prior security product deepens · Policy via `raw.githubusercontent.com` · **50** proceed / **10** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 56, 'disclosure': 3, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `DefectDojo/django-DefectDojo` | 4936 | silent | Vuln management platform; finding/import/path edges | finding import/path edge + Django tests |
| `anonaddy/anonaddy` | 4837 | silent | Anonymous email forwarding; alias/domain/path edges | alias/domain/path edge + PHP tests |
| `HotCakeX/Harden-Windows-Security` | 4734 | silent | Windows hardening toolkit; policy/path edges | hardening policy/path edge + tests |
| `emanuele-f/PCAPdroid` | 4707 | silent | Android firewall/PCAP monitor; rule/path edges | firewall rule/path edge + Android tests |
| `opnsense/core` | 4684 | disclosure | OPNsense firewall core; config/API/path edges — disclose AI | config/API/path edge + tests |
| `Authenticator-Extension/Authenticator` | 4666 | silent | Browser 2FA authenticator; account/otp/path edges | OTP account/path edge + TS tests |
| `stratumauth/app` | 4576 | silent | Mobile 2FA client; entry/otp/path edges | OTP entry/path edge + tests |
| `intuitem/ciso-assistant-community` | 4414 | silent | GRC/risk platform; assessment/policy/path edges | assessment/policy/path edge + Python tests |
| `Bubka/2FAuth` | 4148 | silent | Self-hosted 2FA manager; account/otp/path edges | OTP account/path edge + PHP tests |
| `WithSecureOpenSource/chainsaw` | 3659 | silent | Windows forensic hunt CLI; rule/path edges | sigma/hunt path edge + Rust tests |
| `tnodir/fort` | 3547 | silent | Windows Fort Firewall; rule/path edges | firewall rule/path edge + C++ tests |
| `ukanth/afwall` | 3472 | silent | Android iptables firewall; rule/path edges | iptables rule/path edge + Java tests |
| `pglombardo/PasswordPusher` | 3192 | silent | Secure secret sharing; expire/path edges | push expire/path edge + Ruby tests |
| `ChatSecure/ChatSecure-iOS` | 3152 | silent | Encrypted chat client; account/crypto/path edges | XMPP/crypto path edge + iOS tests |
| `ulisesbocchio/jasypt-spring-boot` | 3087 | silent | Spring Boot Jasypt encryption; property/path edges | property encrypt/path edge + Java tests |
| `bcgit/bc-java` | 2689 | silent | Bouncy Castle Java crypto — API/test edges only, never invent algos | API/test edge + Java tests — not invent crypto |
| `segmentio/chamber` | 2615 | silent | Secrets CLI for AWS SSM; path/param edges | SSM param/path edge + Go tests |
| `open-keychain/open-keychain` | 2615 | silent | Android OpenPGP; key/path edges | OpenPGP key/path edge + Android tests |
| `kubearmor/KubeArmor` | 2610 | silent | K8s runtime security enforcement; policy/path edges | policy/path edge + Go tests |
| `ajinabraham/nodejsscan` | 2573 | silent | Node.js SAST scanner; rule/path edges | SAST rule/path edge + Python tests |
| `pac4j/pac4j` | 2523 | silent | Java security engine; authn/authz/path edges | authn/authz/path edge + Java tests |
| `Peergos/Peergos` | 2515 | silent | P2P encrypted storage; path/crypto edges | storage/crypto path edge + Java tests |
| `RevylAI/greenlight` | 2426 | silent | App Store compliance scanner; check/path edges | compliance check/path edge + Go tests |
| `lihenggui/blocker` | 2392 | silent | Android app firewall; rule/path edges | firewall rule/path edge + Kotlin tests |
| `yeojz/otplib` | 2291 | disclosure | OTP/2FA library; secret/algorithm edges — disclose AI | OTP secret/algo edge + TS tests |
| `bank-vaults/bank-vaults` | 2271 | silent | Vault CLI/operator helper; unseal/config/path edges | vault unseal/config path edge + Go tests |
| `ory/polis` | 2263 | disclosure | Auth streaming/proxy; config/path edges — disclose AI | auth config/path edge + TS tests |
| `salesforce/cloudsplaining` | 2247 | silent | AWS IAM assessment; policy/path edges | IAM policy/path edge + Python tests |
| `Versent/saml2aws` | 2245 | silent | SAML CLI for cloud creds; provider/path edges | SAML provider/path edge + Go tests |
| `greenpau/caddy-security` | 2234 | silent | Caddy AAA plugin; authn/authz/path edges | AAA config/path edge + Go tests |
| `ranisalt/node-argon2` | 2183 | silent | Argon2 Node bindings; hash/param edges | argon2 param/hash edge + JS tests |
| `hannob/snallygaster` | 2112 | silent | HTTP secret-file scanner; path/probe edges | HTTP path/probe edge + Python tests |
| `hlandau/acmetool` | 2092 | silent | ACME certificate tool; order/path edges | ACME order/path edge + Go tests |
| `someengineering/fixinventory` | 2077 | silent | Cloud inventory/cost security; resource/path edges | inventory resource/path edge + Python tests |
| `authgear/authgear-server` | 2045 | silent | Auth0-class identity server; OIDC/path edges | OIDC/path edge + Go tests |
| `opsre/go-ldap-admin` | 2019 | silent | OpenLDAP admin UI/API; entry/path edges | LDAP entry/path edge + Go tests |
| `antonioribeiro/google2fa` | 2008 | silent | PHP TOTP package; secret/window edges | TOTP secret/window edge + PHP tests |
| `dromara/MaxKey` | 1949 | silent | IAM/IDaaS SSO; app/path edges | SSO app/path edge + Java tests |
| `betterleaks/betterleaks` | 1874 | silent | Secret leak finder CLI; pattern/path edges | secret pattern/path edge + Go tests |
| `lirantal/npq` | 1793 | silent | npm pre-install audit CLI; package/path edges | package audit/path edge + JS tests |
| `alienator88/Sentinel` | 1748 | silent | macOS Gatekeeper helper; quarantine/path edges | Gatekeeper path edge + Swift tests |
| `webprofusion/certify` | 1703 | silent | Windows ACME client; cert/path edges | ACME cert/path edge + C# tests |
| `matanolabs/matano` | 1696 | silent | Security data lake; detection/path edges | detection/path edge + Rust tests |
| `emberstack/kubernetes-reflector` | 1673 | silent | K8s secret/config reflector; mirror/path edges | reflect/path edge + C# tests |
| `scito/extract_otp_secrets` | 1655 | silent | OTP secret extractor CLI; QR/path edges | OTP QR/path edge + Python tests |
| `chaitin/veinmind-tools` | 1652 | silent | Container security toolset; scan/path edges | container scan/path edge + Go tests |
| `mssun/passforios` | 1644 | silent | Pass password-store iOS client; entry/path edges | pass entry/path edge + Swift tests |
| `ankane/lockbox` | 1609 | silent | Ruby/Rails encryption; field/path edges | encrypt field/path edge + Ruby tests |
| `freeipa/freeipa` | 1278 | silent | Integrated identity (LDAP/Kerberos/PKI); install/path edges — small hunks only | IPA install/path edge + Python tests |
| `DataDog/guarddog` | 1204 | silent | Malicious package CLI scanner; ecosystem/path edges | package scan/path edge + Python tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `osixia/container-openldap` | 4228 | silent | Container image packaging only — leave packaging satellites |
| `Neo23x0/signature-base` | 3027 | silent | YARA/IOC signature database dump — not product hunk class |
| `cryfs/cryfs` | 2305 | hard_ban | AI_POLICY NO-AI — hard leave |
| `slsa-framework/slsa` | 1927 | silent | SLSA levels spec/docs repo — not product CLI/library |
| `lavabit/magma` | 1830 | silent | Encrypted email server daemon mega — poor drive-by surface |
| `ammarahm-ed/react-native-mmkv-storage` | 1751 | silent | RN MMKV storage lib — mobile KV spill, not security product farm |
| `mprimi/portable-secret` | 1735 | silent | HTML novelty secret page — not product contribution target |
| `AltraMayor/gatekeeper` | 1638 | silent | DDoS protection system — networking/DDoS mega; leave for networking sector or too heavy |
| `mazen160/secrets-patterns-db` | 1617 | silent | Secrets patterns database — content dump, not product |
| `w3c/webauthn` | 1456 | silent | W3C WebAuthn specification — specs-only, not product code |

Notes: Prefer midband security product homes (vuln mgmt/GRC, IAM/SSO/OIDC, OTP/2FA, secrets CLIs/sharing, ACME/PKI, SAST/CSPM, runtime K8s policy, host firewall/hardening, OpenPGP/crypto libs with testable API edges). Leave hard_ban cryfs, specs-only (w3c/webauthn, slsa docs), signature/pattern DBs, HTML novelty secrets, RN MMKV spill, DDoS megas, email-server megas, packaging-only LDAP images.

## Midband product deepen-3 (2026-09-14, +110 scored)

Account: `vulragrag-star` · Curated security-crypto midband TS/JS (1k–5k★) leftover PKI/TLS/IAM/secrets/SBOM/SAST/WAF/authZ/OTP/crypto homes after security-crypto deepen-2 and other sector deepen-3s · Policy via `raw.githubusercontent.com` · **50** proceed / **60** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 102, 'disclosure': 7, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `MrSwitch/hello.js` | 4619 | silent | OAuth social-login client library product | hello.js OAuth provider path edge + tests |
| `oauthjs/node-oauth2-server` | 4063 | silent | Compliant OAuth 2.0 authorization server product for Node | OAuth2 grant/token/path edge + Node tests |
| `eth0izzle/shhgit` | 3982 | silent | Secrets-in-code detection CLI product | secret pattern/path edge + scanner tests |
| `KuroLabs/stegcloak` | 3891 | silent | Steganography secret-hiding CLI product | stego hide/reveal path edge + tests |
| `dcodeIO/bcrypt.js` | 3797 | silent | Pure-JS bcrypt password hashing crypto library | bcrypt hash/salt edge + crypto tests |
| `shuaiplus/nodewarden` | 3658 | silent | Bitwarden-compatible secrets vault on Workers | vault cipher/sync path edge + tests |
| `henryboldi/felony` | 3458 | silent | Desktop PGP encryption product | PGP key/encrypt path edge + tests |
| `express-rate-limit/express-rate-limit` | 3305 | silent | Express rate-limiting security middleware product | rate-limit window/key edge + tests |
| `easychen/CookieCloud` | 3152 | silent | E2E-encrypted browser cookie sync product | cookie sync encrypt/path edge + tests |
| `jpillora/xdomain` | 3146 | silent | Cross-domain CORS alternative security library | xdomain postMessage/CORS edge + tests |
| `ExpressGateway/express-gateway` | 3030 | silent | Express microservices API Gateway with auth plugins | gateway auth/plugin path edge + tests |
| `pyllyukko/user.js` | 2893 | silent | Firefox configuration hardening product | hardening pref/path edge + tests |
| `chibisafe/chibisafe` | 2771 | silent | Blazing-fast TypeScript file vault product | file vault upload/path edge + tests |
| `jaredhanson/passport-local` | 2754 | silent | Passport local username/password strategy product | Passport local auth path edge + tests |
| `ciaranj/node-oauth` | 2432 | silent | Node.js OAuth 1.0/2.0 wrapper library product | node-oauth token/path edge + tests |
| `onury/accesscontrol` | 2329 | silent | Role/attribute-based access control (RBAC/ABAC) library | RBAC grant/deny path edge + tests |
| `Caligatio/jsSHA` | 2264 | silent | Complete SHA family hash crypto library (JS/TS) | hash algorithm/path edge + tests |
| `sergiodxa/remix-auth` | 2201 | silent | Remix authentication framework product | auth strategy/session path edge + tests |
| `mikenicholson/passport-jwt` | 1981 | silent | Passport JWT authentication strategy product | JWT strategy/verify path edge + tests |
| `dchest/tweetnacl-js` | 1923 | silent | TweetNaCl cryptographic library port to JavaScript | NaCl box/sign path edge + crypto tests |
| `cloudflare/workers-oauth-provider` | 1870 | silent | OAuth provider library for Cloudflare Workers | OAuth provider token/path edge + tests |
| `mailvelope/mailvelope` | 1842 | silent | Browser OpenPGP encryption for webmail product | OpenPGP encrypt/key path edge + tests |
| `intika/Librefox` | 1778 | silent | Firefox privacy/hardening enhancement product | privacy pref/hardening path edge + tests |
| `Noovolari/leapp` | 1774 | silent | Cloud IAM access DevTool / credential session CLI | IAM session/credential path edge + tests |
| `indutny/elliptic` | 1765 | silent | Fast elliptic-curve cryptography library in JS | ECC curve/sign path edge + crypto tests |
| `clerk/javascript` | 1755 | silent | Clerk authentication JS/TS monorepo product | Clerk auth SDK/session path edge + tests |
| `googleworkspace/apps-script-oauth2` | 1747 | silent | OAuth2 library for Google Apps Script | OAuth2 token/refresh path edge + tests |
| `pilcrowonpaper/arctic` | 1717 | silent | OAuth 2.0 clients for popular identity providers | OAuth client provider/path edge + tests |
| `forwardemail/forwardemail.net` | 1671 | silent | Privacy-focused encrypted email product | email encrypt/TLS path edge + tests |
| `holtwick/briefing` | 1627 | silent | Secure direct video group-chat product | WebRTC secure-chat path edge + tests |
| `SpiderOak/Encryptr` | 1559 | silent | Zero-knowledge cloud password manager product | password vault/crypto path edge + tests |
| `sidebase/nuxt-auth` | 1551 | silent | Nuxt authentication product (Auth.js adapter) | Nuxt auth session/provider path edge + tests |
| `ssoready/ssoready` | 1535 | silent | Enterprise SSO (SAML + SCIM) developer tooling product | SAML/SCIM SSO path edge + tests |
| `oauth-io/oauthd` | 1520 | silent | OAuth Daemon open-source OAuth provider product | OAuth daemon provider/path edge + tests |
| `traceless/alist-encrypt` | 1504 | silent | AList WebDAV encryption proxy product | WebDAV encrypt/path edge + tests |
| `accounts-js/accounts` | 1502 | silent | Fullstack authentication and accounts-management product | accounts auth/session path edge + tests |
| `robinkarlberg/transfer.zip-web` | 1499 | silent | Self-hostable encrypted file-sharing product | file-share encrypt/path edge + tests |
| `hectorm/otpauth` | 1476 | silent | HOTP/TOTP one-time password library product | OTP generate/verify path edge + tests |
| `tilfinltd/aws-extend-switch-roles` | 1429 | silent | AWS IAM role-switch browser extension product | IAM role-switch path edge + tests |
| `Tygs/0bin` | 1404 | silent | Client-side encrypted pastebin product | paste encrypt/expire path edge + tests |
| `PeculiarVentures/PKI.js` | 1399 | silent | Pure JS PKI formats/X.509/CMS crypto library | PKI ASN.1/X.509 path edge + tests |
| `Authing/Guard` | 1361 | silent | Authing SSO login widget / Guard product | SSO widget/login path edge + tests |
| `davewasmer/devcert` | 1308 | silent | Local HTTPS / trusted cert development product | devcert CA/path edge + TLS tests |
| `jaredhanson/passport-facebook` | 1307 | silent | Passport Facebook OAuth authentication strategy | Passport Facebook OAuth path edge + tests |
| `step-security/harden-runner` | 1268 | silent | CI/CD harden-runner security agent product | CI harden policy/path edge + tests |
| `dotenv-org/dotenv-vault` | 1245 | silent | dotenv-vault secrets sync product | dotenv vault sync/path edge + tests |
| `HemmeligOrg/Hemmelig.app` | 1243 | silent | Self-hosted sensitive-secret sharing product | secret share/expire path edge + tests |
| `nhost/hasura-backend-plus` | 1169 | silent | Hasura Auth + Storage backend product | Hasura auth/storage path edge + tests |
| `auth0/auth0.js` | 1059 | silent | Auth0 headless browser authentication SDK | Auth0 SDK login/token path edge + tests |
| `openid/AppAuth-JS` | 1014 | silent | AppAuth OAuth 2.0 / OIDC JS client SDK product | AppAuth OIDC flow/path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `SadeghHayeri/GreenTunnel` | 4909 | silent | Anti-censorship / VPN circumvention utility — leave |
| `darrenhinde/OpenAgentsControl` | 4842 | silent | AI agent framework — agent kit leave |
| `paulmillr/encrypted-dns` | 4800 | silent | DoH config profiles — networking/config dump leave |
| `Mathieu2301/TradingView-API` | 4769 | silent | TradingView stocks API — wrong sector |
| `async-labs/saas` | 4511 | silent | SaaS boilerplate — template leave |
| `dmno-dev/varlock` | 4392 | disclosure | Disclosure AI-policy AGENTS.md — leave |
| `bookorbit/bookorbit` | 4304 | hard_ban | NO-AI phrase in PR template — hard leave |
| `XiaoDuoYa/codex-with-chatgpt` | 4265 | silent | ChatGPT/Codex AI agent kit — leave |
| `dwyl/learn-json-web-tokens` | 4173 | silent | JWT tutorial/learn repo — leave |
| `buqiyuan/vue3-antdv-admin` | 4110 | silent | Admin panel UI framework — leave |
| `nextauthjs/next-auth-example` | 4030 | silent | NextAuth example app — leave |
| `gildas-lormeau/zip.js` | 3892 | silent | Zip library — not security-crypto product home |
| `async-labs/builderbook` | 3792 | silent | Learn JS stack tutorial app — leave |
| `Haehnchen/crypto-trading-bot` | 3523 | silent | Crypto trading bot — wrong sector |
| `onecli/onecli` | 3478 | silent | Sandboxed AI agent harness — agent kit leave |
| `duolahypercho/codex-router` | 3447 | silent | Codex AI model router — agent kit leave |
| `AdventDevInc/kudu` | 3436 | silent | Desktop cleaner/scanner utility — not security product farm |
| `pashpashpash/vault-ai` | 3391 | silent | ChatGPT vault memory — AI kit leave |
| `cyu/rack-cors` | 3289 | silent | Rack CORS middleware (Ruby) — thin CORS / wrong-lang leave |
| `cool-team-official/cool-admin-midway` | 3272 | silent | AI admin framework — web app leave |
| `nexu-io/nexu` | 3270 | silent | OpenClaw desktop client — agent kit leave |
| `guilhermerodz/input-otp` | 3255 | silent | Unstyled OTP input UI component — thin frontend leave |
| `chaterm/Chaterm` | 3076 | silent | AI terminal for infra — agent/CLI spill leave |
| `afteracademy/nodejs-backend-architecture-typescript` | 3072 | silent | Learn/architecture tutorial — leave |
| `jeremykenedy/laravel-auth` | 3043 | silent | Laravel auth boilerplate — template leave |
| `zenstackhq/zenstack` | 2942 | silent | TypeScript ORM/data layer — databases spill |
| `coddingtonbear/obsidian-local-rest-api` | 2921 | disclosure | Disclosure AI-policy + Obsidian/MCP spill — leave |
| `voidauth/voidauth` | 2818 | disclosure | Disclosure CONTRIBUTING AI-policy — leave (SSO product otherwise) |
| `SabakiHQ/Sabaki` | 2775 | silent | Go board / SGF editor game — leave |
| `auth0/angular2-jwt` | 2623 | silent | Thin Angular JWT helper — thin JWT middleware leave |
| `huanghanzhilian/c-shopping` | 2422 | silent | Ecommerce shopping platform — web app leave |
| `jbilcke-hf/clapper` | 2326 | silent | Video synthesizer app — wrong sector |
| `staylor/react-helmet-async` | 2297 | silent | React Helmet UI helper — thin frontend leave |
| `manfredsteyer/angular-oauth2-oidc` | 1984 | silent | Frontend Angular OIDC client — frontend OIDC leave |
| `FoalTS/foal` | 1935 | silent | Full Node web framework — not security product home |
| `sbwml/luci-app-mosdns` | 1829 | silent | OpenWrt DNS forwarder Luci app — networking spill |
| `LibPDF-js/core` | 1823 | disclosure | Disclosure CONTRIBUTING + PDF lib wrong-sector — leave |
| `xyzeva/k-id-age-verifier` | 1725 | silent | Age-verification automation — leave |
| `panshak/accountill` | 1694 | silent | Invoicing web app — wrong sector |
| `bitbonsai/mcpvault` | 1663 | silent | MCP agent secrets server — agent kit leave |
| `node-opcua/node-opcua` | 1659 | disclosure | Disclosure AI-policy + industrial OPC UA spill — leave |
| `NopeCHALLC/nopecha-nodejs` | 1447 | silent | Automated CAPTCHA solver — leave |
| `PrismarineJS/node-minecraft-protocol` | 1414 | silent | Minecraft protocol — game leave |
| `styled-components/vue-styled-components` | 1377 | silent | CSS-in-JS styled-components port — leave |
| `hokaccha/node-jwt-simple` | 1355 | silent | Thin JWT encode/decode module — thin JWT leave |
| `koajs/jwt` | 1349 | silent | Thin Koa JWT middleware — thin JWT leave |
| `SteveSuv/remix-words-funny` | 1344 | silent | English learning website — web app leave |
| `MomenSherif/react-oauth` | 1337 | silent | Frontend React Google OAuth — frontend OIDC leave |
| `hadynz/obsidian-kindle-plugin` | 1281 | disclosure | Disclosure + Obsidian plugin spill — leave |
| `Jose-Gael-Cruz-Lopez/underclassmen-opportunities` | 1278 | silent | Curated opportunities list — leave |
| `helloyanis/age-verification-bypass` | 1271 | silent | Age-verification bypass extension — leave |
| `sakurity/securelogin` | 1207 | silent | Repo moved / abandoned securelogin — leave |
| `bramses/bramses-highly-opinionated-vault-2023` | 1199 | silent | Obsidian vault config dump — leave |
| `wireapp/wire-webapp` | 1192 | silent | Wire chat mega web client — leave |
| `juliusmarminge/acme-corp` | 1175 | silent | Demo/corp template repo — leave |
| `burakorkmez/mern-chat-app` | 1102 | silent | MERN chat app with JWT — generic web app leave |
| `epicweb-dev/cachified` | 1059 | silent | Cache wrapper library — not security product |
| `stravo1/obsidian-gdrive-sync` | 1045 | silent | Obsidian Google Drive sync plugin — leave |
| `chrisgrieser/shimmering-obsidian` | 1038 | disclosure | Disclosure + Obsidian Alfred workflow spill — leave |
| `aidenlx/zotlit` | 1017 | silent | Obsidian Zotero plugin — leave |

Notes: Prefer midband TS/JS security-crypto product homes (PKI/TLS/ACME, IAM/SSO/OTP, secrets managers, SBOM/SAST/SCA, WAF/authZ, host firewall/hardening, OpenPGP/crypto libs). Leave offensive scanners/crackers, RE frameworks, VPN/censorship tools, thin JWT middleware, frontend OIDC clients, specs-only, agent kits, generic web apps, Obsidian spills, disclosure/hard_ban.

## Midband product deepen-4 (2026-09-14, +125 scored)

Account: `vulragrag-star` · Curated security-crypto midband (1k–5k★) leftover TS/JS+Go/Rust/Python PKI/TLS/IAM/secrets/SBOM/SAST/WAF/authZ/OTP/crypto homes after security-crypto deepen-3 and other sector deepen-3s · Policy via `raw.githubusercontent.com` · **49** proceed / **76** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 123, 'disclosure': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `hardentools/hardentools` | 3110 | silent | Windows attack-surface hardening security tool | hardening toggle/path edge + tests |
| `joestump/python-oauth2` | 3008 | silent | Python OAuth client library product | OAuth client signature/path edge + tests |
| `pquerna/otp` | 2956 | silent | Go TOTP/HOTP one-time password crypto library | TOTP/HOTP code/window edge + Go tests |
| `refraction-networking/utls` | 2572 | silent | Low-level Go TLS library with fingerprint control | TLS handshake/cipher path edge + tests |
| `int128/kubelogin` | 2354 | silent | kubectl plugin for Kubernetes OIDC authentication | OIDC login/token path edge + tests |
| `sh-dv/hat.sh` | 2284 | silent | Browser file encrypt/decrypt security product | file encrypt/key path edge + tests |
| `ghostunnel/ghostunnel` | 2198 | silent | TLS proxy with mutual authentication product | mTLS proxy/cert path edge + tests |
| `vgough/encfs` | 2164 | silent | Encrypted FUSE filesystem crypto product | EncFS mount/cipher path edge + tests |
| `RichardKnop/go-oauth2-server` | 2149 | silent | Spec-compliant standalone OAuth2 server (Go) | OAuth2 grant/token path edge + tests |
| `Keats/jsonwebtoken` | 2089 | silent | Rust JWT encode/decode crypto library | JWT claim/alg path edge + Rust tests |
| `mkhorasani/Streamlit-Authenticator` | 2084 | silent | Streamlit secure authentication module | auth session/password path edge + tests |
| `openpubkey/opkssh` | 2061 | silent | OpenPubkey SSH authentication product | SSH pubkey/OIDC path edge + tests |
| `nuxt-community/auth-module` | 1924 | silent | Nuxt 2 authentication module product | auth strategy/session path edge + tests |
| `iMerica/dj-rest-auth` | 1869 | silent | Django REST Framework authentication product | auth session/token path edge + tests |
| `wallarm/gotestwaf` | 1804 | silent | API security / WAF assessment toolkit (Go) | WAF bypass/detection path edge + tests |
| `cs01/termpair` | 1778 | silent | Browser terminal sharing with E2E encryption | E2E terminal crypto path edge + tests |
| `krakenjs/lusca` | 1774 | silent | Express application security middleware product | CSP/CSRF/XSS header path edge + tests |
| `etesync/server` | 1771 | silent | Etebase E2E encrypted sync server product | E2E sync/crypto path edge + tests |
| `mpdavis/python-jose` | 1757 | silent | Python JOSE/JWT/JWE/JWS implementation | JOSE header/alg path edge + tests |
| `mikespook/gorbac` | 1676 | silent | Lightweight Go RBAC authorization library | RBAC grant/deny path edge + tests |
| `zama-ai/tfhe-rs` | 1662 | silent | Pure Rust TFHE fully-homomorphic encryption lib | FHE encrypt/bootstrap path edge + tests |
| `lelylan/simple-oauth2` | 1641 | silent | Node.js OAuth2 client library product | OAuth2 token/refresh path edge + tests |
| `samwafgo/SamWaf` | 1562 | silent | Self-hosted lightweight website WAF product | WAF rule/block path edge + tests |
| `kubernetes-sigs/secrets-store-csi-driver` | 1560 | silent | Kubernetes Secrets Store CSI driver product | CSI secret mount/provider path edge + tests |
| `cachix/secretspec` | 1504 | silent | Declarative secret-provider interface product | secret provider/resolve path edge + tests |
| `securitybunker/databunker` | 1484 | silent | Secure vault for customer PII/PHI/PCI records | PII vault/token path edge + tests |
| `doy/rbw` | 1479 | silent | Unofficial Bitwarden CLI (Rust) secrets product | vault unlock/sync path edge + tests |
| `hudikhq/hoodik` | 1475 | silent | Self-hosted end-to-end encrypted storage | E2E encrypt/storage path edge + tests |
| `lunasec-io/lunasec` | 1469 | silent | Dependency security / SCA scanner product | SCA vuln/path edge + scanner tests |
| `tuneinsight/lattigo` | 1445 | silent | Lattice-based multiparty HE crypto library (Go) | lattice HE/cipher path edge + tests |
| `go-pkgz/auth` | 1353 | silent | Go authenticator via OAuth2/direct/email | OAuth2 auth provider path edge + tests |
| `hvac/hvac` | 1315 | silent | Python client for HashiCorp Vault secrets | Vault secret/path edge + client tests |
| `owasp-dep-scan/dep-scan` | 1284 | silent | OWASP next-gen dependency risk/SCA scanner | SBOM/SCA risk path edge + tests |
| `paralus/paralus` | 1212 | silent | Kubernetes access manager / user credentials | K8s RBAC access/path edge + tests |
| `ramosbugs/oauth2-rs` | 1205 | silent | Strongly-typed Rust OAuth2 client library | OAuth2 client token/path edge + tests |
| `google/certificate-transparency-go` | 1179 | silent | Certificate Transparency auditing library (Go) | CT log/cert path edge + tests |
| `7ritn/VaulTLS` | 1140 | silent | Self-hosted mTLS certificate management app | mTLS cert/issue path edge + tests |
| `apache/casbin-rs` | 1136 | silent | Casbin authorization library for Rust | RBAC/ABAC policy path edge + tests |
| `XmirrorSecurity/OpenSCA-cli` | 1130 | silent | Open-source software supply-chain SCA CLI | SCA/SBOM scan path edge + tests |
| `crewjam/saml` | 1113 | silent | SAML library for Go identity federation | SAML assertion/ACS path edge + tests |
| `mcginty/snow` | 1096 | silent | Rust Noise Protocol Framework crypto library | Noise handshake/cipher path edge + tests |
| `christiaangoossens/hass-oidc-auth` | 1069 | silent | Home Assistant OpenID Connect auth provider | OIDC auth provider path edge + tests |
| `margelo/react-native-quick-crypto` | 1069 | silent | Fast Node crypto module for React Native | crypto API/path edge + native tests |
| `RealmTeam/django-rest-framework-social-oauth2` | 1066 | silent | Django REST social OAuth2 auth product | social OAuth2 token path edge + tests |
| `duo-labs/py_webauthn` | 1061 | silent | Pythonic WebAuthn/FIDO2 server library | WebAuthn ceremony/attestation edge + tests |
| `emanuele-em/proxelar` | 1061 | silent | Scriptable local traffic inspect workbench | proxy inspect/TLS path edge + tests |
| `authomatic/authomatic` | 1054 | silent | Python authorization/authentication client | OAuth auth provider path edge + tests |
| `auth0/auth0-spa-js` | 1010 | silent | Auth0 SPA authentication SDK product | OIDC SPA token/silent-auth path edge + tests |
| `seeden/rbac` | 1005 | silent | Hierarchical RBAC library for Node.js | RBAC hierarchy/permission path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `PiotrMachowski/Xiaomi-cloud-tokens-extractor` | 4772 | silent | IoT token extractor — IoT spill leave |
| `lwch/natpass` | 4447 | silent | Remote access / NAT tunnel utility — VPN-adjacent leave |
| `thangchung/go-coffeeshop` | 4361 | silent | Microservices demo app — template leave |
| `hwholiday/learning_tools` | 4311 | silent | Go learning materials — tutorial leave |
| `GAM-team/GAM` | 4305 | silent | Google Workspace admin CLI — wrong-sector admin CLI leave |
| `alexandreborges/malwoverview` | 4087 | silent | Threat-hunting / malware analysis tool — offensive leave |
| `google-deepmind/acme` | 4062 | silent | Reinforcement learning agents library — ML leave |
| `bitpay/wallet` | 3941 | silent | Bitcoin wallet — crypto-currency leave |
| `masterking32/MasterHttpRelayVPN` | 3927 | silent | Domain-fronted HTTP/SOCKS VPN tunnel — VPN leave |
| `crypto101/book` | 3767 | silent | Cryptography textbook — docs leave |
| `facebookresearch/ReAgent` | 3714 | silent | RL reasoning platform — ML leave |
| `FxPool/FXMinerProxy` | 3709 | silent | Miner proxy — wrong sector / mining leave |
| `ly4k/Certipy` | 3668 | silent | AD Certificate Services enum/abuse tool — offensive leave |
| `gaubert/gmvault` | 3638 | silent | Gmail backup tool — wrong-sector backup leave |
| `coreruleset/coreruleset` | 3266 | disclosure | Disclosure AI-assisted PR template — leave (OWASP CRS otherwise) |
| `sideshow/apns2` | 3187 | silent | Apple Push Notification library — wrong sector (push) |
| `lejianwen/rustdesk-api` | 3112 | silent | RustDesk remote-desktop API — remote-access spill leave |
| `freenet/freenet-core` | 3096 | disclosure | Disclosure CONTRIBUTING AI-policy — leave |
| `LyricTian/gin-admin` | 2859 | silent | Admin panel RBAC scaffolding — admin dashboard leave |
| `speakeasyjs/speakeasy` | 2755 | silent | Unmaintained Node 2FA library — unmaintained leave |
| `lesismal/nbio` | 2754 | silent | High-conn networking library — networking spill leave |
| `xnl-h4ck3r/waymore` | 2749 | silent | Wayback/recon OSINT tool — recon leave |
| `trustgraph-ai/trustgraph` | 2712 | silent | AI context orchestration — AI kit leave |
| `ihciah/shadow-tls` | 2681 | silent | TLS-handshake proxy to evade firewall — GFW/VPN leave |
| `nexus-xyz/nexus-zkvm` | 2618 | silent | zkVM research — ZK/ML spill leave |
| `epsylon/ufonet` | 2523 | silent | Denial-of-Service toolkit — offensive leave |
| `m4ll0k/SecretFinder` | 2513 | silent | Sensitive-data finder / recon script — offensive leave |
| `synctv-org/synctv` | 2486 | silent | Synchronized video watching — wrong sector |
| `static-web-server/static-web-server` | 2357 | silent | Static web server — networking/devops spill leave |
| `AaronL725/grok-register` | 2211 | silent | Bulk Grok account register — AI/abuse leave |
| `suyuan32/simple-admin-core` | 2058 | silent | Admin microservice scaffold — admin dashboard leave |
| `bufanyun/hotgo` | 2030 | silent | Full-stack AI admin platform — admin/AI scaffold leave |
| `KunMoe/kun-galgame-forum` | 1959 | silent | Galgame forum — wrong sector |
| `rustmailer/bichon` | 1949 | silent | Email archive client — wrong sector |
| `scality/cloudserver` | 1943 | silent | S3 object store — databases/storage spill leave |
| `O365/python-o365` | 1921 | silent | Microsoft Graph client — wrong-sector Graph SDK leave |
| `roxy-wi/roxy-wi` | 1823 | silent | Load-balancer admin UI — devops spill leave |
| `yjose/reactjs-popup` | 1805 | silent | React popup UI component — frontend leave |
| `basir/node-react-ecommerce` | 1757 | silent | Ecommerce tutorial app — template leave |
| `UniClipboard/UniClipboard` | 1717 | silent | Clipboard sync app — wrong sector |
| `twilco/kosmonaut` | 1716 | silent | Web browser engine — wrong sector |
| `anyproto/any-sync` | 1709 | silent | Local-first sync protocol — networking spill leave |
| `secluso/core` | 1668 | silent | Pi home security camera — IoT spill leave |
| `Kodiqa-Solutions/VaultS3` | 1605 | silent | S3-compatible object storage — storage spill leave |
| `nohajc/anylinuxfs` | 1557 | silent | macOS linux FS mount — systems spill leave |
| `sartoopjj/thefeed` | 1540 | silent | DNS feed reader — networking spill leave |
| `Danny-Dasilva/CycleTLS` | 1519 | silent | TLS/JA3 fingerprint spoof library — dual-use recon leave |
| `cryptii/cryptii` | 1497 | silent | Educational cipher playground web app — toy leave |
| `dgrubelic/vue-authenticate` | 1424 | silent | Thin Vue auth frontend library — thin frontend auth leave |
| `Kianmhz/GooseRelayVPN` | 1418 | silent | SOCKS5 VPN via Google Apps Script — VPN leave |
| `blacklanternsecurity/TREVORspray` | 1382 | silent | Password sprayer — offensive leave |
| `devfeel/dotweb` | 1377 | silent | Go web micro framework — framework spill leave |
| `KosmosisDire/obsidian-webpage-export` | 1354 | silent | Obsidian export plugin — Obsidian spill leave |
| `tkaitchuck/aHash` | 1346 | silent | Non-cryptographic hash — not security-crypto product |
| `NiREvil/vless` | 1318 | silent | V2Ray/VLESS subscription links — VPN/censorship leave |
| `alx-xlx/goindex` | 1311 | silent | Google Drive indexer — wrong sector |
| `sardanioss/httpcloak` | 1300 | silent | Browser-identical TLS fingerprint HTTP client — dual-use leave |
| `guyoung/CaptfEncoder` | 1298 | silent | CTF encode/decode toolkit — CTF leave |
| `lerd-env/lerd` | 1285 | silent | Local PHP Herd-like env — devops spill leave |
| `jvdsn/crypto-attacks` | 1284 | silent | Cryptographic attack implementations — offensive leave |
| `TencentBlueKing/bk-sops` | 1276 | silent | BlueKing DevOps SOP platform — devops mega leave |
| `privacypass/challenge-bypass-extension` | 1249 | silent | DEPRECATED Privacy Pass extension — deprecated leave |
| `liamcottle/reticulum-meshchat` | 1246 | silent | Mesh chat app — wrong sector |
| `zkonduit/ezkl` | 1221 | silent | ZK ML inference engine — ZK/ML spill leave |
| `projectdiscovery/tlsx` | 1141 | silent | TLS grabber recon tool — recon leave |
| `meganz/webclient` | 1137 | silent | MEGA cloud web client mega — BaaS/client leave |
| `DevLARLEY/WidevineProxy2` | 1098 | silent | Widevine DRM proxy extension — DRM spill leave |
| `k8spacket/k8spacket` | 1097 | silent | K8s traffic metrics — networking observability leave |
| `tophant-ai/ClawVault` | 1078 | silent | OpenClaw agent security vault — AI agent kit leave |
| `ali-bouali/book-social-network` | 1059 | silent | Book social network app — CRUD app leave |
| `ijry/lyadmin` | 1057 | silent | Generic PHP admin panel — admin dashboard leave |
| `D0n9X1n/hexo-blog-encrypt` | 1052 | silent | Hexo blog encrypt plugin — thin blog plugin leave |
| `a16z/jolt` | 1039 | silent | zkVM research — ZK spill leave |
| `authts/react-oidc-context` | 1029 | silent | Thin React OIDC frontend wrapper — thin frontend OIDC leave |
| `ogxd/gxhash` | 1027 | silent | Non-cryptographic hash — not security-crypto product |
| `revertinc/revert` | 1012 | silent | CRM integration platform — wrong sector BaaS leave |

Notes: Prefer midband TS/JS (and Go/Rust/Python fill) security-crypto product homes (PKI/TLS/ACME, IAM/SSO/OTP, secrets managers, SBOM/SAST/SCA, WAF/authZ, host firewall/hardening, OpenPGP/crypto libs). Leave offensive scanners/crackers, RE frameworks, VPN/censorship tools, thin JWT middleware, frontend OIDC clients, specs-only, agent kits, generic web apps, Obsidian spills, disclosure/hard_ban.

