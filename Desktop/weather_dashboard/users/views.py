from rest_framework import generics
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .serializers import RegisterSerializer, LocationUpdateSerializer
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()

class UpdateLocationView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LocationUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        if 'latitude' in data and 'longitude' in data and not ('location_city' in data or 'location_country' in data):
            user.location_city = None
            user.location_country = None

        return super().update(request, *args, **kwargs)
    
def login_page(request):
    return render(request, "login.html")

def dashboard_page(request):
    return render(request, "dashboard.html")

def register_page(request):
    return render(request, "register.html")

def Home_page(request):
    return render(request,'frontend.html')

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



