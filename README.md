
# About

A data warehouse for a DVD rental company. Built with PostgreSQL and Apache Airflow.

## Setup Instructions

- Clone the repository
- Add a `.env` file with the following enivronment variables:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=(a password of your choosing)
POSTGRES_HOST=postgres
EXECUTOR=LocalExecutor
```
- Run either `make start`, or `sudo astro dev start -e .env` to bootstrap the Airflow and Postgres.
- Navigate to [localhost:8000](localhost:8000), and login with the credentials shown in stdout. 
- Run the `db_init` DAG to create the databases, and tables for the data warehouse.
- Run `sh restore.sh` to build the OLTP database from the `dvdrental.tar` file.
- Enter the password used in your `POSTGRES_PASSWORD` environment variable.
