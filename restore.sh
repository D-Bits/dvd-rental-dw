#! /bin/bash

# Restore Northwind db from backup
echo "---Restoring Northwind OLTP database---"
pg_restore --verbose --host=localhost --port=5432 dvdrental.tar --clean --format=t --dbname=dvdrental --user=postgres