from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer,CustomTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]




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


@swagger_auto_schema(
    request_body=serializers.Serializer(),  # Empty request body
    operation_description="Custom Token Refresh endpoint fetching refresh token from cookies only."
)
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class=CustomTokenRefreshSerializer
    def post(self, request, *args, **kwargs):
        # Get refresh token from the cookies
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({"detail": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Manually pass the refresh token to the serializer
        data = {'refresh': refresh_token}
        try:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response({"detail": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)