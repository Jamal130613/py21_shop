from rest_framework import serializers
from applications.cart.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.email')
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        quantity_order = validated_data['quantity']
        product = validated_data['product']
        product_quantity = product.amount

        if quantity_order > product_quantity:
            raise serializers.ValidationError(f'There is no quantity like this, we have {product_quantity} products!')
        product.amount -= quantity_order
        product.save()
        return super().create(validated_data)
