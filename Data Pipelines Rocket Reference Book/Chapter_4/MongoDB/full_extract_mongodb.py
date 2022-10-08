import csv
from pymongo import MongoClient
import datetime
import os 
from google.cloud import storage

'''
Export MongoDB's documents to CSV
'''

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017")

# Create a database
mongo_db = mongo_client.get_database('bar')

# Create collection
mongo_collection = mongo_db.get_collection('events')


all_events = []

# For every document in the collection
for document in mongo_collection.find():    

    # Grab the relevant keys
    document_keys = list(document.keys())
    relevant_keys = document_keys[1:]

    # Grab the relevant values
    document_values = list(document.values())
    relevant_values = document_values[1:]

    # Turn them into a dictionary and add to list
    relevant_items = dict(zip(relevant_keys, relevant_values))
    all_events.append(relevant_items)

# Export list of dictionaries as CSV
with open('event_logs.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = [list(document.keys())[1:] for document in mongo_collection.find()][0])
    writer.writeheader()
    writer.writerows(all_events)


'''
Load CSV to Google Bucket
'''
# Setting configs
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Grab bucket
storage_client = storage.Client()
bucket = storage_client.get_bucket('chapter_4')

# Create a blob from the csv file
blob = bucket.blob(blob_name='full_extract_mongodb/event_logs.csv')

# Upload to bucket
blob.upload_from_filename('event_logs.csv')
