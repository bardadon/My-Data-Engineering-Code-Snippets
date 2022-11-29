#!/bin/bash

# Run Airflow Dags
docker exec -it airflow_scheduler airflow dags unpause hashtag_generator
docker exec -it airflow_scheduler airflow dags trigger hashtag_generator

# Export the CSV file from airflow_worker to local
docker cp airflow_worker:tmp/input_data.csv input_data.csv

# Solve Problem
python solve_problem.py