from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from .models import Product
from rest_framework.views import APIView

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductAPIView(APIView):

    def get(self, request ,id=None):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return response.Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return response.Response(serializer.data)
        

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'success': 'Product created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return response.Response({'success': 'Product updated successfully','data':serializer.data},status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        p = Product.objects.get(pk = id)
        serializer = ProductSerializer(p, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'success': 'Product updated successfully','data':serializer.data},status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return response.Response({'success': 'Product deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    


