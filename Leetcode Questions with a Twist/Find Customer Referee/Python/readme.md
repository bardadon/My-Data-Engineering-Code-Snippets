### Load Data
```
import sqlite3
import pandas as pd

# Creating an in memory database connection
conn = sqlite3.connect(';memory;')

cursor = conn.cursor()

queries = '''
drop table if exists customer;
Create table If Not Exists Customer (id int, name varchar(25), referee_id int);
insert into Customer (id, name, referee_id) values ('1', 'Will', 'None');
insert into Customer (id, name, referee_id) values ('2', 'Jane', 'None');
insert into Customer (id, name, referee_id) values ('3', 'Alex', '2');
insert into Customer (id, name, referee_id) values ('4', 'Bill', 'None');
insert into Customer (id, name, referee_id) values ('5', 'Zack', '1');
insert into Customer (id, name, referee_id) values ('6', 'Mark', '2');
'''

query_list = queries.splitlines()[1:]

for query in query_list:
    cursor.execute(query)

conn.commit()

df = pd.read_sql_query("select * from Customer;", conn)
```
### Solution
```
names = pd.DataFrame(df[df.referee_id != 2].name)
print(names)
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
