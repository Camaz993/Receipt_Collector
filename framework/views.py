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

    '''GET requests with described query optional parameters to filter
    
        No query parameters --> No IF statements are executed
        Some --> executed and filters applied on the rolling query set '''
    def get_queryset(self):
        queryset = Receipt.objects.all()

        storeparam = self.request.query_params.get('store', None)
        before_purchase = self.request.query_params.get('before_date', None)
        after_purchase = self.request.query_params.get('after_date', None)
        at_purchase = self.request.query_params.get('at_date', None)
        before_update = self.request.query_params.get('before_update', None)
        after_update = self.request.query_params.get('after_update', None)
        at_update = self.request.query_params.get('at_update', None)
        price_gt = self.request.query_params.get('price_gt', None)
        price_lt = self.request.query_params.get('price_lt', None)

        #STORE FILTER
        if storeparam is not None:
            queryset = queryset.filter(store__iexact=storeparam)

        #PURCHASE DATE FILTERS
        if before_purchase is not None:
            queryset = queryset.filter(purchase_date__lte=before_purchase)
        if after_purchase is not None:
                queryset = queryset.filter(purchase_date__gte=after_purchase)
        if at_purchase is not None:
            queryset = queryset.filter(purchase_date__exact=at_purchase)

        #DATE UPDATED FILTERS
        if before_update is not None:
                queryset = queryset.filter(date_updated__lte=before_update)
        if after_update is not None:
                queryset = queryset.filter(date_updated__gte=after_update)
        if at_update is not None:
            queryset = queryset.filter(date_updated__exact=at_update)

        #PRICE FILTERS
        if price_gt is not None:
            queryset = queryset.filter(price_gt=price_gt)
        if price_lt is not None:
            queryset = queryset.filter(price_lt=price_lt)

        return queryset