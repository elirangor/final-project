# Project Overview

## 1. Infrastructure Installation

This section details the setup and configuration of the essential components that support the application:

- **MongoDB**: Supplies the database services for storing application data.

- **Kubernetes (K8s)**: Oversees containerized applications, ensuring they operate efficiently and make effective use of resources.

- **Prometheus and Grafana**: Employed for monitoring the infrastructure and applications, gathering metrics, and offering insights through visualizations.

- **Jenkins**: Facilitates the automation of the continuous integration and continuous delivery (CI/CD) pipeline.

- **Argo CD**: Manages Kubernetes resources in a declarative way, guaranteeing reproducible and transparent deployments.

## 2. The application 

A Flask based web application that interacts with MongoDB. Built to be stateless, it integrates effortlessly into a Kubernetes-managed environment, enabling it to scale efficiently according to demand.
The app is simple. The user has to fill documents in the web page and has the option to delete or update them.

## 3. Deployment

The deployment process is automated using Jenkins and Argo CD:

- **Jenkins**: Manages the early stages of the CI pipeline, such as retrieving code, creating Docker images, and pushing these images to a registry.
- **Argo CD**: Deploys the application on Kubernetes by utilizing the latest Docker images and configurations specified in Helm charts.

## 4. Monitoring

Monitoring is set up using Prometheus and Grafana to provide real-time insights into the application's performance and infrastructure health:

- **Prometheus**: Collects and stores metrics as time-series data from Kubernetes and the Flask application.
- **Grafana**: Visualizes these metrics through customizable dashboards, tracking everything from system CPU and memory usage to application-specific metrics like request counts and response times.

## 5. Purpose of the Project

The primary goal of this project is to demonstrate a highly automated, scalable, and observable infrastructure setup for modern web applications. This setup enables:

- **Rapid Deployment**: Automated processes reduce the time from development to production.
- **Real-Time Monitoring and Alerting**: Ensures high availability and performance.
- **Streamlined Development Workflows**: Enhances efficiency and reduces deployment complexity.

## Conclusion

This project is an example of how modern tools can be combined in a Kubernetes environment to provide a robust platform for deploying and monitoring applications efficiently and effectively. It serves as a template that can be adapted and expanded for different use cases and environments.
