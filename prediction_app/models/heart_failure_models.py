import pickle
from django.db import models

def load_model_from_file(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# models.py (Heart Failure)
class HeartDiseaseData(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
