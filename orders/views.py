from rest_framework import generics,status
from rest_framework.response import Response
from accounts.models import User
from .models import Order
from .serializers import OrderSerializer
from accounts.permissions import IsAdminOrCustomer,IsAdminOrDeliveryBoy,IsAdmin

class OrderCreateView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAdminOrCustomer]

    def get_queryset(self):
        if self.request.user.role == 'customer':
            return self.queryset.filter(customer=self.request.user)
        return self.queryset.all()
    
#DeliveryBoy can see his deliveries
class DeliveryListView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAdminOrDeliveryBoy]

    def get_queryset(self):
        if self.request.user.role == 'delivery_boy':
            return self.queryset.filter(delivery_boy=self.request.user)
        return self.queryset.all()

class AssignDeliveryBoyView(generics.UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[IsAdmin]

    def patch(self, request, *args, **kwargs):
        order=self.get_object()
        delivery_boy_id=request.data.get('delivery_boy')
        try:
            delivery_boy=User.objects.get(id=delivery_boy_id,role='delivery_boy')
        except User.DoesNotExist:
            return Response({'error':'Delivery Boy Not Found'},status=status.HTTP_404_NOT_FOUND)
        order.delivery_boy=delivery_boy
        order.save()
        return Response(OrderSerializer(order).data)