# MLOps Zoomcamp 2025

Welcome to the **MLOps Zoomcamp 2025** repository! This is a practical, project-based course for learning modern Machine Learning Operations (MLOps) with a real-world focus. Whether you're a data scientist, ML engineer, or developer, this course will equip you with the skills to take models from experiments to robust, deployable, and monitored production systems.

---

## 🌟 Why MLOps Zoomcamp?

Machine Learning is not just about building models, but about creating reliable, maintainable, and scalable systems. This course covers the entire MLOps lifecycle:
- Experimentation
- Pipeline orchestration
- Model deployment (batch/real-time)
- Monitoring & retraining
- Best software engineering practices

You’ll gain real, hands-on skills by working through each phase using the NY Taxi dataset as a running example.

---

## 🗓️ Course Modules

### **Module 1: Introduction**
- What is MLOps? Why does it matter?
- MLOps maturity model
- Overview of the NY Taxi dataset
- Course structure & environment setup
- [01-Intra](./01-Intra/) — Notebooks & homework

### **Module 2: Experiment Tracking & Model Management**
- Introduction to experiment tracking
- MLflow basics: tracking, model saving & loading, registry
- Hands-on MLflow exercises
- [02-week](./02-week/) — Notebooks, MLflow setup, homework

### **Module 3: Orchestration & ML Pipelines**
- Workflow orchestration concepts
- Introduction to pipeline tools (Prefect/Airflow)
- Building and running robust ML pipelines
- [03-Orchestration](./03-Orchestration/) — Code, artifacts, homework

### **Module 4: Model Deployment**
- Deployment strategies: online (web, streaming) vs. offline (batch)
- Deploying with Flask as a web service
- Streaming deployment with AWS Kinesis & Lambda
- Batch scoring for offline processing
- [04-deployments](./04-deployments/) — Deployment scripts, examples

### **Module 5: Model Monitoring**
- Monitoring ML services in production
- Web service monitoring: Prometheus, Evidently, Grafana
- Batch job monitoring: Prefect, MongoDB, Evidently
- Alerting and logging best practices

### **Module 6: Best Practices**
- Unit and integration testing for ML pipelines
- Linting, formatting, and pre-commit hooks
- CI/CD automation with GitHub Actions
- Infrastructure as Code (Terraform, cloud basics)

### **Final Project**
- Bring everything together: Build an end-to-end ML workflow with automation, deployment, and monitoring.

---

## 🗂️ Repository Structure

```
mlops-zoomcamp-2025/
│
├── 01-Intra/                # Module 1: Introduction (notebooks, homework)
│   ├── README.md
│   ├── homework1.ipynb
│   └── .ipynb_checkpoints/
│
├── 02-week/                 # Module 2: Experiment Tracking & Model Management
│   ├── README.md
│   ├── homework2.ipynb
│   ├── data/
│   ├── homework2/
│   ├── mlflow-env/
│   ├── mlflow.db
│   ├── mlruns/
│   ├── output/
│   ├── output.log
│   └── .ipynb_checkpoints/
│
├── 03-Orchestration/        # Module 3: Orchestration & ML Pipelines
│   ├── homework3.ipynb
│   ├── homework3.py
│   ├── mlflow.db
│   ├── artifacts/
│   ├── mlruns/
│   └── .ipynb_checkpoints/
│
├── 04-deployments/          # Module 4: Model Deployment (directory present)
│   └── ... (see repo for details)
│
├── README.md                # Main repository documentation
```
> Note: Some folders contain additional or evolving content — for the most up-to-date structure and files, [browse the repository on GitHub](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025).

---

## 🛠️ Tech Stack

- **Languages:** Python, YAML
- **ML Libraries:** scikit-learn, pandas, numpy
- **Experiment Tracking:** MLflow
- **Orchestration:** Prefect (optionally Airflow)
- **Deployment:** Flask, AWS Kinesis & Lambda (for streaming), Docker
- **Monitoring:** Prometheus, Grafana, Evidently, MongoDB
- **Infrastructure:** Terraform, GitHub Actions, pre-commit
- **Other Tools:** Jupyter, pytest, python-dotenv, boto3, pyyaml

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025.git
cd mlops-zoomcamp-2025
```

### 2. Set up your environment
- Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Explore each module
- Each module has its own README and instructions.
- Start from `01-Intra/` and work through each folder sequentially.

---

## 🧑‍💻 Contributing

We welcome contributions to improve this course! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on opening issues, submitting pull requests, and more.

---

## 🤝 Community & Support

- [GitHub Discussions](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025/discussions) — ask questions, share resources, connect!
- [Issues Tracker](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025/issues) — for bugs and suggestions.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Ready to take your ML models to production? Start your MLOps journey with Zoomcamp 2025!**
