from django.urls import path
from . import views

# urlpatterns 
urlpatterns = [
    path('', views.home, name='home'),

    # cbvs
    path('add_item/', views.ItemCreateView.as_view(), name='add_item'),
    path('items/', views.ItemListView.as_view(), name='items'),

    # rims 
    path('rims/', views.RimListView.as_view(), name='rims'),
    path('rims/add/', views.RimCreateView.as_view(), name='rim-create'),
    path('rims/<int:pk>/', views.RimDetailView.as_view(), name='rim-detail'),
    path('rims/<int:pk>/edit/', views.RimUpdateView.as_view(), name='rim-update'),
    path('rims/<int:pk>/delete/', views.RimDeleteView.as_view(), name='rim-delete'),

    # Prints 
    path('prints/', views.PrintListView.as_view(), name='print-list'),
    path('prints/add/<int:rim_id>/', views.PrintCreateView.as_view(), name='print-create'),
    path('prints/<int:pk>/', views.PrintDetailView.as_view(), name='print-detail'),
    path('prints/<int:pk>/edit/', views.PrintUpdateView.as_view(), name='print-update'),
    path('prints/<int:pk>/delete/', views.PrintDeleteView.as_view(), name='print-delete'),
]