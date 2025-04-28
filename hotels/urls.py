from django.urls import path
from .views import HotelCreateListView,TiffinCreateView,TiffinListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('hotels/',HotelCreateListView.as_view(),name='hotels'),
    path('tiffins/', TiffinCreateView.as_view(), name='tiffins'),
    path('tiffins-list/',TiffinListView.as_view(),name='tiffins-list'),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)