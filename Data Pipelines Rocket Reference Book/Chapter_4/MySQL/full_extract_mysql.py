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

# Create a query
m_query = "SELECT * FROM Orders;"
local_filename = "order_extract.csv"

# Create a cursor, execute query and fetch the results
m_cursor = conn.cursor()
m_cursor.execute(m_query)
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
bucket = storage_client.bucket(bucket_name='chapter_4')
bucket = storage_client.create_bucket(bucket, location='US')

# Grabing the bucket object
bucket = storage_client.get_bucket('chapter_4')

# Create a blob from the csv file
blob = bucket.blob(blob_name='full_extract/order_extract.csv')

# Upload to bucket
blob.upload_from_filename('order_extract.csv')
