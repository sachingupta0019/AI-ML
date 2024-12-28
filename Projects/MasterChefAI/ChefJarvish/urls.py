from django.urls import path
from ChefJarvish.views import home

urlpatterns = [
    path('', home.as_view(), name= 'home')
]