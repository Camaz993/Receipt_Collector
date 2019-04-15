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

    def get_queryset(self):
        queryset = Receipt.objects.all()
        storeparam = self.request.query_params.get('store', None)
        before_purchase = self.request.query_params.get('before_date', None)
        after_purchase = self.request.query_params.get('after_date', None)
        at_purchase = self.request.query_params.get('at_date', None)
        before_update = self.request.query_params.get('before_update', None)
        after_update = self.request.query_params.get('after_update', None)
        at_update = self.request.query_params.get('at_update', None)

        if storeparam is not None:
            queryset = queryset.filter(store__iexact=storeparam)
        if before_purchase is not None:
            queryset = queryset.filter(purchase_date__lte=before_purchase)
        if after_purchase is not None:
                queryset = queryset.filter(purchase_date__gte=after_purchase)
        if at_purchase is not None:
            queryset = queryset.filter(purchase_date__exact=at_purchase)
        if before_update is not None:
                queryset = queryset.filter(date_updated__gte=before_update)
        if after_purchase is not None:
                queryset = queryset.filter(date_updated__lte=after_update)
        if at_update is not None:
            queryset = queryset.filter(date_updated__exact=at_update)

        return queryset




#class ReceiptFilter(filters.FilterSet):
#    purchase_date_gte = django_filters.DateTimeFilter(name="purchase_date", lookup_expr='gte')
    #class Meta:
    #    model = Receipt
    #    fields = ['store', 'total_price', 'purchase_date', 'purchase_date_gte']
