from django.urls import path
from cars.views import CarView


urlpatterns = [
    path('cars/', CarView.as_view() ),
]