from django.apps import AppConfig

class PredictionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction_app'

    def ready(self):
        # Import and include views from separate files
        from .views.copd_views import COPDPredictionView
        from .views.heart_failure_views import HeartFailurePredictionView
