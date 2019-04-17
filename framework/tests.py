import self as self
from django.db.models import QuerySet
from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from framework.models import Category
from .models import Category
from .serializers import CategorySerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()
"""
    @staticmethod
    def create_category(category=""):
        if category != "":
            category.objects.create(category=Category)

    def setUp(self):
        # add test data
        self.create_category("supermaket")
        self.create_category("shop2")
        self.create_category("shop3")
"""

class GetAllCategoriesTest(BaseViewTest):
    def test_Categories(self):

        response = self.client.get(
            reverse("categories-all", kwargs={"version": "v1"})
        )

        expected = Category.objects.all()
        serialized = CategorySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

