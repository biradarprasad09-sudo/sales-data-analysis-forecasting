import pandas as pd

class DataProcessor:

    def load_data(self, file_path):
        return pd.read_csv(file_path)

    def clean_data(self, data):
        data = data.drop_duplicates()
        data = data.dropna()
        return data