from rest_framework import serializers
from .models import CustomUser

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']  
        )
        return user


class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('location_city', 'location_country', 'latitude', 'longitude')

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email  
        return token

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        return super().validate(attrs)

