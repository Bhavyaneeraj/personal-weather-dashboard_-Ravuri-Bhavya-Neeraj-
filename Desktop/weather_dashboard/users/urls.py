from django.urls import path
from .views import RegisterView, UpdateLocationView,login_page,dashboard_page,register_page,CustomTokenObtainPairView,Home_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login-page/', login_page, name='login_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('register-page/', register_page, name='register_page'),
    path('register/', RegisterView.as_view()),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('update-location/', UpdateLocationView.as_view()),
]
