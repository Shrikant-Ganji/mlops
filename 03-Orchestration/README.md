# Module 3: Orchestration & ML Pipelines

Welcome to **Module 3: Orchestration & ML Pipelines** for MLOps Zoomcamp 2025!  
This module guides you through building, automating, and tracking machine learning pipelines using modern workflow orchestration tools.

---

## 📋 Module Overview

In this module, you will:

- Learn the motivation behind orchestration in ML projects
- Prepare, train, and track an end-to-end regression pipeline on the NYC Yellow Taxi dataset
- Use MLflow for experiment tracking and artifact logging
- Practice modularizing your workflow for automation and reproducibility

---

## 🚦 Key Concepts

**Orchestration** is about automating, scheduling, and managing multi-step ML workflows.  
It ensures your model development process is:

- **Reproducible:** Runs and results are tracked and logged
- **Reliable:** Handles errors, retries, and dependencies
- **Scalable:** Easily moves from local development to production

This module emphasizes hands-on work with [Prefect](https://www.prefect.io/) and [MLflow](https://mlflow.org/).

---

## 🗂️ Folder Structure

```
03-Orchestration/
│
├── README.md                # This documentation
├── homework3.ipynb          # Main notebook: full pipeline, code, and explanations
├── homework3.py             # Script version for automation/CLI
├── mlflow.db                # MLflow tracking DB (created at runtime)
├── artifacts/               # Output artifacts (e.g., DictVectorizer pickle)
├── mlruns/                  # MLflow experiment logs & model artifacts
└── .ipynb_checkpoints/      # Jupyter notebook checkpoints
```
- Some files/folders are generated when you run the pipeline.

---

## 📝 Detailed Pipeline Walkthrough

The main workflow in `homework3.ipynb` covers:

### 1. **Environment & Version Tracking**
- Uses Prefect 3.4.4, Python 3.10.16, MLflow, and scikit-learn.
- Run `!prefect version` to verify versions.

### 2. **Data Loading**
- Loads the March 2023 NYC Yellow Taxi dataset (over 3.4 million rows) directly from a public parquet file.

### 3. **Data Preparation**
- Calculates trip duration from timestamps.
- Filters outliers: keeps only trips 1–60 minutes long.
- Converts categorical columns (`PULocationID`, `DOLocationID`) to strings.

### 4. **Feature Engineering & Splitting**
- Sets up features and target variable (`duration`).
- Splits into training and validation sets (80/20 split).
- Uses `DictVectorizer` to one-hot encode categorical features for regression.

### 5. **Model Training & Experiment Tracking**
- Trains a `LinearRegression` model from scikit-learn.
- Computes RMSE on validation set.
- Uses MLflow to:
  - Track parameters (`model_type`)
  - Log the RMSE metric
  - Log the trained model artifact (with input signature and example)
  - Set up experiment tracking with a local SQLite backend (`mlflow.db`)

### 6. **Artifact Logging**
- Saves the `DictVectorizer` as a pickle file in the `artifacts/` directory.
- Logs the vectorizer as an artifact in MLflow for full reproducibility.

### 7. **Model Registry & Inspection**
- Automatically logs model artifacts and metadata in `mlruns/`.
- Demonstrates how to search for the `MLmodel` files in the run directories for model introspection.

### 8. **Final Results Summary**
- Example outputs:
  - Records loaded: **3,403,766**
  - Records after prep: **3,316,216**
  - Model intercept: **24.75**
  - RMSE: **8.15**

---

## 🚀 How to Run

### In Jupyter Notebook

1. Open `homework3.ipynb` in Jupyter Lab/Notebook.
2. Run each cell sequentially to follow the pipeline step-by-step.
3. Inspect MLflow experiment results via local files or MLflow UI.

### As a Python Script

1. Run `python homework3.py` to execute the pipeline non-interactively.
2. Artifacts and logs will be saved in `artifacts/` and `mlruns/`.

---

## 💡 Best Practices Highlighted

- **Modular code:** Data preparation, feature engineering, and model training are written as reusable functions.
- **Tracking everything:** All parameters, metrics, and artifacts are logged for reproducibility.
- **Reproducible environment:** Version info and dependencies are recorded.
- **Clean outputs:** The notebook prints summary statistics and results for clarity.

---

## 📚 Further Exploration

- Try extending the pipeline with additional steps (feature engineering, hyperparameter tuning, etc.).
- Use Prefect flows to schedule and monitor the pipeline.
- Integrate with cloud-based MLflow tracking or artifact stores for production setups.

---

## 📑 References & Resources

- [Prefect Documentation](https://docs.prefect.io/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NYC Taxi Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## ❓ Questions & Help

- Use [GitHub Discussions](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025/discussions) for queries about this module.
- Found a bug? [Open an issue](https://github.com/Shrikant-Ganji/mlops-zoomcamp-2025/issues).

---

Happy Orchestrating! 🚦
