from rest_framework import serializers
from .models import Hotel,Tiffin
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
   