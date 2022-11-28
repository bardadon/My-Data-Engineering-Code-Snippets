#!/bin/bash

docker exec -it airflow_scheduler airflow dags unpause majorityElement 
docker exec -it airflow_scheduler airflow dags trigger majorityElement 

bash load_solution.sh