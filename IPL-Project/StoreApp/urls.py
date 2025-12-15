from django.urls import path
from . import views

urlpatterns = [
    path('products/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/', views.ProductListView.as_view(), name='list_products'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit_product'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete_product')
]