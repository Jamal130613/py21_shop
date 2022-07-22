from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from applications.cart.models import Order
from applications.cart.serializers import OrderSerializer


class OrderView(ModelViewSet):
    customer = serializers.ReadOnlyField(source='customer.email')
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

