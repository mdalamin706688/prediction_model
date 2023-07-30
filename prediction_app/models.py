# my_project_name/models.py

import pickle

def load_model_from_file(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model
