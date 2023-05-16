from django.urls import path
from .views import viewHomePage

urlpatterns = [
    path('home/', viewHomePage, name='home_page'),
]