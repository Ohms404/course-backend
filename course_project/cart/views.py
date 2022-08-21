from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer