### Load Data to CSV
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


df = pd.read_sql_query("SELECT * FROM employee",conn)
df.to_csv('employee.csv', header=True, index=None)
```

### Solution - Built-in Functions
```
import pandas as pd

def Nth_Highest_Salary(n):
    df = pd.read_csv('employee.csv')

    values_array = df.Salary.sort_values(ascending=False).values
    return values_array[n-1]
    
print(Nth_Highest_Salary(2))
```

### Solution - From Scratch
```
def nth_highest_number(nums, n):
    n = n - 1
    
    # Insertion Sort
    for i in range(1, len(nums)):

        temp = nums[i]
        j = i - 1

        while j>=0 and temp > nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp

    return nums[n]
```


### Output
```
200
```
