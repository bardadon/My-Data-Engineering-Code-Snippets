### Deploy Pipeline
- Run
```
docker-compose up -d
```

### Run the DAG
- Go to localhost:8080/ and run the dag.

![Screenshot 2022-11-10 152107](https://user-images.githubusercontent.com/65648983/201102655-cf511aad-b26c-4a2e-afed-3043e6a8ff82.png)


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
```
3
```
