import os
import pymongo
from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo import ReturnDocument

# printer = pprint.PrettyPrinter()

load_dotenv()

# MONGODB_URI = os.environ['MONGODB_URI']
connection_string = os.environ.get('MONGODB_URI')

cluster = MongoClient(connection_string)
db = cluster['ClimateTech']

collection = db['test']
def get_database_names():
    for db_info in cluster.list_database_names():
        print(db_info)
    #     print(db_info.testdb.list_collection_names())

# dbs = cluster.list_database_names()
# climateTech = cluster.ClimateTech
# collections_list = climateTech.list_collection_names()
# print(collections_list)

# collection.insert_one({"_id":0, "user_name":"Ramajayam"})
# collection.insert_one({"_id":1000, "user_name":"SriRama"}).inserted_id

# pprint(collection.find_one({'_id':0}))

# insert_row = collection.insert_one({'user_name':'shiva'})
# generated_id = insert_row.inserted_id
# print('id is: {generated_id}'.format(generated_id=generated_id))

# collection.delete_one({"_id":0, "user_name":"Ramajayam"})

# p1 = {"_id":0, "user_name":"Ramajayam"}
# p2 = {"_id":100, "user_name":"SriRama"}
# collection.insert_many([p1,p2])

# select_query = collection.find()
# for i in select_query:
#     print(i)

# select_query = collection.find_one({"_id":0})
# if select_query is None: select_query = []
# for i in select_query:
#     print(i)

# count = collection.count_documents(filter={})
# print(count)

# # upsert- for inserting a new document if no file is found with the mentioned criteria upsert is TRUE
# result = collection.find_one_and_update({"_id":1000}, {"$set" : {"user_name" : "Shankara"}}, upsert=False, return_document = ReturnDocument.AFTER )
# print(result)

# cursor = collection.find().pretty()

def get_find_by_id(sample_id):
    from bson.objectid import ObjectId

    _id = ObjectId(sample_id)
    details = collection.find_one({'_id':_id})
    pprint(details) 

# get_find_by_id('664d515a72fcaa10dc48d8ec')

production = cluster.production
person_collection = production.person_collection

def create_documents():
    firstnames = ['AAA','BBB','CCC','DDD']
    lastnames = ['aaa','bbb','ccc','ddd']
    ages = [34,57,62,12]

    docs = []
    for first_name, last_name, age in zip(firstnames, lastnames, ages) :
        doc = {'first_name':first_name, 'last_name': last_name, 'age':age}
        docs.append(doc)
    
    person_collection.insert_many(docs)

def find_all_people():
    people = person_collection.find()

    for person in people:
        pprint(person)

def find_one_person(first_name):
    one = person_collection.find_one({'first_name':first_name})
    pprint(one)

# find_one_person('AAA')

def count_all_people():
    count = person_collection.count_documents(filter={})
    pprint('Count: ',count)

# count_all_people()

def get_age_range(min_age, max_age):
    query = { '$and': [
        {'age':{'$gte':min_age}}
        ,{'age': {'$lte':max_age}}
    ]}
    pprint(query)
    between_ages = person_collection.find(query).sort('age')
    for person in between_ages:
        pprint(person)

# get_age_range(20,60)

