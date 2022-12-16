#!/bin/bash

# Run Airflow Dag
echo -e "\n--------------Running the Dag...---------------\n"
docker exec -it airflow_airflow-scheduler_1 airflow dags unpause growth_of_population;
docker exec -it airflow_airflow-scheduler_1 airflow dags trigger growth_of_population;

# Copy the solution to my local machine
echo -e "\nCopying solution to local machine..."
rm -r ./solutions/
mkdir ./solutions/
docker cp airflow_airflow-worker_1:/tmp/solution.txt ./solutions/

# Print Solution
solution=$(cat solutions/solution.txt)
echo -e "\nThe Solution is: ${solution}";