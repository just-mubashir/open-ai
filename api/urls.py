from django.urls import path
from . import views

urlpatterns = [

    path('api', views.api_home, name='api'),

]
