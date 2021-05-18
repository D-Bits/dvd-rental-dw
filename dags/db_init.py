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
        task_id="drop_oltp",
        sql="DROP DATABASE IF EXISTS dvdrentals;",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Drop the olap db if it already exists
    t2 = PostgresOperator(
        task_id="drop_olap",
        sql="DROP DATABASE IF EXISTS dvdrentals_dw;",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Create the OLTP db
    t3 = PostgresOperator(
        task_id="create_oltp",
        sql="CREATE DATABASE dvdrentals;",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Create the OLAP database
    t4 = PostgresOperator(
        task_id="create_olap",
        sql="CREATE DATABASE dvdrentals_dw",
        postgres_conn_id="pg_main",
        autocommit=True
    )

    # Create tables for OLAP db
    t5 = PostgresOperator(
        task_id="create_tables",
        sql="tables.sql",
        postgres_conn_id="pg_main",
        database="dvdrentals_dw",
        autocommit=True
    )

    t1 >> t2 >> [t3, t4] >> t5
