import numpy as np

class DataProcessor:
    @staticmethod
    def preprocess_data(record):
        data = np.array([[record["N"], record["P"], record["K"], record["Temperature"],
                          record["Humidity"], record["pH"], record["Rainfall"]]])
        return data
