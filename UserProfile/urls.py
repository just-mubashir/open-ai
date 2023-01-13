from django.urls import path
from . import views

urlpatterns = [

    path('user', views.userprofile, name='userprofile'),

]
