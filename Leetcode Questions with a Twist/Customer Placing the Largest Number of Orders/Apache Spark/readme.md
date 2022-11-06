### Load Data
```
import pandas as pd
import sqlite3

# Connect to sqlite
conn = sqlite3.connect(';memory;')
cursor = conn.cursor()

# Insert data into sqlite
queries = '''
drop table if exists orders;
Create table If Not Exists orders (order_number int, customer_number int);
insert into orders (order_number, customer_number) values ('1', '1');
insert into orders (order_number, customer_number) values ('2', '2');
insert into orders (order_number, customer_number) values ('3', '3');
insert into orders (order_number, customer_number) values ('4', '3');
'''

query_list = queries.splitlines()[1:]

for query in query_list:
    cursor.execute(query)

conn.commit()

# Create a Pandas DataFrame from the data
df = sql('''
select *
from orders
''')
```
### Solution
```
from pyspark.sql import SparkSession

def customer_orders():
    
    # Create a spark session, a spark dataframe and a temporary view
    spark = SparkSession.builder.appName('Customer Orders').getOrCreate()
    df = spark.createDataFrame(data = df)
    df.createOrReplaceTempView('orders')
    
    # Query the data
    query = '''

    select 
        o.customer_number
    from orders as o
    group by 
        o.customer_number
    order by count(*) desc
    limit 1;
    '''

    # Return results
    results = spark.sql(query)
    return results

results.show()
```
### Output
```
+---------------+
|customer_number|
+---------------+
|              3|
+---------------+
```
