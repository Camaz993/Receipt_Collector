from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from framework.serializers import CategorySerializer, ReceiptSerializer
from framework.models import Category, Receipt


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
