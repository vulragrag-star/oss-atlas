# Sector survey: devops-build

Account: `vulragrag-star` · Input: `survey/raw/devops-build.jsonl` (233 repos; lots of awesome/tutorial/game noise) · Deep-sampled **45** cmake/ninja/build/packaging/k8s/container tools via raw.githubusercontent.com policy files + local AgentScan dumps · Skip satellites & AgentScan · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **build / packaging / container / k8s-CLI path·quoting·parser bugs with regression tests** (cmake/ninja wrappers, Earthfile/Dockerfile parsers, goreleaser config, kubectl plugins — not games with incidental cmake, not awesome-lists, not platform UIs).

## Policy histogram (deep sample of 45)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 40 | Most build/k8s tools still have no AI hard-ban page |
| disclosure | 5 | goreleaser, flux2, argo-workflows, prometheus-operator, kubernetes (parked) |
| hostility_risk | 0 | None in this sample |
| hard_ban | 0 | None in this sample (QEMU/Zig/etc. not in shard focus) |
| agentscan | 0 | No sample repo/owner on local adopters/blacklist |

Proceed: **35** · Leave: **10** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class (build/packaging/container/k8s-CLI + tests). Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `ninja-build/ninja` | 13206 | silent | build system core; path/parallel-make/parser bugs with tests | jobserver/path/parallel-make or depfile parse edge + C++ tests |
| `goreleaser/goreleaser` | 16023 | disclosure | CONTRIBUTING AI guidelines — disclose use; do not pretend to be human agent-farming; packaging/config/path | config path/template quoting or archive name edge + Go tests — disclose AI |
| `ko-build/ko` | 8516 | silent | Go container build/deploy; path/importpath | importpath/base-image path or multi-platform build edge + Go tests |
| `kubernetes-sigs/kind` | 15478 | silent | k8s-in-docker CLI; path/config | node image path / kubeadm config edge + Go tests |
| `ahmetb/kubectx` | 19978 | silent | kubectl plugin; path/context parsing | kubeconfig context/namespace path parse edge + Go/shell tests |
| `jesseduffield/lazydocker` | 52756 | silent | docker TUI; argv/path | docker host path / compose project path edge + Go tests |
| `earthly/earthly` | 12045 | silent | build framework; Dockerfile/Makefile-like parser | Earthfile target/path or ARG quoting edge + Go tests |
| `jetify-com/devbox` | 12342 | silent | nix-based env manager; path/quoting | devbox.json path / nix flake quoting edge + Go tests |
| `woodpecker-ci/woodpecker` | 7831 | silent | CI engine; pipeline YAML/path | pipeline YAML step path / clone path edge + Go tests |
| `Jguer/yay` | 13742 | silent | AUR helper; path/quoting/pkgbuild | PKGBUILD path/quoting or AUR RPC parse edge + Go tests |
| `Morganamilo/paru` | 8974 | silent | AUR helper; path/quoting | PKGBUILD path/quoting or pacman.conf path edge + Rust tests |
| `alexellis/k3sup` | 7425 | silent | k3s bootstrap CLI; SSH/path/quoting | SSH remote path / k3s install arg quoting + Go tests |
| `podman-container-tools/buildah` | 9009 | silent | OCI image build; path/argv | build context path / --build-arg quoting + Go tests |
| `GoogleContainerTools/skaffold` | 15888 | silent | k8s dev loop; config/path | skaffold.yaml profile/path or artifact sync edge + Go tests |
| `bitnami/sealed-secrets` | 9276 | silent | k8s secrets CLI/controller; path/YAML | kubeseal path / scope name edge + Go tests |
| `fluxcd/flux2` | 8384 | disclosure | CONTRIBUTING+AGENTS require Assisted-by trailer (no agent Signed-off-by); GitOps CLI path/kustomize/helm edges | bootstrap path / source URL edge + Go tests — Assisted-by trailer |
| `replicate/cog` | 9470 | silent | ML container build; Dockerfile/path | cog.yaml path / Dockerfile generate edge + Go tests |
| `pkgxdev/pkgx` | 9916 | silent | package runner; path/version parsing | package selector / PATH install edge + tests |
| `loft-sh/vcluster` | 11295 | silent | virtual cluster CLI; config/path | values/path / distro config edge + Go tests |
| `velero-io/velero` | 10284 | silent | k8s backup CLI; path/config | backup location path / exclude path edge + Go tests |
| `kubernetes-sigs/kubebuilder` | 9307 | silent | k8s API scaffolding; path/codegen | scaffold path / domain-repo flag edge + Go tests |
| `amir20/dozzle` | 14300 | silent | container log viewer; path/filter | container filter / log path edge + Go tests |
| `dockur/windows` | 53197 | silent | Docker packaging scripts; shell path/quoting | entrypoint shell path/quoting or env parse edge + shell tests |
| `gruntwork-io/terratest` | 7943 | silent | infra test lib; path/terraform args | terraform dir path / options quoting + Go tests |
| `uber/kraken` | 6743 | silent | P2P docker registry; path/OCI | registry path / torrent meta path edge + Go tests |
| `dagger/dagger` | 16230 | silent | CONTRIBUTING: claim issue first, communicate design upfront; build/CI pipeline path | module path / pipeline arg edge + Go tests — claim issue first |
| `argoproj/argo-workflows` | 16959 | disclosure | PR checklist requires AI declaration + DCO/Conventional Commits; workflow YAML/path edges | workflow template path / artifact path edge + Go tests — AI declaration |
| `tektoncd/pipeline` | 9061 | silent | pipeline CRDs; YAML/path edge cases | Task/Pipeline path / workspace bind edge + Go tests |
| `kubernetes/kops` | 16670 | silent | k8s install CLI; config/path | cluster YAML path / cloud flag edge + Go tests — open issue first |
| `stakater/Reloader` | 10392 | silent | k8s controller; config annotation parsing | annotation parse / namespace path edge + Go tests |
| `fission/fission` | 8914 | silent | k8s FaaS CLI; path/config | function package path / env config edge + Go tests |
| `prometheus-operator/prometheus-operator` | 9976 | disclosure | AI allowed with human ownership + communicate significant AI in PR/commit; CRD/config edges | Prometheus CR path/relabel config edge + Go tests — disclose AI |
| `krallin/tini` | 11224 | silent | tiny C init — argv/signal edges; low policy surface; verify activity before investing | argv/-- subcommand edge or signal forwarding + C tests |
| `google/gvisor` | 19245 | silent | AGENTS.md orients assistants (no hard ban); container sandbox path/OCI — Google CLA / high bar | OCI path / mount path edge + Go tests — Google CLA |
| `rust-lang/cargo` | 15460 | silent | package manager; path/lockfile/quoting | path dep / lockfile / quoting edge + Rust tests — high bar |

