# Sector survey: devops-build

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 110 | No hard ban in common paths |
| disclosure | 8 | AI disclosure language |

Proceed: **89** · Leave: **29**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `dockur/windows` | 53197 | silent | Docker packaging scripts; shell path/quoting | entrypoint shell path/quoting or env parse edge + shell tests |
| `jesseduffield/lazydocker` | 52756 | silent | docker TUI; argv/path | docker host path / compose project path edge + Go tests |
| `lerna/lerna` | 36055 | silent | Monorepo publish/build CLI; workspace/path edges | workspace/publish/path edge + tests |
| `ahmetb/kubectx` | 19978 | silent | kubectl plugin; path/context parsing | kubeconfig context/namespace path parse edge + Go/shell tests |
| `google/gvisor` | 19245 | silent | AGENTS.md orients assistants (no hard ban); container sandbox path/OCI — Google CLA / high bar | OCI path / mount path edge + Go tests — Google CLA |
| `argoproj/argo-workflows` | 16959 | disclosure | PR checklist requires AI declaration + DCO/Conventional Commits; workflow YAML/path edges | workflow template path / artifact path edge + Go tests — AI declaration |
| `kubernetes/kops` | 16670 | silent | k8s install CLI; config/path | cluster YAML path / cloud flag edge + Go tests — open issue first |
| `dagger/dagger` | 16230 | silent | CONTRIBUTING: claim issue first, communicate design upfront; build/CI pipeline path | module path / pipeline arg edge + Go tests — claim issue first |
| `goreleaser/goreleaser` | 16023 | disclosure | CONTRIBUTING AI guidelines — disclose use; do not pretend to be human agent-farming; packaging/config/path | config path/template quoting or archive name edge + Go tests — disclose AI |
| `GoogleContainerTools/skaffold` | 15888 | silent | k8s dev loop; config/path | skaffold.yaml profile/path or artifact sync edge + Go tests |
| `kubernetes-sigs/kind` | 15478 | silent | k8s-in-docker CLI; path/config | node image path / kubeadm config edge + Go tests |
| `rust-lang/cargo` | 15460 | silent | package manager; path/lockfile/quoting | path dep / lockfile / quoting edge + Rust tests — high bar |
| `amir20/dozzle` | 14300 | silent | container log viewer; path/filter | container filter / log path edge + Go tests |
| `Jguer/yay` | 13742 | silent | AUR helper; path/quoting/pkgbuild | PKGBUILD path/quoting or AUR RPC parse edge + Go tests |
| `ninja-build/ninja` | 13206 | silent | build system core; path/parallel-make/parser bugs with tests | jobserver/path/parallel-make or depfile parse edge + C++ tests |
| `jetify-com/devbox` | 12342 | silent | nix-based env manager; path/quoting | devbox.json path / nix flake quoting edge + Go tests |
| `earthly/earthly` | 12045 | silent | build framework; Dockerfile/Makefile-like parser | Earthfile target/path or ARG quoting edge + Go tests |
| `loft-sh/vcluster` | 11295 | silent | virtual cluster CLI; config/path | values/path / distro config edge + Go tests |
| `krallin/tini` | 11224 | silent | tiny C init — argv/signal edges; low policy surface; verify activity before investing | argv/-- subcommand edge or signal forwarding + C tests |
| `stakater/Reloader` | 10392 | silent | k8s controller; config annotation parsing | annotation parse / namespace path edge + Go tests |
| `velero-io/velero` | 10284 | silent | k8s backup CLI; path/config | backup location path / exclude path edge + Go tests |
| `prometheus-operator/prometheus-operator` | 9976 | disclosure | AI allowed with human ownership + communicate significant AI in PR/commit; CRD/config edges | Prometheus CR path/relabel config edge + Go tests — disclose AI |
| `pkgxdev/pkgx` | 9916 | silent | package runner; path/version parsing | package selector / PATH install edge + tests |
| `replicate/cog` | 9470 | silent | ML container build; Dockerfile/path | cog.yaml path / Dockerfile generate edge + Go tests |
| `kubernetes-sigs/kubebuilder` | 9307 | silent | k8s API scaffolding; path/codegen | scaffold path / domain-repo flag edge + Go tests |
| `bitnami/sealed-secrets` | 9276 | silent | k8s secrets CLI/controller; path/YAML | kubeseal path / scope name edge + Go tests |
| `tektoncd/pipeline` | 9061 | silent | pipeline CRDs; YAML/path edge cases | Task/Pipeline path / workspace bind edge + Go tests |
| `podman-container-tools/buildah` | 9009 | silent | OCI image build; path/argv | build context path / --build-arg quoting + Go tests |
| `Morganamilo/paru` | 8974 | silent | AUR helper; path/quoting | PKGBUILD path/quoting or pacman.conf path edge + Rust tests |
| `fission/fission` | 8914 | silent | k8s FaaS CLI; path/config | function package path / env config edge + Go tests |
| `ko-build/ko` | 8516 | silent | Go container build/deploy; path/importpath | importpath/base-image path or multi-platform build edge + Go tests |
| `fluxcd/flux2` | 8384 | disclosure | CONTRIBUTING+AGENTS require Assisted-by trailer (no agent Signed-off-by); GitOps CLI path/kustomize/helm edges | bootstrap path / source URL edge + Go tests — Assisted-by trailer |
| `yarnpkg/berry` | 8103 | silent | Yarn modern package manager; lock/path/workspace edges | lockfile/workspace/path edge + tests |
| `gruntwork-io/terratest` | 7943 | silent | infra test lib; path/terraform args | terraform dir path / options quoting + Go tests |
| `woodpecker-ci/woodpecker` | 7831 | silent | CI engine; pipeline YAML/path | pipeline YAML step path / clone path edge + Go tests |
| `alexellis/k3sup` | 7425 | silent | k3s bootstrap CLI; SSH/path/quoting | SSH remote path / k3s install arg quoting + Go tests |
| `uber/kraken` | 6743 | silent | P2P docker registry; path/OCI | registry path / torrent meta path edge + Go tests |
| `testcontainers/testcontainers-go` | 4971 | silent | Programmatic container deps for Go tests | image/wait strategy / mount path edge + Go tests |
| `crazy-max/diun` | 4904 | silent | Docker image update notifier; registry watch | image watch / notify config path edge + Go tests |
| `psviderski/unregistry` | 4862 | silent | Push images to remote hosts without external registry | SSH path / image push edge + Go tests |
| `stern/stern` | 4851 | silent | Multi-pod container log tailing for Kubernetes | pod query / kubeconfig path edge + Go tests |
| `werf/werf` | 4719 | silent | GitOps-friendly delivery to Kubernetes | werf.yaml path / build context edge + Go tests |
| `jenkins-x/jx` | 4690 | silent | Jenkins X CI+CD for Kubernetes CLI | pipeline path / preview env edge + Go tests |
| `gliderlabs/logspout` | 4690 | silent | Log routing for Docker container logs | route URL / adapter path edge + Go tests |
| `magefile/mage` | 4689 | silent | Make/Rake-like Go build tool; path/target edges | magefile target/path edge + Go tests |
| `gliderlabs/registrator` | 4675 | silent | Service registry bridge for Docker | service label / registry path edge + Go tests |
| `AliyunContainerService/pouch` | 4644 | silent | Enterprise container engine | runtime path / image store edge + Go tests |
| `alexellis/arkade` | 4615 | silent | Open-source marketplace CLI for k8s developer tools | app install path / kubeconfig edge + Go tests |
| `docker/buildx` | 4496 | silent | Docker CLI plugin for BuildKit builds; path/bake edges | bake file path / --build-arg quoting + Go tests |
| `moonrepo/moon` | 4095 | silent | Monorepo build system; task/path/config edges | task graph/path/config edge + tests |
| `roboll/helmfile` | 4033 | silent | Deploy Helm charts declaratively; path/values edges | helmfile.yaml path / values quoting edge + Go tests |
| `hasura/gitkube` | 3846 | silent | git-push deploy Docker images to Kubernetes | remote path / Dockerfile edge + Go tests |
| `spegel-org/spegel` | 3774 | disclosure | Stateless cluster-local OCI registry mirror — disclose AI if used | mirror path / peer discovery edge + Go tests |
| `DeterminateSystems/nix-installer` | 3683 | silent | Fast Nix+flakes installer; path/init edges | install path / init system edge + Rust tests |
| `akuity/kargo` | 3637 | silent | Application lifecycle orchestration (GitOps) | stage/path / freight edge + Go tests |
| `terramate-io/terramate` | 3623 | silent | IaC orchestration / GitOps for Terraform stacks | stack path / generate edge + Go tests |
| `railwayapp/nixpacks` | 3555 | silent | App+Nix+Docker image builder; path/plan edges | detect/plan path or provider edge + Go/Rust tests |
| `okteto/okteto` | 3541 | silent | Develop apps directly in Kubernetes | okteto.yml path / sync edge + Go tests |
| `FairwindsOps/polaris` | 3385 | silent | K8s best-practice validation CLI/dashboard | manifest path / check config edge + Go tests |
| `goodwithtech/dockle` | 3295 | silent | Container image CIS linter CLI | image ref / Dockerfile path edge + Go tests |
| `alexei-led/pumba` | 3145 | silent | Chaos testing for containers; name/path edges | container name filter / netem edge + Go tests |
| `zegl/kube-score` | 3102 | silent | Static analysis of Kubernetes object YAML | manifest path / score check edge + Go tests |
| `ContainerSSH/ContainerSSH` | 3075 | silent | SSH that launches containers on demand | config path / backend edge + Go tests |
| `sablierapp/sablier` | 2946 | silent | Scale containers on demand; label/path edges | scale label / idle timeout edge + Go tests |
| `keel-hq/keel` | 2727 | silent | K8s operator automating image updates | policy annotation / registry path edge + Go tests |
| `project-zot/zot` | 2726 | silent | Vendor-neutral OCI-native registry | config path / storage root edge + Go tests |
| `bazelbuild/bazelisk` | 2679 | silent | Bazel version wrapper CLI; path/download edges | version pin/path or mirror URL edge + Go tests |
| `goreleaser/nfpm` | 2631 | silent | deb/rpm/apk/ipk packager CLI; path/config edges | nfpm.yaml path / package name edge + Go tests |
| `thought-machine/please` | 2610 | silent | High-performance multi-language build system; path/target edges | BUILD target/path or remote-cache edge + Go tests |
| `FairwindsOps/pluto` | 2578 | silent | CLI discovering deprecated k8s apiVersions | manifest path / apiVersion edge + Go tests |
| `oras-project/oras` | 2420 | silent | OCI registry client CLI for artifacts/images | ref/path or manifest annotate edge + Go tests |
| `regclient/regclient` | 1927 | silent | Docker/OCI registry client + tooling | registry ref/path or tag copy edge + Go tests |
| `kapicorp/kapitan` | 1926 | silent | Templated config management for k8s/Terraform | inventory path / compile edge + Python tests |
| `kptdev/kpt` | 1892 | disclosure | Automate Kubernetes configuration editing — disclose AI if used | pkg path / set/apply edge + Go tests |
| `carvel-dev/ytt` | 1876 | silent | YAML templating tool (Carvel) | template path / data values edge + Go tests |
| `arttor/helmify` | 1742 | silent | Create Helm chart from Kubernetes YAML | input YAML path / chart out edge + Go tests |
| `rancher/fleet` | 1726 | disclosure | GitOps for large fleets of Kubernetes clusters — disclose AI if used | bundle path / target cluster edge + Go tests |
| `ufoscout/docker-compose-wait` | 1707 | silent | Wait-for-deps script for compose; host/port edges | host/port wait / timeout edge + shell/Go tests |
| `flux-iac/tofu-controller` | 1690 | silent | GitOps OpenTofu/Terraform controller for Flux | Terraform path / source edge + Go tests |
| `chainguard-dev/apko` | 1672 | silent | Build OCI images from APK without Dockerfile; path/config | apko.yaml path / package set edge + Go tests |
| `iximiuz/cdebug` | 1669 | silent | Swiss-army container debugging CLI | target container / nic/path edge + Go tests |
| `kubeshop/testkube` | 1655 | silent | K8s-native testing platform CLI/operator | test CR path / executor edge + Go tests |
| `helm/chart-testing` | 1639 | silent | CLI for linting/testing Helm charts | chart path / ct.yaml edge + Go tests |
| `stepchowfun/toast` | 1630 | silent | Containerized task runner; Dockerfile/path edges | toast.yml path / cache mount edge + Rust tests |
| `agola-io/agola` | 1622 | silent | CI/CD redefined — container-native pipelines | run config path / workspace edge + Go tests |
| `TraceMachina/nativelink` | 1588 | silent | Nix-powered Bazel remote execution/cache; path/CAS edges | CAS/path or remote-exec config edge + Rust tests |
| `OT-CONTAINER-KIT/redis-operator` | 1450 | silent | Redis operator for K8s | CR path / redis.conf edge + Go tests |
| `kitops-ml/kitops` | 1411 | silent | CNCF tool packaging ML models as OCI ModelKits | kitfile path / pack edge + Go tests |
| `denoland/dnt` | 1334 | silent | Deno package emit CLI; path edges | package emit/path edge + tests |

