### Load the Data
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
df = pd.read_sql_query("SELECT * FROM employee",conn)
df.to_csv('employee.csv', header=True, index=None)
```

### Solution
```
from pyspark import SparkConf
from pyspark.sql import SparkSession


def Nth_Highest_Salary(n):
    
    # Starting a session
    spark = SparkSession.builder.appName('Nth_Highest_Salary').getOrCreate()
    
    # loading the data
    df = spark.read.option('header', 'true').option('inferSchema', 'true')\
    .csv('employee.csv')
    
    # Create a temp view called employee
    df.createOrReplaceTempView('employee')
    
    # Query Data
    query = '''
    SELECT min(salary) as Nth_Highest_Salary
    from
    (
    select salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT {}
    )
    '''.format(n)

    result = spark.sql(query)
    return result


result = Nth_Highest_Salary(2)
result.show()
```
### Output
```
+------------------+
|Nth_Highest_Salary|
+------------------+
|               200|
+------------------+
```
