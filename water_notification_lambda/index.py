import sys
sys.path.append('./lib')
from twilio.rest import Client
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://testUser:testUser@serverlessinstance0.itknvtp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.water_notification
consumers = db.consumers;
def handler(event,context):
    client.admin.command('ping')
    street_consumers = consumers.find({'street': 1})

    print("Sent message to {}".format(consumers))

handler('','')


# account_sid = 'AC8c2c7654cfd2cbaddc04d64db7e2de01'
# auth_token = '66eaaf8a62c591c7e455f589e480e034'

# client =  Client(account_sid,auth_token)
# def handler(event,context):
    #message = client.messages.create(body='Water flow is opened',from_='+17122145278',to='+8428169669') 
    #print(message)
    #print(message.sid)

