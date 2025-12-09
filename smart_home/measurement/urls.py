from django.urls import path

from .views import sensor_data


urlpatterns = [
    path('', sensor_data),  # подключаем маршруты из приложения measurement
]