from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Both Passwords must match'})
        return data
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'])
        
        return user
    

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source='user.username')
    
    class Meta:
        model = Task
        fields = ['id','title','description','user','created','is_completed']
    
    def validate(self, data):
        print(data['user']['username'])
        if not User.objects.filter(username=data['user']['username']).exists():
            raise serializers.ValidationError({'user': 'User not found'})
        return data
    def create(self, validated_data):
        user = User.objects.get(username=validated_data['user']['username'])
        if user is None:
            raise serializers.ValidationError({'user': 'User not found'})
        task = Task.objects.create(title=validated_data['title'],description=validated_data['description'],user=user)
        return task
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance
   