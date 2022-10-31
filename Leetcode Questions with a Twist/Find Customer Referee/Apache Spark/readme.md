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
df = pd.read_sql_query("SELECT * FROM customers",conn)
df.to_csv('customers.csv', header=True, index=None)
```
### Solution
```
from pyspark.sql import SparkSession

def consecutiveNumbers():
    
    spark = SparkSession.builder.appName('ConsecutiveNumber').getOrCreate()

    df = spark.read.option('header', 'true').csv('logs.csv')
    df.createOrReplaceTempView('logs')

    query = '''
    select name
    from customer
    where referee_id  != 2 or referee_id is null;
    '''
    result = spark.sql(query)
    return result
```
### Output
```
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```
