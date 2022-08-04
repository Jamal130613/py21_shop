from django.shortcuts import render
from requests import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from applications.cart.models import Order, CartItem
from applications.cart.serializers import OrderSerializer, CartItemSerializer


class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(cart=user.carts.first())
        return queryset


class OrderView(ModelViewSet):
    customer = serializers.ReadOnlyField(source='customer.email')
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
