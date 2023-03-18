from flask import Flask
import pymongo
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@@cluster0.csu36sp.mongodb.net/?retryWrites=true&w=majority")
db = client.events_db
custome_event_collection = db.custom_events

from app import routes,eventing