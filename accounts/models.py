from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self,email,password,role=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not role:
            raise ValueError('Users must have a role')
        
        email=self.normalize_email(email)
        user=self.model(email=email,role=role,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role','admin')
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    role=models.CharField(max_length=20,choices=(('admin','Admin'),('hotel_owner', 'Hotel Owner'),('customer', 'Customer'),('delivery_boy', 'Delivery Boy'),))
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','role']

    def __str__(self):
        return self.email