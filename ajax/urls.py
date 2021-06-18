from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getProfile/', views.getProfiles, name='getProfile'),
]
