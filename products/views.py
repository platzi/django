from django.urls import reverse_lazy
from django.views import generic

from products.models import Product
from .forms import ProductForm

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'