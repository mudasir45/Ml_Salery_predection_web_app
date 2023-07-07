import pickle
import os
import numpy as np

def load_model():
    file_path = os.path.join('main', 'Ml_Model.pkl')
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

