
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus


password = "chetan@3852"
encoded_password = quote_plus(password)

uri = "mongodb+srv://chetans696:" + encoded_password + "@demo1.emw7qyy.mongodb.net/?retryWrites=true&w=majority&appName=demo1"

# Create a new client and connect to the server
conn = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)