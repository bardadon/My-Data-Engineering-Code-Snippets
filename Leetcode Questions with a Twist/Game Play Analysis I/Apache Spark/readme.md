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
df = pd.read_sql_query("SELECT * FROM activity",conn)
df.to_csv('activity.csv', header=True, index=None)
```

### Solution
```
from pyspark.sql import SparkSession

def game_play_analysis():
    
    spark = SparkSession.builder.appName('game_play').getOrCreate()
    df = spark.read.option('header', 'true').csv('activity.csv')
    df.createOrReplaceTempView('activity')
    
    query = '''
    select 
    a1.player_id,
    min(a1.event_date) as first_login
    from activity as a1
    group by a1.player_id;
    '''
    
    result = spark.sql(query)
    return result

result = game_play_analysis()
result.show()
```
### Output
```
+---------+-----------+
|player_id|first_login|
+---------+-----------+
|        1| 2016-03-01|
|        2| 2017-06-25|
|        3| 2016-03-02|
+---------+-----------+
```
