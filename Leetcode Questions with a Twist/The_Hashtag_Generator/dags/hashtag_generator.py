from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


import logging
import datetime
import pandas as pd

default_args = {
    'start_date':datetime.datetime(2022,1,1),
    'schedule_interval':'@daily'
}

def _extract_data(copy_sql):
    hook = PostgresHook(postgres_conn_id = 'postgres')
    logging.info('Exporting query to file')
    hook.copy_expert(copy_sql, filename='/tmp/input_data.csv'
    )


with DAG(dag_id='hashtag_generator',default_args=default_args, catchup=False):
    
    # Dag #1 - Create a table in Postgres
    create_table_postgres = PostgresOperator(
        task_id = 'create_table_postgres',
        postgres_conn_id='postgres',
        database='airflow',
        sql = "postgres_scripts/create_table.sql"
    )

    # Dag #2 - Insert Data to Postgres
    insert_data_postgres = PostgresOperator(
        task_id = 'insert_data_postgres',
        postgres_conn_id='postgres',
        database='airflow',
        sql = "postgres_scripts/insert_data.sql"
    )

    # Dag #3 - Extract Data
    extract_data_python = PythonOperator(
        task_id = 'extract_data_python',
        python_callable=_extract_data,
        op_kwargs={"copy_sql": "COPY (SELECT * FROM hashtags) TO STDOUT WITH CSV HEADER"}
    )


    # Dependencies
    create_table_postgres >> insert_data_postgres >> extract_data_python