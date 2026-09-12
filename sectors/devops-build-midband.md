# Sector survey: devops-build (midband 1k-5k)

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 64 | No hard ban in common paths |
| disclosure | 3 | AI disclosure language |

Proceed: **52** · Leave: **15**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
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

## Deepen pass (2026-09-09, +34 scored)

Account: `vulragrag-star` · Curated product midband slice from remaining unscored devops-build leftovers + curated container/build/CD fills · Policy via `raw.githubusercontent.com` · **25** proceed / **9** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 33, 'disclosure': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `terraform-docs/terraform-docs` | 4818 | silent | Generate Terraform module docs CLI; path/format/config edges | module path / output format edge + Go tests |
| `gomods/athens` | 4795 | silent | Go module proxy/datastore; storage/path/protocol edges | module path / storage backend edge + Go tests |
| `NVIDIA/nvidia-container-toolkit` | 4546 | silent | NVIDIA container runtime toolkit; CDI/config/path edges for GPU containers | runtime config / CDI path edge + Go tests |
| `facebook/buck2` | 4417 | silent | Buck2 multi-language build system; target/path/remote-exec edges | BUCK target/path or remote-cache edge + Rust tests |
| `nicholas-fedor/watchtower` | 4399 | silent | Automate Docker container image updates; label/schedule/registry edges | watch label / registry auth path edge + Go tests |
| `purpleidea/mgmt` | 4314 | silent | Event-driven parallel config management; graph/path/resource edges | resource graph/path edge + Go tests |
| `iterative/cml` | 4186 | silent | CI/CD for ML reports/comments CLI; path/token/provider edges | cml report/path or provider edge + JS tests |
| `google/go-containerregistry` | 4037 | silent | crane/gcrane OCI registry CLIs; mutate/copy/digest edges | crane mutate/copy/ref edge + Go tests |
| `genuinetools/img` | 3987 | silent | Daemon-less Dockerfile/OCI image builder CLI; rootless BuildKit-class surface | Dockerfile/path or rootless build edge + Go tests |
| `dagucloud/dagu` | 3844 | silent | Self-hostable workflow orchestrator CLI; DAG/path/schedule edges | DAG yaml path / step edge + Go tests |
| `composerize/composerize` | 3756 | silent | docker run → compose translator CLI; flag/quoting parse edges | docker-run flag parse / quoting edge + JS tests |
| `buildpacks/pack` | 3002 | silent | Cloud Native Buildpacks pack CLI; builder/path/env edges | pack build builder/path/env edge + Go tests |
| `ofek/pyapp` | 2029 | silent | Runtime installer for Python applications; path/embed edges | install path / embed config edge + Rust tests |
| `jkroepke/helm-secrets` | 2027 | silent | Helm secrets plugin; values decrypt/path/backend edges | secrets values path / backend edge + shell tests |
| `genuinetools/reg` | 1710 | silent | Docker registry v2 CLI for listing/tags/digests; registry ref edges | registry ref/tag/digest path edge + Go tests |
| `kimdre/doco-cd` | 1649 | silent | Docker Compose continuous deployment tool; compose/path/webhook edges | compose file path / deploy trigger edge + Go tests |
| `cabinpkg/cabin` | 1499 | silent | Cargo-inspired C/C++ package manager + build system; manifest/path edges | cabin.toml path / build target edge + Rust tests |
| `cloud66-oss/habitus` | 1401 | silent | Docker build-flow tool; habitus.yml path/secrets edges | habitus.yml path / secret mount edge + Go tests |
| `ekristen/aws-nuke` | 1401 | silent | AWS account resource cleanup CLI; config/filter/path edges | nuke config path / resource filter edge + Go tests |
| `Lifailon/lazyjournal` | 1398 | silent | TUI for journald/Docker/Podman logs; unit/container filter edges | unit/container filter path edge + Go tests |
| `cloudposse/atmos` | 1373 | silent | Atmos infra runtime for Terraform/Helm stacks; stack/path/config edges | stack yaml path / terraform var edge + Go tests |
| `pipe-cd/pipecd` | 1353 | silent | Multi-platform continuous delivery; app/config/path edges | app config path / sync edge + Go tests |
| `swiftlang/swift-llbuild` | 1277 | silent | Low-level build system used by Xcode/SwiftPM; Ninja-like path/target edges | build graph/path or target edge + C++ tests |
| `fastforgedev/fastforge` | 1142 | silent | Build/package/publish CLI for shipping apps; path/target edges | package/publish path edge + Rust tests |
| `hcavarsan/pipedash` | 1080 | silent | Multi-provider CI/CD pipeline manager (desktop/self-host); pipeline path edges | pipeline config/path edge + Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `ovh/cds` | 4839 | silent | Enterprise CD platform — heavy process / large surface for first home |
| `lucaslorentz/caddy-docker-proxy` | 4639 | silent | Caddy reverse-proxy for Docker — networking proxy, not build/packaging CLI |
| `virtual-kubelet/virtual-kubelet` | 4563 | silent | Kubelet implementation / provider runtime — platform, not build/packaging CLI hunk class |
| `Project-HAMi/HAMi` | 4526 | disclosure | Heterogeneous GPU sharing K8s platform — operator/platform UI class, not build CLI |
| `ory/dockertest` | 4525 | silent | Go library for ephemeral Docker testcontainers — library not product CLI |
| `kubernetes-sigs/aws-load-balancer-controller` | 4323 | silent | AWS load-balancer operator — cloud networking, better networking-distributed |
| `kubernetes-sigs/cluster-api` | 4301 | silent | Large SIG Cluster API platform — heavy process for first atlas home |
| `create-go-app/cli` | 2771 | silent | Project scaffolder CLI — template generator, not build/packaging product farm |
| `juju/juju` | 2662 | silent | Large orchestration platform — process-heavy, weak small hunk class |

