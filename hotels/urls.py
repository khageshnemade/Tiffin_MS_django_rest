from django.urls import path
from .views import HotelCreateListView,TiffinCreateView,TiffinListView


urlpatterns=[
    path('hotels/',HotelCreateListView.as_view(),name='hotels'),
    path('tiffins/', TiffinCreateView.as_view(), name='tiffins'),
    path('tiffins-list/',TiffinListView.as_view(),name='tiffins-list'),
  

]