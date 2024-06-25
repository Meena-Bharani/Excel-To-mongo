import os
from dotenv import load_dotenv
from pymongo import MongoClient

#load config from .env file
load_dotenv()

MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