Notes: Prefer container/registry/build-system/Helm/CD CLI surfaces with regression tests. Leave kubelet/SIG platforms, AWS LB operators, GPU-sharing platforms, enterprise CD monoliths, project scaffolders, Go test libraries, and reverse-proxy sidecars.

## Product deepen midband subset (2026-09-10, +9 scored)

Account: `vulragrag-star` · Curated devops/build product homes still missing after prior devops-build passes · Policy via `raw.githubusercontent.com` · **8** proceed / **1** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 9}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `garden-io/garden` | 3611 | silent | K8s/cloud develop CLI; garden.yml/path edges | garden.yml path / build action edge + TS tests |
| `argoproj/argo-rollouts` | 3572 | silent | Progressive delivery controller; rollout/path edges | rollout strategy / analysis path edge + Go tests |
| `digitalocean/doctl` | 3449 | silent | DigitalOcean CLI; resource/path/config edges | config path / droplet create edge + Go tests |
| `argoproj/argo-events` | 2689 | silent | Event-driven workflow; EventSource/path edges | EventSource path / sensor edge + Go tests |
| `rancher/rke2` | 2338 | silent | Rancher Kubernetes engine; config/path edges | config.yaml path / CIS profile edge + Go tests |
| `superfly/flyctl` | 1702 | silent | Fly.io deploy CLI; fly.toml/path/remote edges | fly.toml path / remote builder edge + Go tests |
| `carvel-dev/kapp` | 1081 | silent | K8s app deploy CLI; app/path/diff edges | app YAML path / diff change-group edge + Go tests |
| `buildkite/agent` | 1058 | silent | Buildkite CI agent; pipeline/path/hook edges | pipeline path / hook env edge + Go tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `tonistiigi/binfmt` | 1527 | silent | Thin QEMU binfmt register helper — weak product farm vs buildkit/cli |

Notes: Prefer midband deploy/CI/agent CLIs (flyctl/kapp/buildkite-agent/rke2/doctl/argo-events/rollouts/garden/devspace). Leave thin binfmt helpers.

## Product deepen-2 midband subset (2026-09-11, +48 scored)

