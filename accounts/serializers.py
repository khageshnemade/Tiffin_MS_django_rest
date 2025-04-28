from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('id','email','first_name','last_name','role','password')
    
    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(self)
        # Ensure `self.user` is accessible
        if self.user:
            access=data.pop('access')
            data['Token']=access
            data['email'] = self.user.email
            data['first_name'] = self.user.first_name
            data['last_name'] = self.user.last_name
            data['role']=self.user.role
        else:
            raise serializers.ValidationError("User details are not accessible.")

        return data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        # Call the parent class validate method to refresh the token
        data = super().validate(attrs)

        # Extract the refresh token
        refresh_token = attrs.get('refresh', None)
        if not refresh_token:
            raise serializers.ValidationError("Refresh token is required.")

        # Decode the refresh token to access the user information
        try:
            refresh = RefreshToken(refresh_token)
            user = User.objects.get(id=refresh['user_id'])  # Replace `User` with your custom user model
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        
        # Add user details to the response
        access=data.pop('access')
        data['Token']=access
        data['email'] = user.email
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['role'] = getattr(user, 'role', None)  # Include role if it exists on the user model

        return data
       
       
    