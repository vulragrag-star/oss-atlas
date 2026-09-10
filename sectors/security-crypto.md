# Sector survey: security-crypto

Account: `vulragrag-star` · Input: `survey/raw/security-crypto.jsonl` (44 repos) · Deep-sampled **44** repos (policy files via `gh api` + raw AI policy fetches) · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, prefer **tooling with clear CONTRIBUTING**. Security/crypto maintainers often hate drive-by patches into consensus cores, phishing kits, or novel cryptography — bias to **PKI / TLS / IAM / K8s security / GHA audit / CLI secrets** with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 35 | No hard ban in common CONTRIBUTING/AI paths |
| disclosure | 7 | Explicit AI policy (rustls, zizmor, bitcoin, kyverno/zitadel AGENTS, ghidra AI note) |
| hard_ban | 2 | `kanidm/kanidm`, `openbao/openbao` |
| **agentscan** | 0 | No sample repo/owner on local adopters/blacklist |

Proceed: **14** · Leave: **30** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for clear CONTRIBUTING + tooling fit. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. **Do not** open security advisories / CVE theatre; stick to build/parser/path/config bugs with tests.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `rustls/rustls` | 7605 | disclosure | Clear CONTRIBUTING + AI policy (human-owned code/comments; AI coding OK). Modern TLS lib with strong tests. | TLS API/config edge or CryptoProvider test matrix + rustls-test |
| `cert-manager/cert-manager` | 14069 | silent | Clear CONTRIBUTING + PR template + SECURITY; K8s TLS cert tooling — not core crypto consensus. | cert path/DNSName/CSR encode edge + unit tests |
| `zizmorcore/zizmor` | 6458 | disclosure | Welcomes AI with human-in-loop, disclosure via PR template, issue-first, no AI on GFI. GHA static analysis — playbook-adjacent. | GitHub Actions YAML audit rule / path normalize + snapshot tests |
| `kyverno/kyverno` | 8120 | disclosure | CONTRIBUTING + AGENTS.md for agents; policy-as-code. Prefer engine/CLI edges over docs/GFI spam. | policy YAML parse / path match edge + unit tests |
| `smallstep/certificates` | 8843 | silent | Welcoming CONTRIBUTING + CLA; private CA/ACME tooling with clear process. | ACME/path/SAN parsing edge + go tests |
| `Mbed-TLS/mbedtls` | 6949 | silent | Clear CONTRIBUTING + DCO + PR checklist; portable TLS — small testable API/config bugs only, not novel crypto. | config/parse or build-flag edge + unit tests |
| `dexidp/dex` | 11083 | silent | CONTRIBUTING with DCO/CLA, help-wanted; OIDC connector/config edges. | OIDC connector config / redirect URI parse + tests |
| `quay/clair` | 11057 | silent | .github/CONTRIBUTING with DCO; container vuln static analysis — tooling not phishing. | matcher/index path or purl parse edge + tests |
| `kubescape/kubescape` | 11722 | silent | CONTRIBUTING (central governance); K8s security posture tooling. | control/framework JSON parse or path edge + tests |
| `aquasecurity/kube-bench` | 8176 | silent | Simple CONTRIBUTING; CIS Kubernetes checks — config/YAML edges. | check YAML/config path edge + go tests |
| `gopasspw/gopass` | 7130 | silent | CONTRIBUTING welcomes trivial fixes; CLI password manager — path/quoting playbook class. | store path / git remote quoting / age-backend edge + tests |
| `linkerd/linkerd2` | 11487 | silent | Clear CONTRIBUTING + DCO; security-first mesh — prefer CLI/config path edges over control-plane refactors. | CLI flag/path or identity name normalize + tests |
| `zitadel/zitadel` | 14959 | disclosure | CONTRIBUTING + AGENTS.md for agents; IAM monorepo — stick to small API/CLI bugs with tests. | OIDC/login path or config parse edge + tests |
| `golang-jwt/jwt` | 9217 | silent | Focused JWT library; SECURITY.md present; no hard AI ban. Small surface for parse/claim edges. | JWT claim/time/audience parse edge + table tests |

