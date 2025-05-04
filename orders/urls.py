from django.urls import path
from .views import OrderCreateView,DeliveryListView,AssignDeliveryBoyView
from accounts.views import DeliveryBoyView

urlpatterns=[
    path('orders/',OrderCreateView.as_view(),name='orders'),
    path('my-deliveries/',DeliveryListView.as_view(),name='my_deliveries'),
    path('assign-delivery/<int:pk>/', AssignDeliveryBoyView.as_view(), name='assign-delivery'),
    path('delivery_boys',DeliveryBoyView.as_view(),name='get-delivery-boy')
]