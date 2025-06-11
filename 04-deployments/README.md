# Module 4: Model Deployment

Welcome to the **Model Deployment** module of the MLOps Zoomcamp 2025!  
This directory contains everything you need to package, run, and test a machine learning model for the NYC Taxi Trip Duration prediction in a production-like environment.

---

## 📂 Folder Structure

```
04-deployments/
│
├── Dockerfile              # Docker image definition for reproducible deployment
├── Pipfile                 # Python dependencies specification for Pipenv
├── Pipfile.lock            # Lock file with fully specified dependency versions
├── homework4.ipynb         # Notebook: step-by-step deployment workflow & explanation
├── homework4.py            # Parametrized batch scoring script (can run locally or in Docker)
├── homework/               # Directory for model artifacts (e.g., model.bin)
├── output/                 # Stores output predictions (e.g., predictions.parquet)
└── .ipynb_checkpoints/     # Jupyter auto-saved checkpoints (ignore)
```

---

## 🚀 What You'll Learn & Do

1. **Prepare a batch scoring pipeline** using a trained sklearn model.
2. **Parametrize your script** for flexible use (different months/years).
3. **Package your pipeline** in a Docker container for portability and reproducibility.
4. **Test locally and via Docker** to ensure consistent results.
5. **Understand dependency management** via Pipenv and Docker.

---

## 📝 File-by-File Breakdown

### [`homework4.ipynb`](homework4.ipynb)
- **Purpose:** Step-by-step notebook for batch prediction and deployment.
- **Key Tasks:**
  - Loads a pre-trained model (`model.bin` with DictVectorizer and sklearn model).
  - Downloads and preprocesses new NYC taxi data (by year/month).
  - Runs batch predictions; evaluates RMSE and other stats.
  - Writes output predictions to a parquet file.
  - Converts code to a standalone script for automation.
  - Explains how to parameterize, dockerize, and run the script in various environments.
  - Shows how to check model, code, and data consistency across runs and containers.

### [`homework4.py`](homework4.py)
- **Purpose:** Command-line batch scoring script.
- **Key Features:**
  - Accepts `--year` and `--month` arguments for flexible data input.
  - Loads the trained model and vectorizer from `/app/model.bin` (for Docker compatibility).
  - Downloads and preprocesses the appropriate Yellow Taxi dataset.
  - Runs predictions and calculates evaluation metrics (RMSE, mean, std).
  - Outputs a predictions parquet file to `output/predictions.parquet`.
  - Prints file size and key statistics for result validation.
- **Usage Example:**
  ```bash
  python homework4.py --year=2023 --month=4
  ```

### [`Dockerfile`](Dockerfile)
- **Purpose:** Defines a reproducible and shareable environment for batch scoring.
- **Highlights:**
  - Uses a base image with Python 3.10 and common ML libraries.
  - Copies only the script (`homework4.py`) into the image.
  - Installs all required dependencies via pip (including pandas, pyarrow, scikit-learn==1.5.0).
  - Sets the entrypoint so you can pass `--year` and `--month` arguments at runtime.
- **Usage Example:**
  ```bash
  docker build -t ride-duration-predictor .
  docker run -v $(pwd)/homework:/app -v $(pwd)/output:/output ride-duration-predictor --year=2023 --month=4
  ```

### [`Pipfile` & `Pipfile.lock`](Pipfile)
- **Purpose:** Pin and manage Python dependencies for your project.
- **Details:**
  - Ensures consistent environment setup with Pipenv.
  - Locks versions (e.g., scikit-learn==1.5.0, pandas with pyarrow).
  - Python 3.10 required for full compatibility.

### [`homework/`]
- **Purpose:** Stores your trained model artifact (`model.bin`), which contains both the feature vectorizer and the regression model.
- **Tip:** Make sure `model.bin` is available in this directory before running the scoring script or Docker image.

### [`output/`]
- **Purpose:** Output directory for prediction results (e.g., `predictions.parquet`).
- **Auto-created** if missing when scripts are run.

---

## 💡 How to Use

### 1. **Run Locally**
- Make sure you have Python 3.10 and dependencies installed (via `pip install -r requirements.txt` or `pipenv install`).
- Place your `model.bin` in `homework/`.
- Run:
  ```bash
  python homework4.py --year=2023 --month=4
  ```

### 2. **Build & Run with Docker**
- Build the container:
  ```bash
  docker build -t ride-duration-predictor .
  ```
- Run the scoring job (ensure model and output directories are mounted as volumes):
  ```bash
  docker run -v $(pwd)/homework:/app -v $(pwd)/output:/output ride-duration-predictor --year=2023 --month=4
  ```

### 3. **Check Outputs**
- Find your predictions in `output/predictions.parquet`
- Console output includes RMSE, mean, standard deviation, and output file size for quick validation.

---

## 🛠️ Professional Practices

- **Reproducibility:** All environments (Python, libraries) are version pinned.
- **Portability:** Docker ensures you can ship and run the same code anywhere.
- **Parameterization:** CLI arguments make batch jobs flexible and automatable.
- **Separation of concerns:** Model artifacts, code, and outputs are cleanly separated.

---

## ❓ Troubleshooting

- Ensure `model.bin` is present in the correct location (`homework/` or `/app/` in Docker).
- Confirm Python version matches (3.10).
- If you see dependency errors, rebuild your Docker image or update your Pipfile.
- For large data files, ensure you have enough disk space for output predictions.

---

## 📚 Further Reading

- [Docker Documentation](https://docs.docker.com/)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NYC Taxi Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

**Deploy your ML pipeline with confidence – whether on your laptop, a server, or the cloud!**