### Tier notes

**Best first homes (tooling + clear process):**

1. `zizmorcore/zizmor` — GHA static analysis; AI welcome with disclosure + issue-first; no AI on GFI; YAML/rule edges with snapshots.
2. `rustls/rustls` — modern TLS; explicit AI policy (human comments/PR body); strong `rustls-test` culture.
3. `cert-manager/cert-manager` — K8s TLS automation; CONTRIBUTING + sign-off; CSR/DNSName/path edges.
4. `gopasspw/gopass` — CLI secrets manager; CONTRIBUTING welcomes small fixes; classic path/quoting class.
5. `aquasecurity/kube-bench` / `kubescape/kubescape` / `quay/clair` — K8s/container security scanners; config/YAML/purl parse edges.
6. `smallstep/certificates` / `dexidp/dex` / `zitadel/zitadel` — PKI/OIDC/IAM tooling (not consensus coin).
7. `kyverno/kyverno` — policy-as-code; AGENTS.md exists for agents; avoid GFI spam.
8. `Mbed-TLS/mbedtls` — DCO + checklist; only small config/build/testable API bugs, never “invent crypto”.
9. `golang-jwt/jwt` — small claim/time parse surface; no CONTRIBUTING file but focused library.
10. `linkerd/linkerd2` — proceed only for small CLI/config hunks; mesh core is high bar.

**Process friction / read before any future fork:** rustls & zizmor AI policies (human voice, disclosure); zizmor issue-first for non-trivial; mbedtls DCO; dex/clair/linkerd DCO.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `kanidm/kanidm` | 5354 | hard_ban | AGENTS.md: does not condone LLMs/AI; PR template requires no AI-generated content. |
| `openbao/openbao` | 7306 | hard_ban | AGENTS.md: all AI-generated contributions rejected; robot-emoji PR-title honeypot. |
| `bitcoin/bitcoin` | 90132 | disclosure | AI_POLICY allows tools but bans autonomous agents; consensus-critical — drive-by patches hated. |
| `OpenVPN/openvpn` | 14518 | silent | CONTRIBUTING: GitHub PRs discussion-only; patches must go to openvpn-devel mailing list. |
| `NationalSecurityAgency/ghidra` | 74579 | disclosure | CONTRIBUTING: dialogue-first, AI needs extra legal scrutiny, USG process — poor drive-by fit. |
| `rizinorg/cutter` | 19695 | disclosure | RE GUI; CONTRIBUTING exists but reverse-engineering product — high scrutiny / not playbook class. |
| `hahwul/dalfox` | 5280 | silent | XSS scanner; CONTRIBUTING present but offensive-security optics for first-contact drive-by. |
| `jedisct1/libsodium` | 13940 | silent | No CONTRIBUTING in common paths; core crypto lib — maintainers hate unsolicited crypto changes. |
| `weidai11/cryptopp` | 5502 | silent | No CONTRIBUTING found; Crypto++ core algorithms — leave. |
| `veracrypt/VeraCrypt` | 11557 | silent | No CONTRIBUTING found; disk encryption fork of TrueCrypt — high bar / process opaque. |
| `cloudflare/cfssl` | 9468 | silent | No CONTRIBUTING in common paths; PKI toolkit but unclear outsider onboarding. |
| `casdoor/casdoor` | 14364 | silent | Only SECURITY.md; no CONTRIBUTING — weak process signal for IAM drive-by. |
| `monero-project/monero` | 10840 | silent | No CONTRIBUTING found; consensus cryptocurrency — leave. |
| `dogecoin/dogecoin` | 15254 | silent | No CONTRIBUTING found; Bitcoin fork cryptocurrency — leave. |
| `XRPLF/rippled` | 5189 | silent | No CONTRIBUTING found; XRPL consensus daemon — leave. |
| `mimblewimble/grin` | 5097 | silent | No CONTRIBUTING found; Mimblewimble coin — leave. |
| `Cyan4973/xxHash` | 11243 | silent | Non-cryptographic hash; no CONTRIBUTING — weak sector fit. |
| `aquasecurity/tfsec` | 7037 | silent | Deprecated — tfsec is now part of Trivy; do not open new work here. |
| `Hack-with-Github/Awesome-Hacking` | 119916 | silent | Awesome-list dump — not product code. |
| `swisskyrepo/PayloadsAllTheThings` | 80711 | silent | Payload cheatsheet repo — not product contribution target. |
| `kgretzky/evilginx2` | 15598 | silent | Phishing MITM framework — do not drive-by; optics + not playbook class. |
| `gophish/gophish` | 14194 | silent | Phishing toolkit — leave. |
| `SpacehuhnTech/esp8266_deauther` | 14961 | silent | WiFi deauth attack platform — leave. |
| `justcallmekoko/ESP32Marauder` | 12253 | silent | Offensive WiFi/BT suite — leave. |
| `affaan-m/ECC` | 253275 | silent | AI agent harness misclassified into security-crypto — not a crypto/security product. |
| `OpenBB-finance/OpenBB` | 72768 | silent | Finance/quant platform — wrong sector noise. |
| `pocketbase/pocketbase` | 60980 | silent | Realtime backend — wrong sector noise. |
| `freqtrade/freqtrade` | 54147 | silent | Crypto trading bot — trading app, not security/crypto library. |
| `Canop/broot` | 12930 | silent | Directory tree navigator — wrong sector noise. |
| `fulldecent/system-bus-radio` | 6696 | silent | Hardware novelty radio demo — not security tooling product. |

