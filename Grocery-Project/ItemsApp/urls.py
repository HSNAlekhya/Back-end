from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_item, name='create_item'),
    path('all/', views.list_items, name='list_items'),
    path('details/<int:id>/', views.item_details, name='item_details'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]