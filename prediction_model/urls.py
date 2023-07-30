# my_project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/disease/prediction/', include('prediction_app.urls')),
]
