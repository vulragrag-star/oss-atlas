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

