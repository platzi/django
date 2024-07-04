from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductListViewTests(TestCase):

    def test_should_return_200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse("list_product")
        Product.objects.create(
            name="test", description="test description", price="5", available=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)
