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
        model=Tiffin
        fields='__all__'
   

    def validate_image(image):
        if image.size > 20 * 1024 * 1024:  # Limit file size to 5 MB
            raise ValidationError("Image file size should not exceed 20 MB")
   