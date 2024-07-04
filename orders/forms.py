from django.forms import ModelForm
from .models import OrderProduct


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
