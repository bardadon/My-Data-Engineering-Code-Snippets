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
from pyspark.sql import SparkSession

def consecutiveNumbers():
    
    spark = SparkSession.builder.appName('ConsecutiveNumber').getOrCreate()

    df = spark.read.option('header', 'true').csv('logs.csv')
    df.createOrReplaceTempView('logs')

    query = '''
    select 
        distinct l1.num as ConsecutiveNumber
    from logs as l1
    join logs as l2
    on l1.id = l2.id - 1
    join logs as l3
    on l2.id = l3.id -1
    where 
        l1.num = l2.num and l2.num = l3.num
    '''
    result = spark.sql(query)
    return result
```
### Output
```
+-----------------+
|ConsecutiveNumber|
+-----------------+
|                1|
|                2|
+-----------------+
```
