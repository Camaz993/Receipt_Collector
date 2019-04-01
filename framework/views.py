from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from framework.serializers import CategorySerializer
from framework.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