## LEAVE list

| Repo | Stars | Policy | Reason |
|---|---:|---|---|
| `kubernetes/kubernetes` | 126898 | disclosure | disclose AI in PRs; too large / SIG process for new-account first home — park |
| `nrwl/nx` | 29317 | silent | Monorepo mega-platform leave |
| `semantic-release/semantic-release` | 24028 | silent | Release automation - prefer lock/workspace/build CLIs |
| `bcicen/ctop` | 17838 | silent | last push mid-2024; appears low-maintenance — weak cadence for regression feedback |
| `kubesphere/kubesphere` | 17038 | silent | large platform UI; not quoting/build hunk class |
| `OpenRCT2/OpenRCT2` | 16197 | silent | game product; cmake incidental |
| `dutchcoders/transfer.sh` | 15892 | silent | file-sharing service, not build tool |
| `cheat/cheat` | 13446 | silent | docs cheatsheets, not product build tool |
| `gotenberg/gotenberg` | 13023 | silent | PDF convert API; weak build-tool fit |
| `diasurgical/DevilutionX` | 9722 | silent | game product; cmake incidental |
| `release-it/release-it` | 9050 | silent | Release CLI - secondary to package managers |
| `openshift/origin` | 8684 | silent | conformance/platform suite; heavy process |
| `googleapis/release-please` | 7462 | silent | Release-PR bot - process-heavy vs parser hunks |
| `fabiolb/fabio` | 7341 | silent | load balancer; networking sector better |
| `cilium/tetragon` | 4992 | silent | eBPF security observability — security sector |
| `arrayfire/arrayfire` | 4903 | silent | compute library — cmake incidental |
| `cdk-team/CDK` | 4745 | silent | security testing toolkit — better security sector |
| `opencontainers/image-spec` | 4470 | silent | OCI specification docs — not product CLI |
| `gofireflyio/aiac` | 3789 | silent | AI IaC generator — not build/packaging product for hunk class |
| `opencontainers/runtime-spec` | 3671 | silent | OCI runtime specification — not product CLI |
| `ContainerSolutions/k8s-deployment-strategies` | 3655 | silent | docs/examples — not product CLI |
| `gardener/gardener` | 3442 | silent | large hosted-control-plane platform — heavy process for first home |
| `cyclops-ui/cyclops` | 3322 | silent | K8s UI platform — not quoting/build CLI hunk class |
| `skyhook-io/radar` | 3281 | silent | K8s UI with MCP — platform UI not build CLI |
| `operacle/checkcle` | 2950 | silent | monitoring platform UI — weak build-tool fit |
| `docker-library/mysql` | 2585 | silent | official image packaging of app — not tool product |
| `docker-library/postgres` | 2515 | silent | official image packaging of app — not tool product |
| `tungbq/devops-basics` | 1880 | silent | tutorial/docs curriculum — not product |
| `mpusz/mp-units` | 1473 | silent | C++ units library — cmake incidental |

