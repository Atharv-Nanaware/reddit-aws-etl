import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Adjust the path to ensure modules can be found
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline

# Default arguments for the DAG
default_args = {
    'owner': 'Atharv_Nanaware',
    'start_date': datetime(2024, 11, 20)
}


file_postfix = datetime.now().strftime("%Y%m%d")
# Firstly we do the Extraction From Rediit 
#  then we Will Upload this to the Reddit
#  then we will do the Transformation
dag = DAG(
    dag_id="etl_reddit_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Define the extraction task
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{file_postfix}',
        'subreddit': "dataengineering",
        'time_filter': 'day',
        'limit': 50
    },
    dag=dag  
)

# If you have more tasks, define them here and set dependencies
# For example:
# transform = PythonOperator(...)
# load = PythonOperator(...)
# extract >> transform >> load





