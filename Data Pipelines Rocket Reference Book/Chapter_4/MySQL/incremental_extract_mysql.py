import csv
import pymysql
import configparser
import os 
from google.cloud import storage

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

if conn is None:
  print("Error connecting to the MySQL database")
else:
  print("MySQL connection established!")

# Creating a cursor object
m_cursor = conn.cursor()


# Creating query - Grabing max date from warehouse
set_variable_query = "select max(LastUpdated) from warehouse.orders_warehouse;"
m_cursor.execute(set_variable_query)
last_update_date = m_cursor.fetchone()
last_update_date = last_update_date[0].date()


collect_orders_query = '''select *
           from orders
           where LastUpdated > {};'''.format(last_update_date)


local_filename = "order_extract.csv"

# Create a cursor, execute query and fetch the results
m_cursor.execute(collect_orders_query)
results = m_cursor.fetchall()

# Create a new file and write the results into it
with open(local_filename, 'w') as fp:
  csv_w = csv.writer(fp, delimiter='|')
  csv_w.writerows(results)

# Close file, cursor and connection
fp.close()
m_cursor.close()
conn.close()

# Setting configs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Creating a bucket
storage_client = storage.Client()

# Grabing the bucket object
bucket = storage_client.get_bucket('chapter_4')

# Create a blob from the csv file
blob = bucket.blob(blob_name='chapter_4/incremental_extract/order_extract.csv')

# Upload to bucket
blob.upload_from_filename('order_extract.csv')
