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
df = pd.read_sql_query("SELECT * FROM scores",conn)
df.to_csv('scores.csv', header=True, index=None)
```

### Solution
```
def rank_score():
    
    # Starting a session
    spark = SparkSession.builder.appName('Nth_Highest_Salary').getOrCreate()

    # loading the data
    df = spark.read.option('header', 'true').option('inferSchema', 'true')\
    .csv('scores.csv')

    df.createOrReplaceTempView('scores')

    query = '''
    select 
        aaa.score,
        aaa.rank
    from 
    (
        select 
            s1.id,
            s1.score,
            count(*) as rank
        from scores as s1, (select distinct score from scores) as s2
        where s1.score <= s2.score
        group by s1.id, s1.score
        order by s1.score desc
    ) aaa
    '''

    result = spark.sql(query)
    return result
```
```
result = rank_score()
result.show()
```

### Output
```
+-----+----+
|score|rank|
+-----+----+
|  4.0|   1|
|  4.0|   1|
| 3.85|   2|
| 3.65|   3|
| 3.65|   3|
|  3.5|   4|
+-----+----+
```
