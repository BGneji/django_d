from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', UserRegisterView.as_view(), name='login'),
]