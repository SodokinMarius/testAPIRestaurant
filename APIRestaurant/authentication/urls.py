
from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path('register/',views.SignUpView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    #path('login/',views.AccessTokenObtainView.as_view(),name='login')
    path('api_keys/',TokenObtainPairView.as_view(),name='api_keys'),
]