## Sector synthesis

- Refreshed after TS/JS/Zig DevEx product slice.
- No tracker comments/forks/third-party PRs.
- scored_at: `2026-09-08T17:38:01Z`

## Product deepen (≥5k★ subset) (2026-09-10, +57 scored)

Account: `vulragrag-star` · Curated devops/build product homes still missing after prior devops-build passes · Policy via `raw.githubusercontent.com` · **48** proceed / **9** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 45, 'disclosure': 11, 'hostility_risk': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `moby/moby` | 72073 | silent | Moby container engine; daemon/path/OCI edges | daemon config/path or OCI mount edge + Go tests |
| `nektos/act` | 71844 | silent | Run GitHub Actions locally; workflow/path/env edges | workflow YAML path / secret env edge + Go tests |
| `ansible/ansible` | 70621 | disclosure | IT automation CLI; module/path/inventory — AGENTS disclosure trailer | inventory/path or module arg edge + py tests — disclose AI |
| `apple/container` | 49759 | silent | Apple Linux container runtime CLI; path/config edges | container config/path or image ref edge + Swift/tests |
| `docker/compose` | 38127 | silent | Compose multi-container CLI; YAML/path/project edges | compose.yaml path / project name edge + Go tests |
| `firecracker-microvm/firecracker` | 36647 | silent | Secure microVM VMM; config/path/API edges — Amazon CLA/high bar | VM config JSON path / vsock edge + Rust tests — CLA |
| `k3s-io/k3s` | 33925 | disclosure | Lightweight Kubernetes distro CLI; install/config path — AI-assisted mention | install path / kubeconfig edge + Go tests — careful AI |
| `podman-container-tools/podman` | 32834 | disclosure | Podman engine CLI; image/path/quadlet — AGENTS AI policy | quadlet/path or image ref edge + Go tests — human-owned |
| `dokku/dokku` | 32126 | silent | Docker-powered PaaS CLI; app/path/plugin edges | app path / plugin hook edge + shell tests |
| `kubernetes/minikube` | 32113 | silent | Local Kubernetes CLI; driver/path/config edges | driver/path or addon config edge + Go tests |
| `helm/helm` | 30229 | silent | Kubernetes package manager CLI; chart/values/path edges | chart path / values quoting edge + Go tests |
| `opentofu/opentofu` | 30141 | silent | Terraform-compatible IaC CLI; HCL/path/state edges | module path / state backend edge + Go tests |
| `goharbor/harbor` | 29342 | silent | Cloud-native registry; project/path/policy edges | project path / retention policy edge + Go tests |
| `microsoft/vcpkg` | 27454 | silent | C/C++ package manager; port/path/triplet edges | portfile path / triplet edge + tests |
| `hashicorp/vagrant` | 27206 | silent | VM/dev env CLI; Vagrantfile/path/provider edges | Vagrantfile path / synced-folder edge + Ruby tests |
| `bazelbuild/bazel` | 25825 | silent | Hermetic build system; BUILD/path/label edges — high bar | label/path or remote-cache edge + Java tests — high bar |
| `pulumi/pulumi` | 25659 | disclosure | IaC in real languages; stack/path/config — AI policy disclosure | stack path / config key edge + Go tests — disclose AI |
| `argoproj/argo-cd` | 24114 | silent | GitOps continuous delivery; app/path/sync edges | app manifest path / sync option edge + Go tests |
| `containerd/containerd` | 21275 | disclosure | Container runtime; snapshot/path/OCI — AI-assisted mention | snapshotter path / image ref edge + Go tests — careful |
| `gradle/gradle` | 18832 | disclosure | Build system; task/path/config — AI_POLICY disclosure | task path / property edge + tests — AI_POLICY |
| `hashicorp/nomad` | 16862 | silent | Workload orchestrator CLI; job HCL/path edges | job HCL path / artifact edge + Go tests |
| `hashicorp/packer` | 15776 | silent | Image builder CLI; template/path/plugin edges | template path / provisioner edge + Go tests |
| `loft-sh/devpod` | 15191 | silent | Open-source codespaces client; provider/path edges | provider config / workspace path edge + Go tests |
| `basecamp/kamal` | 14575 | silent | Deploy CLI for Docker hosts; config/path/SSH edges | deploy.yml path / SSH dest edge + Ruby tests |
| `opencontainers/runc` | 13435 | disclosure | OCI runtime CLI; config/path — disclosure requirement | config.json path / namespace edge + Go tests — disclose |
| `infracost/infracost` | 12509 | silent | IaC cost estimate CLI; plan/path/usage edges | tfplan path / usage file edge + Go tests |
| `xmake-io/xmake` | 12212 | silent | Cross-platform build utility; lua/path/target edges | xmake.lua path / target edge + tests |
| `kubernetes-sigs/kustomize` | 12158 | silent | K8s config customization CLI; overlay/path edges | kustomization path / name-prefix edge + Go tests |
| `crossplane/crossplane` | 12041 | disclosure | Cloud control plane; XRD/path/compose — AI_POLICY | XRD/path or composition edge + Go tests — AI_POLICY |
| `podman-container-tools/skopeo` | 11225 | silent | Image copy/inspect CLI; ref/path/auth edges | image ref / auth file path edge + Go tests |
| `distribution/distribution` | 10607 | silent | OCI registry (CNCF Distribution); storage/path edges | storage root / manifest path edge + Go tests |
| `moby/buildkit` | 10243 | silent | BuildKit engine; LLB/path/cache edges | dockerfile path / cache key edge + Go tests |
| `tilt-dev/tilt` | 10041 | silent | K8s microdev CLI; Tiltfile/path/sync edges | Tiltfile path / live-update edge + Go tests |
| `gruntwork-io/terragrunt` | 9819 | silent | Terraform wrapper CLI; include/path/dependency edges | terragrunt.hcl path / dependency edge + Go tests |
| `conan-io/conan` | 9511 | silent | C/C++ package manager; recipe/path/profile edges | conanfile path / profile edge + py tests |
| `canonical/microk8s` | 9367 | silent | Local K8s snap distro; addon/path/config edges | addon enable / config path edge + py/tests |
| `testcontainers/testcontainers-java` | 8736 | silent | Testcontainers Java; image/mount/wait edges | mount path / wait strategy edge + JUnit tests |
| `kata-containers/kata-containers` | 8693 | disclosure | VM-isolated containers; config/path — disclosure | runtime config path / hypervisor edge + Go tests — disclose |
| `Kitware/CMake` | 8060 | disclosure | Cross-platform build generator; listfile/path — AI policy mention | CMakeLists path / generator edge + C++/CTest — careful AI |
| `concourse/concourse` | 7898 | silent | CI system; pipeline YAML/path/resource edges | pipeline path / resource type edge + Go tests |
| `k0sproject/k0s` | 6470 | silent | Zero-friction Kubernetes; install/config path edges | k0s.yaml path / install edge + Go tests |
| `sigstore/cosign` | 6292 | silent | Sigstore signing CLI; key/path/attest edges | key path / attest predicate edge + Go tests |
| `docker/cli` | 6048 | silent | Docker CLI; command/path/context edges | context path / compose project edge + Go tests |
| `terraform-linters/tflint` | 5806 | silent | Terraform linter CLI; rule/path/config edges | module path / rule config edge + Go tests |
| `fluxcd/flagger` | 5401 | silent | Progressive delivery operator; canary/path edges | canary target / metric path edge + Go tests |
| `apache/maven` | 5340 | silent | Java build tool; POM/path/plugin edges | pom path / plugin config edge + Java tests |
| `devspace-sh/devspace` | 5180 | silent | K8s develop/deploy CLI; config/path/sync edges | devspace.yaml path / sync edge + Go tests |
| `spack/spack` | 5121 | silent | HPC package manager; spec/path/concretize edges | spec syntax / package path edge + py tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `coollabsio/coolify` | 61542 | disclosure | Self-host PaaS control plane/UI — weak path/quoting farm vs engine/CLI homes |
| `portainer/portainer` | 38462 | silent | Docker/K8s management GUI — prefer engine/CLI product homes over dashboard UI |
| `Dokploy/dokploy` | 37158 | silent | PaaS alternative UI — leave product-web PaaS; prefer kamal/dokku/flyctl CLIs |
| `jenkinsci/jenkins` | 26531 | silent | Mega Java CI monolith — weak small path/quoting PR class; prefer concourse/act/agent |
| `rancher/rancher` | 25893 | silent | Full container mgmt platform UI/API — prefer rke2/k3s/minikube product CLIs |
| `louislam/dockge` | 24286 | silent | Compose YAML GUI manager — leave dashboard skins; prefer docker/compose CLI |
| `caprover/caprover` | 15154 | silent | PaaS (Docker+nginx) control plane — leave GUI/PaaS farms |
| `actions/runner` | 6248 | silent | GitHub Actions runner infra — internal high bar / empty policy surface; leave |
| `cloud-hypervisor/cloud-hypervisor` | 6209 | hostility_risk | Mentor-gated LLM / hostility_risk in CONTRIBUTING+AGENTS — leave |

