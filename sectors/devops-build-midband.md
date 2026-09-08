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
