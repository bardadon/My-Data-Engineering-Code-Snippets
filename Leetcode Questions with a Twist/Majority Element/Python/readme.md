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
![Screenshot 2022-11-11 134322](https://user-images.githubusercontent.com/65648983/201333640-31955a1d-9d51-4e32-92b3-d8462c86ec3b.png)


### The Data
- Login to Postgres - Go to localhost:5050/
- Grab the IP of the Postgres server container and login
- The data:
![Screenshot 2022-11-10 130346](https://user-images.githubusercontent.com/65648983/201074865-91bb8629-1d2b-4450-bd5e-709f7911e5e9.png)

### Python Solution
```
def majorityElement(nums):
    
    count_dict = dict()
    
    # Count appearances in a dictionary
    for i in nums:

        count_dict[i] = count_dict.get(i,0) + 1
        
    # Grab the key that belongs to the max value
    for key, value in count_dict.items():

        if value == max(count_dict.values()):
            return key
```
