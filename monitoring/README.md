# Setting up Prometheus and Grafana on Kubernetes

## Requirements
- Installed `kubectl` command-line tool.
- Connected to a Kubernetes cluster 

## Installation

#### 1. Create a new namespace named `monitoring`(if not created):
```bash
kubectl create namespace monitoring
```
#### 2. Run the following commands to add the helm chart
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
#### 3. Install Prometheus and Grafana Helm Chart on Kubernetes Cluster

```bash
helm install my-prometheus prometheus-community/kube-prometheus-stack --namespace monitoring
```

Output: 
```bash
NAME: my-prometheus
LAST DEPLOYED: Mon Jul  8 16:08:48 2024
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=my-prometheus"

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
```

#### 4. Check the resources in the namespace 

Run the next command:
```bash
kubectl get all -n monitoring
```

#### 5. Port forwarding Grafana and Prometheus 
Grafana:
```bash
k port-forward svc/my-prometheus-grafana -n monitoring 3000:80
```
Prometheus:
```bash
k port-forward svc/my-prometheus-kube-prometh-prometheus -n monitoring 9090:9090
```

#### 6. Username and password for grafana

Username: admin
Password: prom-operator

#### Creating rule (for after the creation of the app and pipelines)
```bash
helm upgrade my-prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  -f count-rule.yml
```