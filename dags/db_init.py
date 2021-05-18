"""
DAG to initialize OLTP and OLAP databases.
"""
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime


default_args = {
    "owner": "airflow",
    "start_date": None,
    "retries": 1,
}

dag = DAG(
    "db_init", 
    schedule_interval=None, 
    template_searchpath=['/usr/local/airflow/dags/sql'], 
    catchup=False, 
    start_date=datetime(2021, 5, 16),
    default_args=default_args
)

with dag:

    # Drop the oltp db if it already exists
    t1 = PostgresOperator(
        task_id="drop_db",
        sql="DROP DATABASE IF EXISTS dvdrentals;",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Create the OLTP db
    t2 = PostgresOperator(
        task_id="create_db",
        sql="CREATE DATABASE dvdrentals;",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Create a separate schema in the 
    t3 = PostgresOperator(
        task_id="create_schema",
        sql="CREATE SCHEMA dw;",
        postgres_conn_id="pg_main",
        database="dvdrentals",
        autocommit=True
    )

    t1 >> t2 >> t3
