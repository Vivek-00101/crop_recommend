import pickle

class Model:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    @staticmethod
    def load_model(model_path):
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model

    def predict(self, data):
        return self.model.predict(data)
