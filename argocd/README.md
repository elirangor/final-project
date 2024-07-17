# Setting up Argo CD on Kubernetes

## Requirements
- Installed `kubectl` command-line tool.
- Connected to a Kubernetes cluster - Ensure you have a kubeconfig file (default location is `~/.kube/config`).

## Install Argo CD

#### 1. Create a new namespace named `argocd`:
```bash
kubectl create namespace argocd
```

#### 2. Apply the Argo CD installation manifests to the `argocd` namespace:
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

This will deploy Argo CD services and application resources within the `argocd` namespace.

#### 3. Retrieve the initial admin password:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d
```

## Access Argo CD Server

#### To access the Argo CD server, you can use port forwarding:

```bash
kubectl port-forward svc/argocd-server -n argocd 8081:443
```
This command will forward local port `8081` to the Argo CD server's HTTPS port (`443`) in the `argocd` namespace. Access the Argo CD UI via `https://localhost:8081` in your web browser.


## Clean ArgoCD namespace

```bash
kubectl delete ns argocd
```