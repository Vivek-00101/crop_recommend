import unittest
from utils.database import Database
from utils.model_utils import Model
from utils.data_processing import DataProcessor
import yaml

class TestFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("config/config.yaml", 'r') as file:
            cls.config = yaml.safe_load(file)
        cls.db = Database("config/config.yaml")
        cls.model = Model(cls.config['model']['path'])
        cls.data_processor = DataProcessor()

    def test_get_database(self):
        collection = self.db.collection
        self.assertIsNotNone(collection)

    def test_load_model(self):
        model = self.model.model
        self.assertIsNotNone(model)

    def test_preprocess_data(self):
        record = {
            "N": 90,
            "P": 80,
            "K": 90,
            "Temperature": 45,
            "Humidity": 65,
            "pH": 6.5,
            "Rainfall": 130.0
        }
        data = self.data_processor.preprocess_data(record)
        self.assertEqual(data.shape, (1, 7))

if __name__ == '__main__':
    unittest.main()
