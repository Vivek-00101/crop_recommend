from pymongo import MongoClient
import yaml

class Database:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.client = MongoClient(config['mongodb']['uri'])
        self.db = self.client[config['mongodb']['database']]
        self.collection = self.db[config['mongodb']['collection']]

    def insert_document(self, document):
        try:
            self.collection.insert_one(document)
            print("Record inserted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def fetch_latest_record(self):
        try:
            latest_record = self.collection.find_one(sort=[("timestamp", -1)])
            if latest_record:
                latest_record.pop("timestamp", None)
                print("Latest record fetched successfully!")
                return latest_record
            else:
                print("No record found!")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
