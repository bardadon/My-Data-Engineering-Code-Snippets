#!/bin/bash

docker exec -it airflow_scheduler airflow dags unpause unique_in_order;
docker exec -it airflow_scheduler airflow dags trigger unique_in_order;

bash load_solution.sh;

echo "The Solution is: "; cat solutions/solution.txt;