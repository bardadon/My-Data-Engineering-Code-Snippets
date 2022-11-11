### Deploy Airflow
- Run
```
docker-compose up -d
```

### Run the Pipeline
```
bash run_etl.sh
```

### The Pipeline
- Go to localhost:8080/ 

![Screenshot 2022-11-11 120331](https://user-images.githubusercontent.com/65648983/201316793-7c606da0-d53c-424a-9421-74c684eae0b3.png)

### The Data
- Login to MySQL - Go to localhost:3000/
- Grab the IP of the MySQL server container and login
- The data:
![Screenshot 2022-11-11 120521](https://user-images.githubusercontent.com/65648983/201317095-979e6b96-350d-44c5-8cc8-a7b5516e3a7f.png)


### MySQL Solution
```
select nums
from majorityelement
group by nums
order by count(*) desc
limit 1
```
### Output
![Screenshot 2022-11-11 120556](https://user-images.githubusercontent.com/65648983/201317180-486295b4-4664-4df3-b402-63ce24e1264f.png)
