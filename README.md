# 🍽️ SOA Food Ordering System - Microservices Project

A microservices-based **Online Food Ordering System** built using **Python (Flask)**, **Docker**, **Kubernetes**, **CI/CD**, and **Consul Service Discovery**. This project simulates a real-world food ordering platform with multiple independent services and modern DevOps practices.

---

## 📦 Microservices Architecture

- **User Service**: Handles user registration, login, and authentication.
- **Restaurant Service**: Manages the restaurant data (menu, availability, etc).
- **Product Service**: Handles products and tracking.
- **Notification Service**: Sends email/SMS confirmations (mocked).

All services communicate via REST APIs and use **Consul for service discovery**.

---

## 📐 Architecture Diagram

![Architecture Diagram](./docs/architecture-diagram.png)


---

## ⚙️ Technologies Used

- Python (Flask)
- Docker & Docker Compose
- Kubernetes (Minikube)
- Consul (Service Discovery)
- Prometheus & Grafana (Monitoring)
- GitHub Actions (CI/CD)
- pytest (Testing)

---

## 🚀 Local Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Minikube (or Kind or Docker Desktop with K8s)
- kubectl
- Git
- Python 3.10+
- pip

---

### 1. Clone the Repository

```bash
git clone https://github.com/shonal11/SOA-Project.git
cd SOA-Project