### Tier notes

**Best first homes (small testable build/path/quoting hunks):**

1. `ninja-build/ninja` — classic build system; jobserver/path/depfile class matches METHOD.md cmake/ninja wrappers.
2. `goreleaser/goreleaser` — packaging/release CLI; **disclose AI**; config/path/template edges.
3. `ko-build/ko` / `podman-container-tools/buildah` / `replicate/cog` — container build path/importpath/Dockerfile generate.
4. `kubernetes-sigs/kind` / `ahmetb/kubectx` / `alexellis/k3sup` — small k8s CLIs; kubeconfig/SSH path quoting.
5. `jesseduffield/lazydocker` / `amir20/dozzle` / `dockur/windows` — docker UX/shell path surfaces.
6. `earthly/earthly` / `woodpecker-ci/woodpecker` — Earthfile / pipeline YAML parsers.
7. `jetify-com/devbox` / `Jguer/yay` / `Morganamilo/paru` / `pkgxdev/pkgx` — env/package managers; path/quoting.
8. `GoogleContainerTools/skaffold` / `bitnami/sealed-secrets` / `loft-sh/vcluster` / `velero-io/velero` — k8s tool config/path.

**Careful / later (disclosure or process friction):**

- `fluxcd/flux2` — **Assisted-by** trailer required; no agent `Signed-off-by`/`Co-authored-by`.
- `argoproj/argo-workflows` — AI declaration in PR checklist + DCO/Conventional Commits.
- `prometheus-operator/prometheus-operator` — AI OK with human ownership; say so in PR/commit when significant.
- `dagger/dagger` — claim an issue first; communicate design early.
- `kubernetes/kops` — open an issue before PR (per AGENTS).
- `google/gvisor`, `rust-lang/cargo` — high bar / CLA / RFC culture; not first-home picks.
- `tektoncd/pipeline`, `kubernetes-sigs/kubebuilder`, `fission/fission` — agent-oriented AGENTS.md present (not a ban); large surfaces.

