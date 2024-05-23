from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone_number']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'title', 'category', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source = "customer.first_name")
    last_name = serializers.CharField(source = 'customer.last_name')
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'ticket_number']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'food_item', 'quantity']