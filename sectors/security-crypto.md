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
