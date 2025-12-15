from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product

# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('list_products')

class ProductListView(ListView):
    model = Product
    template_name = 'list-products.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('list_products')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product_confirmation.html'
    success_url = reverse_lazy('list_products')