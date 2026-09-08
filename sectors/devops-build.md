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
