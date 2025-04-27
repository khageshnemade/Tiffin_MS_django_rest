from django.urls import path,include
from .views import RegisterView,UserView,CustomTokenObtainPairView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserView, basename='user')
urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'), #create new user
   path('', include(router.urls)),
]