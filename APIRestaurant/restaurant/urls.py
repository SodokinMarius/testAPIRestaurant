
from django.contrib import admin
from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns = [
    path('restaurants/',views.RestaurantAPIView.as_view(),name='coordonnes')
]
