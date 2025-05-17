from django.urls import path
from . import views

# urlpatterns 
urlpatterns = [
    path('', views.home, name='home'),

    # cbvs
    path('add_item/', views.ItemCreateView.as_view(), name='add_item'),
    path('items/', views.ItemListView.as_view(), name='items'),
]