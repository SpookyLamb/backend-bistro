from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer