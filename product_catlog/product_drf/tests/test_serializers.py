from rest_framework.test import APITestCase 
from product_drf.serializers import ProductSerializer
from decimal import Decimal
class ProductSerializerTestCase(APITestCase):
    def test_product_serializer(self):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 10.99,
            'quantity': 5,
            'is_active': True,
            'brand': 'Test Brand',
            'category': 'Test Category'
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, Decimal('10.99'))
        self.assertEqual(product.quantity, 5)
        self.assertTrue(product.is_active)
        self.assertEqual(product.brand, 'Test Brand')
        self.assertEqual(product.category, 'Test Category')

    def test_invalid_quantity(self):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 10.99,
            'quantity': -5,
            'is_active': True,
            'brand': 'Test Brand',
            'category': 'Test Category'
        }
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['non_field_errors'][0], 'Quantity cannot be negative')

    def test_invalid_quantity(self):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': -1010,
            'quantity': 5,
            'is_active': True,
            'brand': 'Test Brand',
            'category': 'Test Category'
        }
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['non_field_errors'][0], 'Price cannot be negative')