## Sector synthesis

- **Hard excludes in-sector:** `kanidm/kanidm` (explicit no-LLM) and `openbao/openbao` (reject AI-generated PRs + robot-emoji honeypot). Re-read before any future contact.
- **Consensus cryptocurrency cores** (`bitcoin`, `monero`, `dogecoin`, `rippled`, `grin`): even when AI tools are allowed (`bitcoin` AI_POLICY), autonomous agents are banned and drive-by consensus patches are radioactive — leave for this account’s early queue.
- **Offensive / phishing / deauth kits** (`evilginx2`, `gophish`, `esp8266_deauther`, `ESP32Marauder`, payload/awesome dumps): not playbook product work; optics risk.
- **Prefer tooling:** TLS/PKI (rustls, cert-manager, smallstep, mbedtls), IAM/OIDC (dex, zitadel), K8s security (kyverno, kubescape, kube-bench, clair, linkerd), GHA audit (`zizmor`), CLI secrets (`gopass`).
- **Misclassified noise in raw dump:** `affaan-m/ECC`, OpenBB, pocketbase, freqtrade, broot, system-bus-radio, xxHash.
- **Deprecated:** `aquasecurity/tfsec` → Trivy.
- **OpenVPN:** mailing-list workflow — GitHub PR is not the merge path.
- **AgentScan:** none of the deep sample hit local adopters/skip_orgs. Re-run `agentscan-check.py --refresh` before any future fork (API rate-limited during this survey).

## Method notes

- Policy files probed: CONTRIBUTING*, AI.md, AI_POLICY.md, AGENTS.md, CoC, PR templates, SECURITY.md, docs/CONTRIBUTING*, `.github/workflows` names.
- Extra raw fetches: `kanidm` AGENTS.md, `openbao` AGENTS.md, `zizmorcore/.github` AI_POLICY.md, `bitcoin` doc/AI_POLICY.md, `rustls` CONTRIBUTING.md, `ghidra` CONTRIBUTING.md.
- Local AgentScan check during batch scan; GitHub API later hit rate limit — no tracker comments, no forks/PRs.

## Product deepen (≥5k★ subset) (2026-09-10, +79 scored)

