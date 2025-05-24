from django.urls import path
from . import views

# urlpatterns 
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]