Notes: Prefer container/runtime/build/IaC/GitOps CLIs (moby/podman/helm/opentofu/pulumi/argo-cd/buildkit/kamal/act/vcpkg/bazel/gradle). Disclosure/careful: ansible AGENTS, podman AGENTS, pulumi/crossplane/gradle AI_POLICY, k3s/containerd/runc/kata/CMake. Leave PaaS GUIs (coolify/dokploy/portainer/dockge/caprover), jenkins mega, rancher platform UI, actions/runner, cloud-hypervisor hostility_risk.

## Product deepen-2 (≥5k★ subset) (2026-09-11, +53 scored)

Account: `vulragrag-star` · Curated devops container/runtime/k8s-CLI/IaC/Nix/serverless product homes still missing after prior devops product deepen · Policy via `raw.githubusercontent.com` · **42** proceed / **11** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 50, 'disclosure': 3}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `abiosoft/colima` | 30766 | silent | macOS/Linux container runtime CLI; lima/docker path edges | VM disk/path or docker socket path edge + Go tests |
| `openfaas/faas` | 26236 | silent | OpenFaaS gateway/CLI stack; function YAML | stack.yml path / env edge + Go tests |
| `slimtoolkit/slim` | 23410 | silent | container image minify CLI; Dockerfile/path | include-path / http-probe edge + Go tests |
| `lima-vm/lima` | 21866 | silent | Linux VM CLI focused on containers; YAML/path/quoting | lima.yaml mount path / port forward edge + Go tests |
| `google/cadvisor` | 19417 | silent | container metrics agent; path/cgroup | cgroup path / docker endpoint edge + Go tests |
| `kubernetes-sigs/kubespray` | 18727 | silent | ansible k8s deploy; inventory/path | inventory path / group_vars edge + ansible tests |
| `labring/sealos` | 18341 | silent | cluster app deploy CLI; Clusterfile/path | Clusterfile path / app install edge + Go tests |
| `GoogleContainerTools/jib` | 14451 | silent | Java container build; path/layer | extra directory / entrypoint edge + Java tests |
| `89luca89/distrobox` | 12969 | silent | distro-in-terminal wrapper; shell path/quoting | image/name or home mount path quoting + shell tests |
| `siderolabs/talos` | 11142 | silent | Talos Linux for k8s; machine config/path | machineconfig path / patch edge + Go tests |
| `kubernetes/kompose` | 10623 | silent | Compose→K8s converter CLI; path/YAML | compose path / service convert edge + Go tests |
| `kedacore/keda` | 10517 | silent | event-driven autoscaler; ScaledObject YAML | scaler metadata / trigger path edge + Go tests |
| `reviewdog/reviewdog` | 9581 | silent | review annotation CLI; reporter/path | diff path / reporter config edge + Go tests |
| `runatlantis/atlantis` | 9285 | silent | Terraform PR automation; path/workspace | repo config path / plan output edge + Go tests |
| `kubernetes/autoscaler` | 8963 | silent | cluster autoscaler; config/path | node group config / expander edge + Go tests |
| `linuxkit/linuxkit` | 8649 | silent | secure OS image toolkit; YAML/path | pkg path / kernel config edge + Go tests |
| `kubevela/kubevela` | 7894 | silent | app platform CLI; appfile/path | appfile path / trait edge + Go tests |
| `chaos-mesh/chaos-mesh` | 7888 | silent | chaos engineering platform; experiment YAML | experiment path / selector edge + Go tests |
| `aws/karpenter-provider-aws` | 7715 | silent | k8s node autoscaler; NodePool YAML | NodePool requirement / EC2 path edge + Go tests |
| `operator-framework/operator-sdk` | 7678 | silent | operator scaffolding CLI; path/API | scaffold path / domain flag edge + Go tests |
| `cachix/devenv` | 7635 | silent | declarative Nix env; devenv.nix/path | devenv.nix path / shell hook edge + tests |
| `kubeedge/kubeedge` | 7570 | silent | edge k8s; device/path config | edgecore config path edge + Go tests |
| `kubevirt/kubevirt` | 7063 | silent | k8s VM API/runtime; VM YAML/path | disk path / cloud-init edge + Go tests |
| `aws/aws-sam-cli` | 6732 | disclosure | SAM build/deploy CLI — disclose AI | template path / build artifact edge + Python tests — disclose AI |
| `kubernetes-sigs/metrics-server` | 6716 | silent | metrics-server; kubelet path/config | kubelet cert path / metric scrape edge + Go tests |
| `k3d-io/k3d` | 6551 | silent | k3s-in-docker helper CLI; path/config | k3d.yaml volume / registry config edge + Go tests |
| `actions/actions-runner-controller` | 6490 | silent | GH Actions runner controller; CR path | RunnerDeployment path / scale edge + Go tests |
| `containers/podman-compose` | 6212 | silent | compose-on-podman; YAML/path/env | compose service path / env file edge + Python tests |
| `lxc/incus` | 6166 | silent | system container/VM manager CLI; path/config | instance config path / storage pool edge + Go tests |
| `knative/serving` | 6089 | silent | knative serving; service YAML/path | Service path / revision edge + Go tests |
| `goss-org/goss` | 5966 | silent | server validation CLI; YAML/path | goss.yaml path / command check edge + Go tests |
| `fnproject/fn` | 5944 | silent | fn serverless CLI; path/route | func.yaml path / route edge + Go tests |
| `volcano-sh/volcano` | 5939 | silent | batch scheduling; queue/job YAML | queue/job path edge + Go tests |
| `nuclio/nuclio` | 5755 | silent | high-perf serverless; function YAML/path | function.yaml path / build edge + Go tests |
| `cri-o/cri-o` | 5657 | silent | OCI CRI runtime; path/config | runtime path / cni conf edge + Go tests |
| `karmada-io/karmada` | 5619 | silent | multi-cluster orchestration; policy/path | propagation policy path edge + Go tests |
| `litmuschaos/litmus` | 5610 | silent | chaos engineering; chaosengine path | chaosengine path / probe edge + Go tests |
| `kubernetes-sigs/descheduler` | 5515 | silent | k8s descheduler; policy YAML/path | policy path / node selector edge + Go tests |
| `psviderski/uncloud` | 5486 | silent | lightweight container deploy CLI; path | compose/deploy path edge + Go tests |
| `eksctl-io/eksctl` | 5211 | silent | EKS CLI; cluster YAML/path | cluster.yaml path / addon config edge + Go tests |
| `helmfile/helmfile` | 5193 | silent | declarative helm deploy CLI; values/path | helmfile.yaml path / values quoting edge + Go tests |
| `diggerhq/digger` | 5044 | disclosure | IaC orchestration — disclose AI | project path / plan edge + Go tests — disclose AI |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `dapr/dapr` | 26091 | silent | Distributed app runtime mega — weak small path/quoting PR class vs CLI/build homes |
| `ansible/awx` | 15550 | silent | AWX web UI/API control plane — leave GUI; prefer ansible-runner/CLI homes |
| `hashicorp/terraform-provider-aws` | 11085 | disclosure | Provider plugin mega — prefer atlantis/terragrunt/CLI IaC homes over provider internals |
| `orbstack/orbstack` | 9305 | silent | Mostly proprietary product landing/docs repo — weak open contribution farm |
| `cloudnative-pg/cloudnative-pg` | 9282 | silent | Postgres operator — databases-storage sector, not devops-build deepen |
| `nginx-proxy/acme-companion` | 7726 | silent | Thin ACME companion for nginx-proxy — weak product farm |
| `stefanprodan/podinfo` | 5992 | silent | Demo microservice template — not a product contribution home |
| `weaveworks/scope` | 5909 | silent | Monitoring visualisation UI — leave dashboards |
| `devtron-labs/devtron` | 5595 | silent | Kubernetes dashboard/UI platform — leave GUIs |
| `tsuru/tsuru` | 5311 | silent | PaaS platform — prefer kamal/dokku/flyctl class already scored |
| `github/gh-aw` | 5127 | silent | GitHub Agentic Workflows product — leave agent workflow farms |