Account: `vulragrag-star` · Curated PKI/TLS/IAM/secrets/SBOM/SAST/access product homes still missing after midband · Policy via `raw.githubusercontent.com` · **51** proceed / **28** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 62, 'disclosure': 17}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `dani-garcia/vaultwarden` | 66999 | silent | Bitwarden-compatible secrets server; vault path/config edges | vault path/config/API edge + Rust tests |
| `traefik/traefik` | 64795 | disclosure | Cloud-native proxy; router/middleware/path edges — AGENTS disclosure | router/middleware/path edge + Go tests — disclose AI |
| `acmesh-official/acme.sh` | 47609 | silent | Shell ACME client; domain/path/dns-api edges | domain/path/dns-api edge + shell tests |
| `aquasecurity/trivy` | 37848 | silent | Vuln/misconfig/SBOM scanner; path/target edges | scan target/path/SBOM edge + Go tests |
| `AdguardTeam/AdGuardHome` | 36759 | silent | DNS adblock server; config/path/filter edges | config/path/filter edge + Go/TS tests |
| `keycloak/keycloak` | 36712 | disclosure | IAM/IdP; realm/client/config edges — disclose AI | realm/client/config edge + tests — disclose AI |
| `tailscale/tailscale` | 36297 | silent | WireGuard mesh VPN; ACL/path/config edges | ACL/path/config edge + Go tests |
| `hashicorp/vault` | 36219 | silent | Secrets management; path/policy/auth method edges — CLA/process care | secret path/policy/auth edge + Go tests |
| `certbot/certbot` | 33231 | disclosure | EFF ACME client; renew/path/plugin edges — AI allowed w/ disclosure + priority evidence | renew/path/plugin edge + py tests — disclose AI |
| `jumpserver/jumpserver` | 31512 | silent | PAM platform; asset/path/ACL edges | asset/path/ACL edge + py tests |
| `projectdiscovery/nuclei` | 31092 | silent | Vuln scanner templates; template/path edges | template/path/match edge + Go tests |
| `openssl/openssl` | 30770 | disclosure | TLS/crypto library — config/build/API edges only, never invent crypto; disclose AI | config/build/API edge + tests — disclose AI; no novel crypto |
| `better-auth/better-auth` | 29863 | disclosure | Auth framework; session/provider/config edges — AI policy | session/provider/config edge + TS tests — disclose AI |
| `gitleaks/gitleaks` | 29191 | silent | Secrets scanner; rule/path edges | rule/path/detect edge + Go tests |
| `Infisical/infisical` | 29164 | silent | Secrets platform; path/env/sync edges | secret path/env sync edge + TS tests |
| `netbirdio/netbird` | 29055 | silent | WireGuard overlay; peer/path/config edges | peer/path/config edge + Go tests |
| `authelia/authelia` | 28868 | silent | SSO MFA portal; config/path/OIDC edges | config/path/OIDC edge + Go tests |
| `keepassxreboot/keepassxc` | 28741 | disclosure | Password manager; entry/path/import edges — disclose AI assist | entry/path/import edge + C++ tests — disclose AI |
| `nextauthjs/next-auth` | 28366 | silent | Web auth library; provider/callback/path edges | provider/callback/path edge + TS tests |
| `trufflesecurity/trufflehog` | 27738 | silent | Credential finder; detector/path edges | detector/path/verify edge + Go tests |
| `goauthentik/authentik` | 25418 | disclosure | Auth glue IdP; flow/provider/config edges — AI welcome w/ disclosure+HITL | flow/provider/config edge + py tests — disclose AI |
| `osquery/osquery` | 23556 | silent | OS instrumentation SQL; table/query/path edges | table/query/path edge + C++ tests |
| `chaitin/SafeLine` | 22549 | silent | Self-hosted WAF; rule/config/path edges | WAF rule/config/path edge + Go tests |
| `TecharoHQ/anubis` | 22318 | disclosure | AI-crawler weight gate; config/path edges — AGENTS disclosure | config/path/challenge edge + Go tests — disclose AI |
| `gravitational/teleport` | 20900 | silent | Secure access platform; role/path/session edges | role/path/session edge + Go tests |
| `apache/casbin` | 20381 | silent | AuthZ library; policy/model edges | policy/model match edge + Go tests |
| `ory/hydra` | 17524 | disclosure | OAuth2/OIDC server; client/config edges — AI policy | OAuth client/config edge + Go tests — disclose AI |
| `wazuh/wazuh` | 16800 | silent | XDR/SIEM platform; rule/decoder/path edges | rule/decoder/path edge + tests |
| `crowdsecurity/crowdsec` | 14787 | silent | Collaborative IPS; scenario/path edges | scenario/path edge + Go tests |
| `projectdiscovery/subfinder` | 14399 | silent | Passive subdomain enum; source/config edges | source/config edge + Go tests |
| `ory/kratos` | 13870 | disclosure | Headless identity; identity/schema/path edges — AI policy | identity/schema/path edge + Go tests — disclose AI |
| `bitwarden/clients` | 13762 | silent | Bitwarden clients; vault item/path/crypto-ui edges | vault item/path edge + TS tests |
| `anchore/grype` | 12865 | silent | Container/filesystem vuln scanner; DB/path edges | vuln match/path edge + Go tests |
| `open-policy-agent/opa` | 12210 | disclosure | Policy engine; Rego/path edges — AGENTS AI mention | Rego/path/input edge + Go tests — follow AGENTS |
| `google/osv-scanner` | 10992 | silent | OSV vulnerability scanner; lockfile/path edges | lockfile/path edge + Go tests |
| `projectdiscovery/httpx` | 10371 | silent | HTTP toolkit; URL/header/path edges | URL/header/path edge + Go tests |
| `go-acme/lego` | 9863 | silent | ACME client lib/CLI; challenge/path edges | ACME challenge/path edge + Go tests |
| `VirusTotal/yara` | 9853 | silent | Pattern matching engine; rule/path edges | rule/path compile edge + C tests |
| `anchore/syft` | 9544 | silent | SBOM generator CLI; path/format edges | SBOM path/format edge + Go tests |
| `falcosecurity/falco` | 9352 | silent | Runtime security; rule/config/path edges | rule/config/path edge + tests |
| `bridgecrewio/checkov` | 8996 | silent | IaC scanner; check/path edges | IaC check/path edge + py tests |
| `securego/gosec` | 8945 | silent | Go security checker; rule/AST edges | rule/AST/path edge + Go tests |
| `containers/bubblewrap` | 8636 | silent | Unprivileged sandbox; arg/path edges | arg/path sandbox edge + C tests |
| `panva/jose` | 7784 | silent | JWS/JWE/JWT lib; claim/header edges | JWT claim/header edge + TS tests |
| `pyca/cryptography` | 7762 | silent | Python crypto bindings — API/hazmat edges only | API/hazmat edge + py tests — not invent algorithms |
| `netblue30/firejail` | 7632 | silent | Namespace sandbox; profile/path edges | profile/path edge + C tests |
| `external-secrets/external-secrets` | 6840 | disclosure | ESO operator; SecretStore/path edges — AI-assisted mention in template | SecretStore/path/key edge + Go tests — disclose if AI |
| `fleetdm/fleet` | 6821 | silent | Device management; query/path/config edges | query/path/config edge + Go tests |
| `passbolt/passbolt_api` | 6112 | silent | Team password API; resource/path/ACL edges | resource/path/ACL edge + PHP tests |
| `ossf/scorecard` | 5685 | silent | Security scorecard; check/path edges | check/path edge + Go tests |
| `deepfence/ThreatMapper` | 5321 | silent | Cloud-native threat mapper; scan/path edges | scan/path edge + Go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `mitmproxy/mitmproxy` | 44978 | silent | Pen-test intercepting proxy — careful optics; leave for first-contact drive-by |
| `sqlmapproject/sqlmap` | 38394 | silent | Offensive SQL injection toolkit — optics; not playbook product farm |
| `istio/istio` | 38378 | silent | Service mesh mega — prefer small CLI/config in dedicated tools; high bar |
| `OWASP/CheatSheetSeries` | 33133 | disclosure | Docs/cheatsheet dump — not product code |
| `nginx/nginx` | 31606 | silent | HTTP server mega — better networking-distributed; high bar |
| `trailofbits/algo` | 30369 | silent | VPN install script — recipe class; prefer product codebases |
| `envoyproxy/envoy` | 28893 | disclosure | Envoy proxy mega — AI policy exists but mesh core high bar; leave drive-by |
| `hwdsl2/setup-ipsec-vpn` | 28453 | silent | IPsec VPN installer script — recipe class; leave |
| `wg-easy/wg-easy` | 26881 | disclosure | WireGuard admin UI recipe — prefer netbird/tailscale product CLIs |
| `hashcat/hashcat` | 26739 | silent | Password cracker — offensive recovery class; leave |
| `robertdavidgraham/masscan` | 25994 | silent | Async SYN port scanner — offensive recon class; leave |
| `cilium/cilium` | 25107 | disclosure | eBPF platform mega — disclosure template; prefer smaller tetragon/falco homes |
| `radareorg/radare2` | 24770 | silent | RE framework — reverse-engineering product; high scrutiny |
| `jaredhanson/passport` | 23530 | silent | Legacy Passport.js — sparse process; prefer better-auth/next-auth |
| `renovatebot/renovate` | 22445 | silent | Dependency automation — better devops-build sector |
| `MobSF/Mobile-Security-Framework-MobSF` | 21719 | silent | Mobile security framework GUI — RE/mobile-audit class; leave |
| `elastic/kibana` | 21285 | disclosure | Observability mega UI — not security-sector primary; prefer osquery/fleet/wazuh |
| `Nyr/openvpn-install` | 20636 | silent | OpenVPN installer script — recipe class; leave |
| `bee-san/RustScan` | 20388 | silent | Port scanner — recon class; weak playbook fit |
| `golangci/golangci-lint` | 19359 | silent | Go linter runner — better editors-devex / python-tooling adjacency |
| `auth0/node-jsonwebtoken` | 18196 | silent | Small JWT lib; no CONTRIBUTING — prefer panva/jose or golang-jwt |
| `projectdiscovery/katana` | 17406 | silent | Crawler/spider — recon-adjacent; prefer nuclei/httpx product edges |
| `openwall/john` | 13608 | silent | John the Ripper — offensive cracker; leave |
| `nmap/nmap` | 13538 | silent | Network mapper mirror — prefer non-offensive product CLIs; high process bar |
| `Shopify/toxiproxy` | 12314 | silent | Chaos TCP proxy — better devops/networking chaos class than security-crypto |
| `lucia-auth/lucia` | 10450 | silent | Auth lib with no CONTRIBUTING in common paths — weak process signal / possibly archived lane |
| `haproxy/haproxy` | 6837 | silent | LB mirror — networking mega; high bar / weak outsider onboarding |
| `ossec/ossec-hids` | 5056 | silent | Legacy HIDS — prefer wazuh successor product |

Notes: Prefer secrets/PKI/IAM/SBOM/SAST/access homes (vaultwarden, vault, trivy, gitleaks, keycloak, authentik, OPA, teleport, falco). Disclosure: openssl, keycloak, authentik, certbot, keepassxc, ory/*, better-auth, anubis, traefik, opa, external-secrets. Scanner false-positive NO-AI on certbot/authentik overridden to disclosure (AI allowed with HITL). Leave offensive scanners/crackers, RE frameworks, VPN install recipes, mesh megas (istio/envoy/cilium), and wrong-sector (renovate/golangci/kibana).

