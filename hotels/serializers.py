from rest_framework import serializers
from .models import Hotel,Tiffin
from django.core.exceptions import ValidationError

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields='__all__'
    def create(self, validated_data):
        validated_data['owner']=self.context['request'].user
        return super().create(validated_data)
    
class TiffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiffin
        fields = ['id', 'name', 'description', 'price', 'available', 'image', 'hotel']

    # Optional: Add a validation method if needed
    def validate_image(self, value):
        if value and not value.name.endswith(('.jpg', '.jpeg', '.png')):
            raise serializers.ValidationError("Only .jpg, .jpeg, or .png files are allowed.")
        return value

   