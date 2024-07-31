import yaml
import json
import argparse
from utils.database import Database
from utils.model_utils import Model
from utils.data_processing import DataProcessor
from utils.insert_document import DocumentInserter

class CropPredictionApp:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.db = Database(config_path)
        self.model = Model(self.config['model']['path'])
        self.data_processor = DataProcessor()
        self.crop_labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
                            'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango',
                            'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya',
                            'coconut', 'cotton', 'jute', 'coffee']

    def run(self, operation):
        if operation == 'insert':
            self.insert_sample_document()
        elif operation == 'predict':
            latest_record = self.fetch_latest_record()
            if latest_record:
                self.show_latest_record(latest_record)
                self.predict_on_data(latest_record)
                self.save_latest_record(latest_record)
        else:
            print("Invalid operation. Use 'insert' or 'predict'.")

    def insert_sample_document(self):
        inserter = DocumentInserter(self.db)
        inserter.insert_document()

    def fetch_latest_record(self):
        return self.db.fetch_latest_record()

    def show_latest_record(self, record):
        print("Latest Record:", record)

    def predict_on_data(self, record):
        data = self.data_processor.preprocess_data(record)
        prediction = self.model.predict(data)
        predicted_crop = self.crop_labels[int(prediction[0])]
        print(f"Predicted crop: {predicted_crop}")
        return predicted_crop

    def save_latest_record(self, record):
        with open('data/latest_record.json', 'w') as file:
            json.dump(record, file, default=str)
        print("Latest record saved to 'data/latest_record.json'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Crop Prediction Application')
    parser.add_argument('operation', type=str, help="Operation to perform: 'insert' or 'predict'")
    args = parser.parse_args()

    app = CropPredictionApp('config/config.yaml')
    app.run(args.operation)
