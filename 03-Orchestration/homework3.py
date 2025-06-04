from prefect import flow, task
import pandas as pd
import numpy as np
import os
import pickle
import pathlib
import mlflow
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from mlflow.models.signature import infer_signature


@task
def load_data():
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    df = pd.read_parquet(url)
    print(f"✅ Loaded {len(df):,} records")
    return df


@task
def prepare_data(df):
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df['duration'].dt.total_seconds() / 60
    df = df[(df['duration'] >= 1) & (df['duration'] <= 60)].copy()

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)
    print(f"✅ Data after preparation: {len(df):,} rows")
    return df


@task
def train_model(df):
    categorical = ['PULocationID', 'DOLocationID']
    df['target'] = df['duration']
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

    def df_to_dict(df):
        return df[categorical].to_dict(orient='records')

    X_train = df_to_dict(train_df)
    X_val = df_to_dict(val_df)

    dv = DictVectorizer()
    X_train = dv.fit_transform(X_train)
    X_val = dv.transform(X_val)

    y_train = train_df['target'].values
    y_val = val_df['target'].values

    mlflow.set_tracking_uri("sqlite:///mlflow.db")

    # Explicitly set or create the experiment
    mlflow.set_experiment("homework3-nyc-taxi")

    # Verify the experiment
    experiment = mlflow.get_experiment_by_name("homework3-nyc-taxi")
    if experiment:
        print(f"Experiment ID: {experiment.experiment_id}")
    else:
        print("Experiment not found!")

    with mlflow.start_run():
        lr = LinearRegression()
        lr.fit(X_train, y_train)

        y_pred = lr.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        rmse = np.sqrt(mse)

        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("rmse", rmse)

        signature = infer_signature(X_val, y_pred)
        input_example = X_val[:1]

        mlflow.sklearn.log_model(
            sk_model=lr,
            artifact_path="models",
            signature=signature,
            input_example=input_example
        )

        # Save DictVectorizer
        output_dir = pathlib.Path("artifacts")
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / "dv.pkl", "wb") as f_out:
            pickle.dump(dv, f_out)

        mlflow.log_artifact(str(output_dir / "dv.pkl"))

        print(f"✅ RMSE: {rmse:.2f}")
        print(f"✅ Intercept: {lr.intercept_:.2f}")

        return lr.intercept_


@task
def find_model_file():
    mlflow_dir = "mlruns"
    for root, dirs, files in os.walk(mlflow_dir):
        for file in files:
            if file == "model.pkl":
                full_path = os.path.join(root, file)
                size_bytes = os.path.getsize(full_path)
                print("✅ Found model.pkl at:", full_path)
                print(f"✅ model.pkl size: {size_bytes} bytes")
                return size_bytes

@flow
def main():
    df = load_data()
    df_clean = prepare_data(df)
    intercept = train_model(df_clean)
    model_size = find_model_file()

    print(f"✅ Intercept = {intercept:.2f}")
    print(f"✅ MLModel file size (bytes): {model_size}")

if __name__ == "__main__":
    main()