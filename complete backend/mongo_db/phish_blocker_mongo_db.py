import pymongo
import pandas as pd

class PhishBlockerMongoDB:
    conn_str = ""

    def __init__(self):
        self.conn_str = "mongodb+srv://phishblocker:CMPE272team17@cluster0.yjds0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.database = "phish_blocker_db"
        self.collection = "url_collection"

    def insert_url(self, url, label):
        with pymongo.MongoClient(self.conn_str, serverSelectionTimeoutMS=5000) as client:
            db = client[self.database]
            col = db[self.collection]

            instance = { "url": url, "label": label }
           
            # check if instance already exists
            query = col.find_one({ "url": url })

            if (query == None):
                res = col.insert_one(instance)

    def create_csv(self):
        with pymongo.MongoClient(self.conn_str, serverSelectionTimeoutMS=5000) as client:
            db = client[self.database]
            col = db[self.collection]

            instances = []

            for inst in col.find():
                instances.append(inst)

            df = pd.DataFrame(instances)

            df.to_csv("data.csv", index=False)
