### Load Data
```
import pymysql
import configparser
import pandas as pd

# Creating a parser object and reading from the config file
parser = configparser.ConfigParser()
parser.read("pipeline.conf")

# Grabing the values from the config file
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")

# Connecting to MySQL
conn = pymysql.connect(host=hostname,
        user=username,
        password=password,
        db=dbname,
        port=int(port))

# Export Table to CSV
df = pd.read_sql_query("SELECT * FROM logs",conn)
df.to_csv('logs.csv', header=True, index=None)
```
### Solution
```
import pandas as pd
import numpy as np

df = pd.read_csv('logs.csv')
nums = df.num

for num in range(len(nums)-2):
    if nums[num] == nums[num+1] and nums[num+1] == nums[num+2]:
        print(nums[num])
```
### Output
```
1
2
```
