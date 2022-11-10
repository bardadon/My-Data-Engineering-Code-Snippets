### Deploy Pipeline

```
docker-compose up -d
```
Go to localhost:8080/

### Run the DAG
```
docker exec -it majorityelement_airflow-scheduler_1 bash

airflow@fbdff0ccc162:/opt/airflow$ airflow dags unpause user_processing

airflow@fbdff0ccc162:/opt/airflow$ airflow dags trigger user_processing
```

### The Data

Login to Postgres - Go to localhost:5050/
![Screenshot 2022-11-10 130346](https://user-images.githubusercontent.com/65648983/201074865-91bb8629-1d2b-4450-bd5e-709f7911e5e9.png)


### PostgreSQL Solution
```
select nums
from majorityelement
group by nums
order by count(*) desc
limit 1
```
### Output
![Screenshot 2022-11-10 130715](https://user-images.githubusercontent.com/65648983/201075554-1b403eb2-146d-455f-ab32-5dbb246249ac.png)
