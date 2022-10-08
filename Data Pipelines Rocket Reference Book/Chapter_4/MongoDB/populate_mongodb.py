from pymongo import MongoClient
import datetime

mongo_client = MongoClient("mongodb://127.0.0.1:27017/")

mongo_db = mongo_client.get_database('bar')

mongo_db.create_collection('events')

mongo_collection = mongo_db.get_collection('events')

event_1 = {
    'event_id':1,
    'event_timestamp' : datetime.datetime.today(),
    'event_name': 'signup'
}


event_2 = {
    'event_id':2,
    'event_timestamp' : datetime.datetime.today(),
    'event_name': 'pageview'
}


event_3 = {
    'event_id':3,
    'event_timestamp' : datetime.datetime.today(),
    'event_name': 'login'
}

mongo_collection.insert_one(event_1)
mongo_collection.insert_one(event_2)
mongo_collection.insert_one(event_3)
