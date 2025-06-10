FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

# Copy only your script into the image (not the model)
COPY homework4.py .

# Install required Python packages
RUN pip install pandas pyarrow python-dateutil scikit-learn==1.5.0

# Set default command with CLI arguments as placeholders
ENTRYPOINT ["python", "homework4.py"]

