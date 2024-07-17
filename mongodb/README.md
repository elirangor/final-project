# Setting up MongoDB on a Kubernetes cluster

This guide provides step-by-step instructions for setting up MongoDB on Kubernetes using kind or minikube.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

- Docker (running on WSL for Windows users)
- kubectl

## Steps

### 1. Adding and updating Bitnami Helm repository

```bash 
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### 2. Deploying a simple MongoDB instance

Make Sure that the password, username and database names are in the python app.

```bash
helm install my-mongodb-release bitnami/mongodb \
  --set auth.enabled=true \
  --set auth.rootPassword=root \
  --set auth.username=root \
  --set auth.password=root \
  --set auth.database=mydatabasetest
```

### 3. Make sure that the service is up and running 

The output should look like it:
```bash 
ubuntuwsl@Eliran-6700K:~$ kubectl get svc
NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE
kubernetes                    ClusterIP   10.96.0.1        <none>        443/TCP     26h
my-mongodb                    ClusterIP   10.100.10.158    <none>        27017/TCP   26h
my-mongodb-arbiter-headless   ClusterIP   None             <none>        27017/TCP   26h
my-mongodb-headless           ClusterIP   None             <none>        27017/TCP   26h
```

the service that we look for is `my-mongodb`
