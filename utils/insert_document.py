from datetime import datetime

class DocumentInserter:
    def __init__(self, db):
        self.db = db

    def insert_document(self):
        document = {
            "N": 90,
            "P": 80,
            "K": 90,
            "Temperature": 45,
            "Humidity": 65,
            "pH": 6.5,
            "Rainfall": 130.0,
            "timestamp": datetime.utcnow()
        }
        self.db.insert_document(document)
