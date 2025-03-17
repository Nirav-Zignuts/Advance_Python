from rest_framework import serializers
from .models import Product
from rest_framework import status

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate(self, attrs):
        if attrs.get('quantity') is None:
            return attrs
        qty = attrs.get('quantity')
        if qty < 0:
            raise serializers.ValidationError('Quantity cannot be negative', code=status.HTTP_400_BAD_REQUEST)
        price = attrs.get('price')
        if price < 0:
            raise serializers.ValidationError('Price cannot be negative', code=status.HTTP_400_BAD_REQUEST)
        return attrs  