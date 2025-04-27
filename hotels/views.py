from rest_framework import generics
from .models import Hotel,Tiffin
from .serializers import HotelSerializer,TiffinSerializer
from accounts.permissions import IsHotelOwner

class HotelCreateListView(generics.ListCreateAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    permission_classes=[IsHotelOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user) #Only hotel_owner see hotels


class TiffinCreateView(generics.CreateAPIView):
        queryset=Tiffin.objects.all()
        serializer_class=TiffinSerializer
        # permission_classes=[IsHotelOwner] #Only hotel_owner create hotels

        # def get_queryset(self):
        #  return self.queryset.filter(hotel_owner=self.request.user) 
        
class TiffinListView(generics.ListAPIView):
    queryset=Tiffin.objects.all()
    serializer_class=TiffinSerializer
    permission_classes=[]#no auth reuired