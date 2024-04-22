from django.urls import path
from .views import *

urlpatterns = [
    path('diseases', DiseasesPredict.as_view(), name='predict-diseases' ),
]