from pymysqlreplication import BinLogStreamReader
from pymysqlreplication import row_event
import configparser
import pymysqlreplication
import csv
from google.cloud import storage
import os

# Creating a parser object and reading from the config file
parser = configparser.ConfigParser()
parser.read("pipeline.conf")

# Grabing the values from the config file
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")

# Creating a dictionary with MySQL settings
mysql_settings = {
    'host':hostname,
    'port': int(port),
    'user':username,
    'passwd':password
}

# Connect to MySQL Binlog
b_stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    server_id=100,
    only_events=[row_event.DeleteRowsEvent, row_event.UpdateRowsEvent, row_event.WriteRowsEvent]
)

order_events = []

# Read the binlog, check the type of each event and store it in a dictionary
# Append each event dictionary to a list
for binlogevent in b_stream:
    for row in binlogevent.rows:
        if binlogevent.table =='orders':
            event = {}
            if isinstance(binlogevent, row_event.DeleteRowsEvent):
                event['action'] = 'delete'
                event.update(row['values'].items())
            elif isinstance(binlogevent, row_event.UpdateRowsEvent):
                event['action'] = 'update'
                event.update(row['after_values'].items())
            elif isinstance(binlogevent, row_event.WriteRowsEvent):
                event['action'] = 'insert'
                event.update(row['values'].items())

        order_events.append(event)

# Close connection
b_stream.close()


keys = order_events[0].keys()
local_filename = 'binlog_orders.csv'
with open(local_filename, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='|')
    dict_writer.writerows(order_events)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Creating a bucket
storage_client = storage.Client()

# Grabing the bucket object
bucket = storage_client.get_bucket('chapter_4')

# Create a blob from the csv file
blob = bucket.blob(blob_name='binlog_extract/binlog_orders.csv')

# Upload to bucket
blob.upload_from_filename('binlog_orders.csv')

