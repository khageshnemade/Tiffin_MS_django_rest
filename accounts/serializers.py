from rest_framework import serializers
from .models import User
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
    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

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