Notes: Prefer container/runtime CLIs (colima/lima/distrobox/cri-o/slim/talos/incus/k3d), k8s installer/autoscaler/CLI plugins (kubespray/kompose/eksctl/karpenter/helmfile/kubefwd), IaC PR automation (atlantis/digger/driftctl), Nix env/deploy (devenv/nh/colmena/deploy-rs), serverless CLIs (openfaas/fn/nuclio/sam-cli). Disclosure: gateway-api/kueue/sam-cli/digger/nh/apptainer. Leave GUIs (awx/devtron), provider plugins, PaaS megas, hard_ban s6-overlay.

## Midband product deepen (spill ≥5k★ if any) (2026-09-12, +10 scored)

Account: `vulragrag-star` · Curated devops-build midband (1k–5k★) product container/k8s/IaC/Nix/CI/ops CLI homes still missing after prior devops-build midband + product deepens · Policy via `raw.githubusercontent.com` · **6** proceed / **4** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 9, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `nix-community/home-manager` | 10340 | silent | Declarative user environment via Nix | home.nix option/path edge + Nix tests |
| `kubernetes-sigs/krew` | 7037 | silent | kubectl plugin manager CLI | krew install/index path edge + Go tests |
| `coreos/ignition` | 973 | silent | First-boot machine configuration (Ignition) | ignition config path/unit edge + Go tests |
| `containers/image` | 967 | silent | containers/image transport library (skopeo/podman shared) | image ref/transport parse edge + Go tests |
| `rootless-containers/slirp4netns` | 930 | silent | User-mode networking for rootless containers | slirp CIDR/MTU/netns path edge + C tests |
| `shipwright-io/build` | 821 | silent | K8s-native container build framework (Shipwright) | Build/BuildRun strategy path edge + Go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `semaphoreui/semaphore` | 14134 | silent | Ansible/Terraform UI control plane — AWX-class GUI leave |
| `podman-desktop/podman-desktop` | 7999 | silent | Podman Desktop GUI — leave GUIs; prefer podman/buildah CLIs |
| `getarcaneapp/arcane` | 7345 | hard_ban | AI_POLICY.md NO-AI — hard leave Docker management GUI |
| `terraform-aws-modules/terraform-aws-eks` | 5005 | silent | Terraform EKS module mega — provider/module leave |

Notes: Prefer midband product devops/build CLIs (container/OCI leftovers, k8s CLI/plugins/operators, IaC/policy CLIs, Nix/deploy/release CLIs, CI runner/ops CLIs, observability-adjacent ops products). Disclosure: grafana/alloy, crate-ci/cargo-release, sustainable-computing-io/kepler. Hard leave: getarcaneapp/arcane (NO-AI). Leave GUIs (podman-desktop/semaphore/zadig/monokle), awesome-lists/examples/official images, agent/MCP kits, DB/networking spills, Terraform modules, GH Actions satellites.

