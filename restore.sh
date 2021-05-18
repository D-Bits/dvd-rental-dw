#! /bin/bash

# Restore Northwind db from backup
echo "---Restoring DVD Rental OLTP database---"
pg_restore --verbose --host=localhost --port=5432 dvdrental.tar --clean --format=t --dbname=dvdrentals --user=postgres
