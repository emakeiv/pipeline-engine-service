from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from app.sal.etl.main import main

DAG_DEFAULT_ARGS={
    'owner': 'airflow',
    'depends_on_past': False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
      default_args = DAG_DEFAULT_ARGS,
      dag_id='get_fx_mkt_data',
      start_date=datetime(2024, 1, 1),
      schedule_interval='@daily',
      catchup=False
) as dag:
      update_daily = PythonOperator(
            task_id='first_attempt',
            python_callable=main
      )

      update_daily