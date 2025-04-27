from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        # Extract refresh token manually
        refresh = response.data.get('refresh', None)
        if refresh:
            # Set Refresh Token in HttpOnly Cookie
            response.set_cookie(
                key='refresh_token', 
                value=refresh, 
                httponly=True, 
                secure=True,   # if using HTTPS
                samesite='Lax', 
                max_age=3600*24*7  # 7 days
            )

            # Optional: remove refresh from body response
            response.data.pop('refresh', None)
        
        return response