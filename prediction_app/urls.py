# prediction_app/urls.py

from django.urls import path

from .views.heart_failure_views import HeartFailurePredictionView
from .views.copd_views import COPDPredictionView

urlpatterns = [
    path('copd_prediction/', COPDPredictionView.as_view(), name='copd_prediction'),
    path('heart_failure_prediction/', HeartFailurePredictionView.as_view(), name='heart_failure_prediction'),
]
