from rest_framework import generics
from .models import Hotel,Tiffin
from .serializers import HotelSerializer,TiffinSerializer
from accounts.permissions import IsAdminOrHotelOwner

class HotelCreateListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrHotelOwner]

    def get_queryset(self):
          # Allow hotel owners to see their own hotels, but admins can see all
         if self.request.user.role == 'hotel_owner':
           return self.queryset.filter(owner=self.request.user)
         return self.queryset.all() 
   

class TiffinCreateView(generics.CreateAPIView):
        queryset=Tiffin.objects.all()
        serializer_class=TiffinSerializer
        permission_classes=[IsAdminOrHotelOwner] #Only hotel_owner create hotels

        def get_queryset(self):
         if self.request.user.role == 'hotel_owner':
             return self.queryset.filter(hotel_owner=self.request.user) 
         return self.queryset.all()
        
class TiffinListView(generics.ListAPIView):
    queryset=Tiffin.objects.all()
    serializer_class=TiffinSerializer
    permission_classes=[]#no auth reuired