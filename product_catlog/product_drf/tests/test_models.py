from django.test import TestCase
from product_drf.models import Product

class ProductTestCase(TestCase):
           
    def test_product_creation(self):
        name = 'Test Product'
        description = 'Test Description'
        price = 10.9
        quantity = 5
        is_active = True
        brand = 'Test Brand'
        category = 'Test Category'
        
        product = Product.objects.create(name = name ,description = description, price = price, quantity = quantity, is_active = is_active, brand = brand, category = category)
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.9)
        self.assertEqual(product.quantity, 5)
        self.assertTrue(product.is_active, True)
        self.assertEqual(product.brand, 'Test Brand')
        self.assertEqual(product.category, 'Test Category')

    def test_str(self):
        produt = Product(name = "Test Product")
        self.assertEqual(produt.__str__(), 'Test Product')

    
    