from . import views
from django.urls import path

urlpatterns = [
    path('', views.AllDestinations.as_view(), name='home'),
    path('<str:name>/', views.destination_detail, name='view_destination'),
]