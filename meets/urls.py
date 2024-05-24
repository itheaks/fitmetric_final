from django.urls import path
from .views import *

urlpatterns = [
    path('', AppointmentView.as_view(), name='meets-home' ),
    path('appointment_list/', appointment_list, name='appointment_list' ),
    path('video_call/<str:uuid>/', VideoCallView, name='video_call' ),
]