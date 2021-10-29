from django.urls import path
from cars.models import Complectation
from cars.views import *


urlpatterns = [
    path('cars/', CarView.as_view()),
    path('models/', CarModelView.as_view()),
    path("complectation/", ComplectationView.as_view()),
    path("credit/", CreditView.as_view()),

    
]