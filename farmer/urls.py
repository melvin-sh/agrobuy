from django.urls import path
from . import views

app_name = 'farmer'

urlpatterns = [
    path('', views.see, name='see'),
]
