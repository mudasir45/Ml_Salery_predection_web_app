import pickle
import numpy as np

def load_model():
    with open('Ml_Model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_education = data["le_education"]
le_country = data["le_country"]
le_emp = data["le_emp"]