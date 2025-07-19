from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from src.ingest import load_data
from src.clean import clean_data

def step_ingest():
    df = load_data('data/raw_dataset.csv')
    df.to_csv('data/interim/ingested.csv', index=False)

def step_clean():
    df = pd.read_csv('data/interim/ingested.csv')
    cleaned = clean_data(df)
    cleaned.to_csv('data/processed/cleaned.csv', index=False)

with DAG('autoclean_pipeline',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    ingest_task = PythonOperator(task_id='ingest_data', python_callable=step_ingest)
    clean_task = PythonOperator(task_id='clean_data', python_callable=step_clean)

    ingest_task >> clean_task
