from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllDestinations.as_view(), name='home'),
    path('add/', views.add_destination, name='add_destination'),
    path('contact/', views.contact, name='contact'),
    path('<str:name>/', views.destination_detail, name='view_destination'),
    path('<str:name>/edit_review/<int:review_id>/', views.review_edit,
         name='edit_review'),
    path('<str:name>/delete_review/<int:review_id>/', views.review_delete,
         name='review_delete'),

]
