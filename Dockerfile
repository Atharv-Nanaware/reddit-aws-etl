# Use the official Apache Airflow image as the base
FROM apache/airflow:2.10.3-python3.10

# Switch to root to install system dependencies
USER root

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your requirements file
COPY requirements.txt /opt/airflow/

# Change ownership of the requirements file to the airflow user
RUN chown airflow: /opt/airflow/requirements.txt

# Switch to the airflow user
USER airflow

# Upgrade pip as the airflow user
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# (Optional) Switch back to root if you need to perform additional system-level configurations
# USER root

# (Optional) Set the entrypoint or CMD if not already set by the base image
# ENTRYPOINT ["..."]
# CMD ["..."]
