from rest_framework import serializers
from .models import Order
from accounts.models import User

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='customer'),
        required=False
    )

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['ordered_at']

    def validate(self, data):
        tiffin = data.get('tiffin')
        delivery_location = data.get('delivery_location')

        if tiffin and delivery_location:
            hotel_location = tiffin.hotel.location
            if hotel_location.lower().strip() != delivery_location.lower().strip():
                raise serializers.ValidationError({
                    'delivery_location': f"This tiffin is only available in {hotel_location}."
                })

        return data

    def create(self, validated_data):
        request_user = self.context['request'].user

        validated_data.setdefault('delivered', False)

        if request_user.role == 'customer':
            validated_data['customer'] = request_user
        else:
            if 'customer' not in validated_data:
                raise serializers.ValidationError({'customer': 'Customer field is required for admins.'})

        delivery_location = validated_data.get('delivery_location')

        delivery_boy = User.objects.filter(
            role='delivery_boy',
            location__icontains=delivery_location
        ).first()

        if delivery_boy:
            validated_data['delivery_boy'] = delivery_boy

        return super().create(validated_data)
