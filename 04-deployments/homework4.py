#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import pickle
import argparse
from pathlib import Path
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, required=True)
parser.add_argument('--month', type=int, required=True)
args = parser.parse_args()

year = args.year
month = args.month

# Generate input and output file names
input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
output_file = Path(f'./output/yellow_tripdata_{year:04d}-{month:02d}.parquet')

# Load the model
with open('/app/model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Load data
df = pd.read_parquet(input_file)

# Preprocess
df['duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
df = df[(df['duration'] >= 1) & (df['duration'] <= 60)]

categorical = ['PULocationID', 'DOLocationID']
df[categorical] = df[categorical].astype(str)

# Prepare dicts for model
dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

# Calculate metrics
print(f"Standard deviation of predictions: {round(y_pred.std(), 2)}")
print(f"Mean predicted duration: {round(y_pred.mean(), 2)}")
from math import sqrt

print(f"RMSE: {round(sqrt(mean_squared_error(df['duration'], y_pred)), 2)}")

# **2: Preparing the output**

df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

df_result = pd.DataFrame()
df_result['ride_id'] = df['ride_id']
df_result['predicted_duration'] = y_pred

import os

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

output_file = 'output/predictions.parquet'

df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


import os

file_size = os.path.getsize(output_file) / (1024 * 1024)  # Convert bytes to MB
print(f"{file_size:.0f}M")

