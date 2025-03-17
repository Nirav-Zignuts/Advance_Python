from django.urls import path,include
from rest_framework import routers
from .views import ProductAPIView

# router = routers.DefaultRouter()
# router.register('product_catlog', ProductAPIView ,basename='home')

urlpatterns = [
    path('product_catlog/', ProductAPIView.as_view(), name='product_catlog'),
    path('product_catlog/<int:id>/', ProductAPIView.as_view(), name='product_catlog_id'),
]


