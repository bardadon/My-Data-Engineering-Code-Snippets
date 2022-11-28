rm -r ./solutions/
mkdir ./solutions/
docker cp postgres:/tmp/postgres_solution.csv ./solutions/
docker cp airflow_worker:/tmp/mysql_solution.csv ./solutions/
docker cp airflow_worker:/tmp/python_solution.csv ./solutions/