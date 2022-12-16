### Solution


#### Dag
![python_growth](https://user-images.githubusercontent.com/65648983/208084970-ab92a604-0264-49a0-a266-4b39740a8b82.png)

#### Running the Workflow

```
bash run_etl.sh
```


#### Output
```
(Growth_of_a_Population) root@DESKTOP-3U7IV4I:/projects/CodeWares_Project/Growth_of_a_Population# bash run_etl.sh 

--------------Running the Dag...---------------

/home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:386: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
  FutureWarning,
Dag: growth_of_population, paused: False
/home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:386: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
  FutureWarning,
[2022-12-16 10:59:23,595] {__init__.py:42} INFO - Loaded API auth backend: airflow.api.auth.backend.basic_auth
[2022-12-16 10:59:23,595] {__init__.py:42} INFO - Loaded API auth backend: airflow.api.auth.backend.session
Created <DagRun growth_of_population @ 2022-12-16T10:59:23+00:00: manual__2022-12-16T10:59:23+00:00, state:queued, queued_at: 2022-12-16 10:59:23.787192+00:00. externally triggered: True>

Copying solution to local machine...

__The Solution is: 94__
```
