from rest_framework import serializers
from .models import Hotel,Tiffin
from django.core.exceptions import ValidationError

class TiffinShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiffin
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    tiffins = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Hotel
        fields='__all__'
    def create(self, validated_data):
        validated_data['owner']=self.context['request'].user
        return super().create(validated_data)
    


class TiffinSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)
    hotel_location = serializers.CharField(source='hotel.location', read_only=True)
    hotel_owner_username = serializers.CharField(source='hotel.owner.username', read_only=True)

    class Meta:
        model = Tiffin
        fields = '__all__'  # or list fields explicitly if you want more control
        # Example: ['id', 'hotel', 'name', 'description', 'price', 'available', 'image', 'hotel_name', 'hotel_location', 'hotel_owner_username']

    def validate_image(self, image):
        if image and image.size > 20 * 1024 * 1024:  # 20 MB
            raise ValidationError("Image file size should not exceed 20 MB")
        return image

   