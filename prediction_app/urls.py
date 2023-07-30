# prediction_app/urls.py

from django.urls import path
from .views import copd_prediction

urlpatterns = [
    path('copd_prediction/', copd_prediction, name='copd_prediction'),
]
