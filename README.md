# 🚀 MLOps Deployment Demo  

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) 
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) 
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white) 
![AWS SageMaker](https://img.shields.io/badge/AWS-SageMaker-orange?logo=amazonaws&logoColor=white) 
![License: MIT](https://img.shields.io/badge/License-MIT-green)  

---

## 📑 Table of Contents
- [Description](#-description)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [Quickstart](#-quickstart)
- [Future Work](#-future-work)
- [MLOps Workflow](#-mlops-workflow)

---

## 📖 Description  
End‑to‑end MLOps pipeline demo showcasing model training, packaging, and deployment with **FastAPI**, **Docker**, **MLflow**, and **AWS SageMaker**. Includes **CI/CD workflows** via GitHub Actions and **monitoring scripts** for performance tracking and drift detection.  

---

## 📦 Features  
- FastAPI service for model inference  
- Dockerized deployment for portability  
- MLflow for experiment tracking & model registry  
- AWS SageMaker integration for scalable training & hosting  
- CI/CD workflows with GitHub Actions  
- Monitoring scripts for performance & drift detection  

---

## 🛠 Tech Stack  
- **Languages:** Python  
- **Frameworks:** FastAPI, MLflow  
- **Deployment:** Docker, AWS SageMaker  
- **CI/CD:** GitHub Actions  
- **Monitoring:** Prometheus, Grafana (optional)  

---

## 📂 Repository Structure  
mlops-deployment-demo/  
├── src/                  # Source code for training & inference  
│   ├── train_model.py    # Model training script  
│   ├── inference.py      # FastAPI inference service  
│   └── monitoring.py     # Drift detection & performance monitoring  
├── docker/               # Dockerfiles for containerization  
├── workflows/            # GitHub Actions CI/CD pipelines  
├── requirements.txt      # Python dependencies  
├── README.md             # Project documentation  
├── LICENSE               # MIT License  
└── .gitignore            # Ignore build and environment files  

---

## ⚡ Quickstart  
Clone the repo and install dependencies:  
```bash
git clone https://github.com/melessemenelik/mlops-deployment-demo.git
cd mlops-deployment-demo
pip install -r requirements.txt
uvicorn src.inference:app --reload
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

## 🏗️ Architecture Diagram

This project demonstrates end‑to‑end MLOps deployment:

                 ┌───────────────────────────────┐
                 │     Development Environment   │
                 │  Python Source + Training     │
                 │  FastAPI Inference Service    │
                 └───────────────┬───────────────┘
                                 │
                                 ▼
                 ┌───────────────────────────────┐
                 │   Experiment Tracking Layer   │
                 │  MLflow Tracking + Registry   │
                 └───────────────┬───────────────┘
                                 │
                                 ▼
                 ┌───────────────────────────────┐
                 │   Deployment Layer            │
                 │  Docker Containerized Service │
                 │  AWS SageMaker Hosting        │
                 └───────────────┬───────────────┘
                                 │
                                 ▼
                 ┌───────────────────────────────┐
                 │   CI/CD Pipeline              │
                 │  GitHub Actions Automation    │
                 └───────────────┬───────────────┘
                                 │
                                 ▼
                 ┌───────────────────────────────┐
                 │   Monitoring & Drift Detection│
                 │  Prometheus / Grafana Alerts  │
                 └───────────────────────────────┘

Key components:
- **[Development](ca://s?q=Explain_development_environment_in_MLOps)**: Python code, FastAPI service, training scripts  
- **[Experiment tracking](ca://s?q=Explain_experiment_tracking_with_MLflow)**: MLflow server + model registry  
- **[Deployment](ca://s?q=Explain_docker_and_SageMaker_deployment)**: Dockerized service hosted on AWS SageMaker  
- **[CI/CD](ca://s?q=Explain_CI_CD_in_MLOps)**: GitHub Actions automating build and deploy  
- **[Monitoring](ca://s?q=Explain_monitoring_and_drift_detection_in_MLOps)**: Prometheus/Grafana dashboards and alerts

## 🔄 MLOps Workflow  

```mermaid
flowchart LR
    A[Data Ingestion] --> B[Model Training]
    B --> C[Experiment Tracking (MLflow)]
    C --> D[Model Packaging (Docker)]
    D --> E[Deployment (FastAPI + AWS SageMaker)]
    E --> F[CI/CD (GitHub Actions)]
    F --> G[Monitoring & Drift Detection] ```