**Parked (scored leave):** `kubernetes/kubernetes` — disclose-AI + SIG process too heavy for new-account first home.

**Clusters to farm leftovers (one home at a time):**

| Cluster | Repos | Hunk shape |
|---|---|---|
| Build systems | ninja, earthly, dagger | depfile / Earthfile / module path |
| Packaging / release | goreleaser, yay, paru, pkgx, devbox | config path / PKGBUILD quoting / lockfile |
| Container build | ko, buildah, cog, skaffold, kraken | context path / importpath / Dockerfile gen |
| k8s CLIs | kind, kubectx, k3sup, vcluster, velero, sealed-secrets | kubeconfig / values / bootstrap path |
| CI/GitOps | woodpecker, flux2, argo-workflows, tekton, terratest | pipeline YAML / Assisted-by where required |
| Docker UX / shell | lazydocker, dozzle, dockur/windows, tini | host path / argv / entrypoint quoting |

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `kubernetes/kubernetes` | 126898 | disclosure | disclose AI in PRs; too large / SIG process for new-account first home — park |
| `bcicen/ctop` | 17838 | silent | last push mid-2024; appears low-maintenance — weak cadence for regression feedback |
| `kubesphere/kubesphere` | 17038 | silent | large platform UI; not quoting/build hunk class |
| `OpenRCT2/OpenRCT2` | 16197 | silent | game product; cmake incidental |
| `dutchcoders/transfer.sh` | 15892 | silent | file-sharing service, not build tool |
| `cheat/cheat` | 13446 | silent | docs cheatsheets, not product build tool |
| `gotenberg/gotenberg` | 13023 | silent | PDF convert API; weak build-tool fit |
| `diasurgical/DevilutionX` | 9722 | silent | game product; cmake incidental |
| `openshift/origin` | 8684 | silent | conformance/platform suite; heavy process |
| `fabiolb/fabio` | 7341 | silent | load balancer; networking sector better |

## Shard noise (not deep-sampled)

Raw `devops-build.jsonl` also contains high-★ tutorial/awesome/curriculum dumps (`codecrafters-io/build-your-own-x`, `sindresorhus/awesome`, `freeCodeCamp/freeCodeCamp`, roadmap/interview repos, etc.) and apps that only mention Docker in topics. Those were skipped for deep policy work — not product build/packaging/k8s tools.

## Method notes

- Policy files fetched from `raw.githubusercontent.com` (REST core quota was exhausted by parallel sector agents).
- AgentScan: local `data/agentscan-adopters.txt` + `agentscan-blacklist.json` skip_orgs — **0 hits** in this 45-repo sample.
- Satellites from `repo-gate.py` not present in sample.
- Predecessor open queues (meson/hatch/cibuildwheel/…) not in this curated sample.
- Before any future contribution: refresh AgentScan + hostility-scan; sample 10 merged outsider PRs.

