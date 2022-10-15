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
