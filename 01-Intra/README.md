# 🚀 MLOps Zoomcamp 2025 – Week 1: Introduction

Welcome to the Introduction module of the **MLOps Zoomcamp 2025** by [Shrikant-Ganji](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025)!

This week sets the foundation for your journey into Machine Learning Operations (MLOps). You’ll become familiar with the course structure, prepare your development environment, and gain an understanding of key MLOps concepts and their significance in real-world projects.

---

## Table of Contents

1. [Introduction to MLOps](#1-introduction-to-mlops)
2. [Environment Preparation](#2-environment-preparation)
   - [Using GitHub Codespaces](#21-using-github-codespaces)
   - [Working Locally or on Cloud VMs](#22-working-locally-or-on-cloud-vms)
   - [Using Installers (Simpler Option)](#23-using-installers-simpler-option)
3. [Training a Ride Duration Prediction Model](#3-training-a-ride-duration-prediction-model)
4. [Course Overview](#4-course-overview)
5. [MLOps Maturity Model](#5-mlops-maturity-model)
6. [Homework](#6-homework)
7. [Additional Resources](#7-additional-resources)
8. [Contributing](#8-contributing)

---

## 1. Introduction to MLOps

**MLOps** (Machine Learning Operations) is the discipline of streamlining the deployment, monitoring, and management of machine learning models in production environments. This course covers the tools and techniques needed to create robust, scalable ML solutions.

**Example use case:** Predicting the duration of a taxi ride.

Typical ML project lifecycle:
- **Design:** Assess if ML is necessary or if a simpler solution suffices.
- **Train:** Build and evaluate an appropriate model.
- **Operate:** Deploy, monitor, and maintain the model over time.

Deployed models are commonly served as web APIs. Continuous monitoring is crucial to detect data drift and ensure ongoing performance.

---

## 2. Environment Preparation

### 2.1 Using GitHub Codespaces

1. Log in to GitHub.
2. Create a new public repository (with a README).
3. Navigate to `Code` → `Codespaces` → create a codespace on `main`.

**Advantages:** Codespaces come pre-installed with Python, Docker, Docker Compose, and Node.js, simplifying setup.

**Recommendation:** For best experience, use Visual Studio Code Desktop with the Codespaces extension.

#### Install Anaconda:

```sh
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh
```

After installation:

```sh
python -V
jupyter notebook
```

*Tip: Use the PORTS section in VSCode to manage local and remote port mappings.*

---

### 2.2 Working Locally or on Cloud VMs (AWS/GCP/Linux)

#### Step 1: Install Anaconda

```sh
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh
```

#### Step 2: Update System Packages

```sh
sudo apt update
```

#### Step 3: Install Docker and Docker Compose

Follow the [official Docker documentation](https://docs.docker.com/engine/install/ubuntu/) for up-to-date instructions. Example:

```sh
sudo apt-get update
sudo apt-get install ca-certificates curl wget
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

To run Docker without `sudo`:

```sh
sudo groupadd docker
sudo usermod -aG docker $USER
```

Test Docker installation:

```sh
docker run hello-world
```

*Troubleshooting:*
- If you receive a permission denied error, try running `sudo dockerd`.
- For SSH key permission errors: `chmod 400 name-of-your-private-key-file.pem`

---

### 2.3 Using Installers (Simplified)

Install tools with official installers:
- [Anaconda](https://www.anaconda.com/products/individual)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Create and activate a conda environment:

```sh
conda create -n mlops-zoomcamp python=3.9.7
conda activate mlops-zoomcamp
```

Install common packages:

```sh
conda install numpy pandas scikit-learn seaborn jupyter
```

---

## 3. Training a Ride Duration Prediction Model

The NYC taxi dataset is available in Parquet format. Download with:

```sh
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-02.parquet
```

To work with Parquet files, install:

```sh
pip install pyarrow
```

*Advantages:* Parquet files are compressed and efficient for analytics.

---

## 4. Course Overview

While Jupyter notebooks are excellent for exploration, production workflows require structure.

**Recommendations:**
- Use Markdown cells to document metrics and parameters.
- Employ experiment tracking tools such as MLflow.
- Register models in a model registry for version control.

**ML Pipeline stages:**
1. Data loading and preparation
2. Feature engineering and vectorization
3. Model training

Pipelines should be parameterized and automated where possible. Monitor deployed models, and retrain as needed.

---

## 5. MLOps Maturity Model

| Level | Description                                                             |
|-------|-------------------------------------------------------------------------|
| **0** | No automation. Experiments in Jupyter, no reproducibility.              |
| **1** | DevOps practices applied, but no ML-specific tooling.                   |
| **2** | Automated training, experiment tracking, model registry.                |
| **3** | Automated deployment, API access, A/B testing, monitoring.              |
| **4** | Fully automated ML system – training, deployment, monitoring.           |

**Reference:** [Microsoft MLOps Documentation](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)

**Key Takeaways:**
- **Level 0:** Manual experiments, poor reproducibility.
- **Level 1:** Basic CI/CD, not ML-aware.
- **Level 2:** Automated training, experiment tracking, model registry.
- **Level 3:** Automated deployment and monitoring, A/B testing.
- **Level 4:** Fully automated end-to-end ML lifecycle.

> ⚡️ **Tip:** Start small, iterate, and evolve your MLOps maturity over time.

---

## 6. Homework

Homework for this module is available [here](homework1).

---

## 7. Additional Resources

- [Official MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)
- [Python Documentation](https://docs.python.org/3/)
- [What is MLOps?](https://ml-ops.org/)

---

## 8. Contributing

Contributions are welcome! If you notice any issues or wish to add content, please open an issue or submit a pull request.

If you’d like to see additional sections or request further customization, please let me know!
