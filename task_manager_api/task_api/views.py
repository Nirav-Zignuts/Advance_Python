from django.shortcuts import render
from .serializers import UserSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserAPI(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
    def get(self,request,pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({'data':serializer.data,'access_token':access_token,'refresh_token':refresh_token},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class TaskAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk = None):
        if pk:
            try:
                task = Task.objects.get(pk=pk)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializer(task)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serailzer = TaskSerializer(data=request.data)
        if serailzer.is_valid():
            print()
            # user = User.objects.get(username=serailzer.validated_data['user'])
            serailzer.save()
            return Response(serailzer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serailzer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    def delete(self,request,pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.is_deleted = True
        task.save()
        return Response({'success':'task deleted successfully'},status=status.HTTP_204_NO_CONTENT)