Account: `vulragrag-star` · Curated devops container/runtime/k8s-CLI/IaC/Nix/serverless product homes still missing after prior devops product deepen · Policy via `raw.githubusercontent.com` · **33** proceed / **15** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 43, 'disclosure': 4, 'hard_ban': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mutagen-io/mutagen` | 4419 | silent | file sync + forward CLI; path/ignore | sync path / ignore rule edge + Go tests |
| `whalebrew/whalebrew` | 4247 | silent | homebrew-like docker CLI packages; path | package install path / image edge + Go tests |
| `txn2/kubefwd` | 4168 | silent | bulk service port-forward CLI; kubeconfig/path | namespace/service select / kubeconfig edge + Go tests |
| `helm/chartmuseum` | 3843 | silent | helm chart repo server; path/storage | chart storage path / index edge + Go tests |
| `databus23/helm-diff` | 3491 | silent | helm diff plugin; release/path | manifest diff / values path edge + Go tests |
| `ahmetb/kubectl-tree` | 3423 | silent | kubectl plugin; object hierarchy | GVK/name parse edge + Go tests |
| `wowu/docker-rollout` | 3334 | silent | compose zero-downtime deploy; service/path | compose service / healthcheck edge + shell tests |
| `open-policy-agent/conftest` | 3259 | silent | config policy tests CLI; path/rego | policy path / input parse edge + Go tests |
| `nix-community/nh` | 3191 | disclosure | Nix CLI helper — disclose AI | flake path / generation edge + Rust tests — disclose AI |
| `yannh/kubeconform` | 3186 | silent | k8s manifest validator CLI; path/schema | manifest path / schema cache edge + Go tests |
| `kubernetes-sigs/kwok` | 3184 | silent | fake kubelet simulator; config/path | stage config path / node template edge + Go tests |
| `gruntwork-io/cloud-nuke` | 3182 | silent | cloud cleanup CLI; resource filter/path | resource filter / region config edge + Go tests |
| `kubernetes-sigs/gateway-api` | 2995 | disclosure | Gateway API CRDs; YAML/path — disclose AI | HTTPRoute path match / gateway ref edge + Go tests — disclose AI |
| `kubernetes-sigs/kueue` | 2963 | disclosure | job queueing — disclose AI (K8s policy) | ClusterQueue / LocalQueue path edge + Go tests — disclose AI |
| `kubernetes-sigs/controller-runtime` | 2953 | silent | controller lib used by operators; path/scheme | scheme/builder path edge + Go tests — library bar |
| `devcontainers/cli` | 2948 | silent | devcontainer CLI; json/path | devcontainer.json path / feature edge + TS tests |
| `kubesphere/kubekey` | 2865 | silent | k8s installer CLI; config/path | config path / addons edge + Go tests |
| `snyk/driftctl` | 2663 | silent | infra drift detect CLI; state/path | tfstate path / filter edge + Go tests |
| `cycloidio/terracognita` | 2390 | silent | cloud→tf import CLI; provider/path | resource filter / output path edge + Go tests |
| `nix-community/colmena` | 2340 | silent | NixOS deploy tool; hive/path | hive.nix path / target edge + Rust tests |
| `serokell/deploy-rs` | 2311 | silent | Nix flake deploy tool; profile/path | deploy flake path / profile edge + Rust tests |
| `openfaas/faas-netes` | 2170 | silent | OpenFaaS on k8s; function CR path | Function CR path / secret edge + Go tests |
| `sealerio/sealer` | 2093 | silent | cluster+image build/run CLI; path | Clusterfile path / image build edge + Go tests |
| `cycloidio/inframap` | 2064 | silent | tfstate/HCL graph CLI; path | tfstate path / graph edge + Go tests |
| `zhaofengli/attic` | 2063 | silent | Nix binary cache; path/auth | cache path / narinfo edge + Rust tests |
| `apptainer/apptainer` | 1962 | disclosure | HPC app containers; path/SIF — disclose AI | bind path / sif create edge + Go tests — disclose AI |
| `operator-framework/operator-lifecycle-manager` | 1861 | silent | OLM operator lifecycle; CSV/path | CSV path / catalog source edge + Go tests |
| `argoproj-labs/argocd-image-updater` | 1717 | silent | Argo CD image updater; annotation/path | image list / write-back path edge + Go tests |
| `knative/eventing` | 1552 | silent | knative eventing; trigger/path | Trigger broker path edge + Go tests |
| `bazel-contrib/rules_go` | 1484 | silent | Bazel Go rules; path/label | go_library path / embed edge + Go tests |
| `moonrepo/proto` | 1406 | silent | multi-lang version manager; tool/path | tool version / shim path edge + Rust tests |
| `rootless-containers/rootlesskit` | 1303 | silent | rootless fake-root helper; argv/path | path mapping / port driver edge + Go tests |
| `ansible/ansible-runner` | 1085 | silent | ansible runner lib/CLI; path/inventory | playbook path / inventory edge + Python tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `wallix/awless` | 4955 | silent | Unmaintained AWS CLI alternative — weak cadence |
| `just-containers/s6-overlay` | 4583 | hard_ban | CONTRIBUTING hard ban: does not accept LLM-generated contributions |
| `bitnami/containers` | 4459 | silent | Container image catalog — packaging farm not product CLI |
| `oxequa/realize` | 4434 | silent | Unmaintained Go task runner — weak cadence |
| `moby/swarmkit` | 3651 | silent | Swarm orchestration toolkit — legacy/low product CLI surface vs compose/buildkit |
| `dragonflyoss/dragonfly` | 3326 | silent | P2P distribution — networking-distributed adjacency |
| `im2nguyen/rover` | 3325 | silent | Terraform visualization UI — leave viz apps |
| `docker/docker-install` | 3173 | silent | Install script only — not an ongoing product CLI |
| `mitogen-hq/mitogen` | 2533 | silent | Python distributed exec library — leave libs vs ansible-runner CLI |
| `kuberhealthy/kuberhealthy` | 2266 | silent | Synthetic check operator — monitoring adjacency |
| `openshift/openshift-ansible` | 2221 | silent | Legacy OpenShift 3.x installer — prefer kubekey/kubespray/talos |
| `projectcapsule/capsule` | 2176 | silent | Multi-tenancy framework — policy mega vs path/quoting farm |
| `konstructio/kubefirst` | 2058 | silent | Full platform installer mega — weak small hunk class |
| `siderolabs/omni` | 1375 | silent | SaaS control plane for Talos — prefer siderolabs/talos CLI |
| `weaveworks/weave-gitops` | 1130 | silent | Transitioning/community wind-down — skip |

Notes: Prefer midband CLI/plugins (kubeconform/conftest/helm-diff/chartmuseum/whalebrew/docker-rollout/rootlesskit/proto/rules_go). Leave install scripts, demo apps, unmaintained CLIs.

## Midband product deepen (2026-09-12, +91 scored)

Account: `vulragrag-star` · Curated devops-build midband (1k–5k★) product container/k8s/IaC/Nix/CI/ops CLI homes still missing after prior devops-build midband + product deepens · Policy via `raw.githubusercontent.com` · **63** proceed / **28** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 86, 'disclosure': 5}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `NilsIrl/dockerc` | 4919 | silent | Compile OCI images to standalone executables CLI | image→binary path/entrypoint edge + Go tests |
| `flipt-io/flipt` | 4896 | silent | Feature flag server & CLI product | flipt flag/segment path edge + Go tests |
| `cdk8s-team/cdk8s` | 4854 | silent | Define Kubernetes apps with code (cdk8s) | cdk8s synth app path edge + TypeScript tests |
| `jonmosco/kube-ps1` | 3811 | silent | Shell prompt helper for kubectl context/namespace | prompt format/context edge + shell tests |
| `getwud/wud` | 3803 | silent | Watch and update Docker containers CLI | wud watch registry/tag edge + JS tests |
| `doitintl/kube-no-trouble` | 3680 | silent | Detect deprecated Kubernetes APIs in cluster/manifests | kubent API version/manifest path edge + Go tests |
| `grafana/alloy` | 3531 | disclosure | OpenTelemetry Collector distribution CLI (disclosure AGENTS) | alloy run config path edge + Go tests — disclose AI |
| `nix-community/nixos-anywhere` | 3437 | silent | Install NixOS over SSH (often with disko) | nixos-anywhere disk-layout/path edge + Nix tests |
| `nix-community/disko` | 3316 | silent | Declarative disk partitioning for NixOS | disko device/partition path edge + Nix tests |
| `openfaas/faasd` | 3277 | silent | Lightweight OpenFaaS without full Kubernetes | faasd up/provider path edge + Go tests |
| `nix-community/NixOS-WSL` | 3089 | silent | NixOS on WSL integration | wsl module/path edge + Nix tests |
| `pulumi/kubespy` | 3083 | silent | Watch Kubernetes resources in real time CLI | kubespy status/trace edge + Go tests |
| `kubernetes-sigs/kro` | 3034 | silent | Kube Resource Orchestrator (ResourceGraphDefinition) | RGD schema/path edge + Go tests |
| `projen/projen` | 2953 | silent | Project config synthesizer CLI | projen synth/.projenrc path edge + TypeScript tests |
| `sagiegurari/cargo-make` | 2950 | silent | Rust task runner (cargo-make) | Makefile.toml task/path edge + Rust tests |
| `firecracker-microvm/firecracker-containerd` | 2926 | silent | Firecracker + containerd runtime integration | snapshotter/VM config path edge + Go tests |
| `microvm-nix/microvm.nix` | 2920 | silent | Declarative NixOS MicroVMs | microvm hypervisor/config edge + Nix tests |
| `kcp-dev/kcp` | 2821 | silent | Kubernetes-like control planes for multi-tenancy | workspace/APIExport path edge + Go tests |
| `LukeMathWalker/cargo-chef` | 2704 | silent | Cache Rust Docker layers via cargo-chef | chef prepare/cook path edge + Rust tests |
| `grafana/tanka` | 2686 | silent | Jsonnet Kubernetes config CLI (tk) | tk apply/env path edge + Go tests |
| `robscott/kube-capacity` | 2667 | silent | Cluster capacity overview kubectl plugin | kube-capacity filter/context edge + Go tests |
| `flant/shell-operator` | 2605 | silent | Run shell hooks as Kubernetes operators | hook config/binding path edge + Go tests |
| `openshift/source-to-image` | 2544 | silent | S2I source→image builder CLI | s2i build source/builder path edge + Go tests |
| `GoogleContainerTools/container-structure-test` | 2496 | silent | Assert container image filesystem/metadata CLI | structure-test config path edge + Go tests |
| `intuit/auto` | 2494 | silent | Label-driven semantic release CLI | auto shipit/label edge + TypeScript tests |
| `ryantm/agenix` | 2482 | silent | age-encrypted secrets for NixOS/HM | agenix secret path/rekey edge + Nix tests |
| `myoung34/docker-github-actions-runner` | 2451 | silent | Self-hosted GitHub Actions runner container | runner label/org/env edge + shell tests |
| `k3s-io/kine` | 2406 | silent | etcd-API on SQL for lightweight clusters | kine DSN/driver path edge + Go tests |
| `bitnami/minideb` | 2216 | silent | Minimal Debian base image recipes for containers | package install recipe path edge + shell tests |
| `axodotdev/cargo-dist` | 2114 | silent | Shippable application packaging / release CLI | dist init/plan path edge + Rust tests |
| `zarf-dev/zarf` | 2038 | silent | Airgap-native Kubernetes package manager CLI | zarf package create/path edge + Go tests |
| `willfarrell/docker-autoheal` | 1995 | silent | Restart unhealthy Docker containers sidecar | autoheal label/socket path edge + shell tests |
| `sil-org/ecs-deploy` | 1984 | silent | Blue-green deploy helper for AWS ECS | ecs-deploy service/image edge + shell tests |
| `nix-community/impermanence` | 1886 | silent | Ephemeral root with selective persistence (NixOS) | persistence path/module edge + Nix tests |
| `nix-community/lanzaboote` | 1839 | silent | Secure Boot for NixOS (lanzaboote) | lanzaboote UKI/path edge + Rust/Nix tests |
| `mrjackwills/oxker` | 1834 | silent | Docker container TUI controller | oxker action/filter edge + Rust tests |
| `yonahd/kor` | 1822 | silent | Find unused Kubernetes resources CLI | kor unused resource/namespace edge + Go tests |
| `norwoodj/helm-docs` | 1765 | silent | Auto-generate Helm chart README docs CLI | chart path/values edge + Go tests |
| `open-telemetry/opentelemetry-operator` | 1755 | silent | OpenTelemetry Collector Kubernetes operator | OpenTelemetryCollector CR path edge + Go tests |
| `ostreedev/ostree` | 1681 | silent | OSTree content-addressed filesystem CLI | ostree commit/ref/repo path edge + C tests |
| `containers/podlet` | 1640 | silent | Generate Podman Quadlet units from compose/command | compose→quadlet path/volume edge + Rust tests |
| `crate-ci/cargo-release` | 1588 | disclosure | Cargo release subcommand (disclosure AI_POLICY) | cargo release version/path edge + Rust tests — disclose AI |
| `containerd/stargz-snapshotter` | 1587 | silent | Lazy-pulling stargz snapshotter plugin | stargz resolve/ref edge + Go tests |
| `sustainable-computing-io/kepler` | 1566 | disclosure | K8s power/energy exporter (disclosure CONTRIBUTING) | kepler metric/cgroup path edge + Go tests — disclose AI |
| `mkubaczyk/helmsman` | 1492 | silent | Helm Charts as Code desired-state CLI | helmsman desired-state path edge + Go tests |
| `liquidmetal-dev/flintlock` | 1490 | silent | MicroVM lifecycle manager for Firecracker/Cloud Hypervisor | microvm create/config path edge + Go tests |
| `orlangure/gnomock` | 1488 | silent | Ephemeral Docker test containers (Gnomock) | gnomock preset/port edge + Go tests |
| `ipetkov/crane` | 1460 | silent | Nix library for cargo builds without IFD | crane buildDepOnly path edge + Nix tests |
| `kuasar-io/kuasar` | 1452 | silent | Multi-sandbox container runtime (wasm/VM) | sandbox config/path edge + Rust/Go tests |
| `getporter/porter` | 1424 | silent | CNAB application packaging CLI (Porter) | porter build/install mixin path edge + Go tests |
| `poseidon/matchbox` | 1423 | silent | Network boot / PXE provisioner for Flatcar/FCOS | matchbox profile/ignition path edge + Go tests |
| `aws-cloudformation/cloudformation-guard` | 1388 | silent | cfn-guard policy-as-code validation CLI | guard validate rule/template path edge + Rust tests |
| `crc-org/crc` | 1386 | silent | CRC local OpenShift/OKD VM CLI | crc start preset/path edge + Go tests |
| `kube-green/kube-green` | 1373 | silent | Schedule sleep/wake for K8s namespaces (CO2) | SleepInfo CR schedule edge + Go tests |
| `Mirantis/cri-dockerd` | 1366 | silent | CRI shim wrapping dockerd for Kubernetes | cri socket/docker endpoint path edge + Go tests |
| `k8gb-io/k8gb` | 1317 | silent | Kubernetes Global Balancer operator | Gslb CR/DNS edge + Go tests |
| `containers/podman-tui` | 1223 | silent | Podman terminal UI for container/image ops | TUI action/filter edge + Go tests |
| `cachix/cachix` | 1118 | silent | Nix binary cache client CLI | cachix push/watch path edge + Haskell tests |
| `genuinetools/amicontained` | 1089 | silent | Container introspection CLI (capabilities/seccomp) | amicontained runtime detect edge + Go tests |
| `buildpacks-community/kpack` | 1084 | silent | K8s-native Cloud Native Buildpacks controller | Image/Builder CR path edge + Go tests |
| `python-semantic-release/python-semantic-release` | 1058 | silent | Python SemVer release automation CLI | psr version/changelog path edge + Python tests |
| `cloudposse/geodesic` | 1052 | silent | Geodesic DevOps toolbox container/CLI | geodesic wrapper path/env edge + shell tests |
| `coreos/rpm-ostree` | 1022 | silent | Atomic hybrid image/package host tooling | rpm-ostree override/compose path edge + C++/Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `JamesIves/github-pages-deploy-action` | 4606 | silent | GitHub Action for Pages deploy — Action satellite leave |
| `IBM/mcp-context-forge` | 4463 | disclosure | MCP/AI gateway registry — agent/MCP kit leave |
| `NVIDIA/k8s-device-plugin` | 3871 | silent | NVIDIA device plugin — GPU plugin leave |
| `welliamcao/OpsManage` | 3594 | silent | Chinese ops/CMDB/CI GUI platform — not product CLI |
| `collabnix/kubetools` | 3474 | silent | Curated Kubernetes tools list — awesome-list leave |
| `dorny/paths-filter` | 3328 | silent | GitHub Action paths filter — Action satellite leave |
| `docker/docker-agent` | 3320 | silent | Docker AI Agent Builder/Runtime — leave AI-agent product |
| `koderover/zadig` | 3244 | silent | AI-powered DevOps platform UI — process-heavy platform leave |
| `instrumenta/kubeval` | 3231 | silent | Archived kubeval — prefer kubeconform (already scored) |
| `apecloud/kubeblocks` | 3122 | silent | Multi-DB Kubernetes operator — databases-storage spill |
| `rancher/local-path-provisioner` | 2941 | silent | Local PV provisioner — storage provisioner leave |
| `NVIDIA/gpu-operator` | 2872 | silent | NVIDIA GPU Operator platform — heavy operator leave |
| `erda-project/erda` | 2754 | silent | Enterprise cloud-native platform mega — not CLI hunk farm |
| `awslabs/amazon-eks-ami` | 2669 | silent | Packer EKS AMI recipes — AMI scripts leave |
| `apptainer/singularity` | 2622 | silent | Legacy Singularity rename tree — prefer apptainer/apptainer |
| `ublue-os/bluefin` | 2590 | disclosure | Opinionated Linux workstation image — OS image product leave |
| `GhostWriters/DockSTARTer` | 2570 | silent | Docker compose starter-kit helper — example/starter leave |
| `Kong/kubernetes-ingress-controller` | 2411 | silent | Kong ingress controller — networking-distributed spill |
| `LeanerCloud/AutoSpotting` | 2369 | silent | AWS Spot cost automation service — cloud platform leave |
| `kubeshop/monokle` | 2141 | silent | Kubernetes YAML IDE/GUI suite — prefer CLI homes |
| `poseidon/typhoon` | 2053 | silent | Full Kubernetes distro with Terraform — distribution mega leave |
| `docker-library/wordpress` | 1976 | silent | Docker Official Image for WordPress — image recipe leave |
| `HariSekhon/Dockerfiles` | 1379 | silent | Dockerfile/image dump — not product CLI |
| `fluxcd/flux2-kustomize-helm-example` | 1297 | silent | Flux GitOps example repo — demo/example leave |
| `adoptium/temurin-build` | 1164 | silent | Temurin JDK build scripts — compilers-runtimes spill |
| `marhkb/pods` | 1087 | silent | GTK GUI for Podman — desktop UI leave |
| `BagelHole/DevOps-Security-Agent-Skills` | 1085 | silent | Agent-skills / AI devops kit — leave agent farms |
| `in-toto/in-toto` | 1036 | silent | in-toto supply-chain framework — security-crypto spill |

Notes: Prefer midband product devops/build CLIs (container/OCI leftovers, k8s CLI/plugins/operators, IaC/policy CLIs, Nix/deploy/release CLIs, CI runner/ops CLIs, observability-adjacent ops products). Disclosure: grafana/alloy, crate-ci/cargo-release, sustainable-computing-io/kepler. Hard leave: getarcaneapp/arcane (NO-AI). Leave GUIs (podman-desktop/semaphore/zadig/monokle), awesome-lists/examples/official images, agent/MCP kits, DB/networking spills, Terraform modules, GH Actions satellites.

