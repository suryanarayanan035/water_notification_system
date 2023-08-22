import sys
sys.path.append('./lib')

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://testUser:testUser@serverlessinstance0.itknvtp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

def handler(event,context):
    db = client.water_notification
    consumers = db.consumers
    print("event: {}".format(event))
    print("context: {}".format(context))
    client.admin.command('ping')


