import pickle
from django.db import models

def load_model_from_file(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# models.py (COPD)
class COPDData(models.Model):
    AGE = models.IntegerField()
    PackHistory = models.IntegerField()
    MWT1 = models.IntegerField()
    MWT2 = models.IntegerField()
    FEV1 = models.FloatField()
    FVC = models.FloatField()
    CAT = models.IntegerField()
    HAD = models.IntegerField()
    SGRQ = models.FloatField()
    copd = models.IntegerField()
    gender = models.IntegerField()
    smoking = models.IntegerField()
