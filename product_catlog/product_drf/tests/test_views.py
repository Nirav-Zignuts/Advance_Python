from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from product_drf.models import Product
from product_drf.serializers import ProductSerializer
from rest_framework.test import APIClient



class ProductTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name='Test Product', description='Test Description', price=10.9, quantity=5, is_active=True, brand='Test Brand', category='Test Category')
    def test_get_all_products(self):
        url = reverse('product_catlog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_product(self):
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 110.9, 'quantity': 51, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        product = Product.objects.create(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'], is_active=data['is_active'], brand=data['brand'], category=data['category'])
        url = reverse('product_catlog_id', args=[product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
    def test_create_product(self):
        url = reverse('product_catlog')
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 110.9, 'quantity': 51, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        response =self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 110.9, 'quantity': 51, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        product = Product.objects.create(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'], is_active=data['is_active'], brand=data['brand'], category=data['category'])
        url = reverse('product_catlog_id', args=[product.pk])
        data = {'name': 'Test Product in testing with', 'description': 'Test Description', 'price': 1110.98, 'quantity': 56, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        response = self.client.put(url,data,format='json')
        print()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'Test Product in testing with')
        self.assertEqual(float(response.data['data']['price']), 1110.98)
        self.assertEqual(response.data['data']['quantity'], 56)

    def test_partial_update_product(self):
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 110.9, 'quantity': 51, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        product = Product.objects.create(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'], is_active=data['is_active'], brand=data['brand'], category=data['category'])
        url = reverse('product_catlog_id', args=[product.pk])
        data = {'name': 'Test Product in testing with'}
        response = self.client.patch(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'Test Product in testing with')

    def test_delete_product(self):
        data = {'name': 'Test Product for delete', 'description': 'Test Description', 'price': 110.9, 'quantity': 51, 'is_active': True, 'brand': 'Test Brand', 'category': 'Test Category'}
        product = Product.objects.create(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'], is_active=data['is_active'], brand=data['brand'], category=data['category'])
        url = reverse('product_catlog_id', args=[product.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(Product.objects.count())
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, 'Test Product')