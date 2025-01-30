from . import views
from django.urls import path

urlpatterns = [
    path('', views.AllDestinations.as_view(), name='home'),
    path('<str:name>/', views.destination_detail, name='view_destination'),
    path('category/<str:category_name>/', views.filter_by_category, name='filter_by_category'),
]