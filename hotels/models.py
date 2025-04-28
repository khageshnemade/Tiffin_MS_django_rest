from django.db import models
from accounts.models import User

# Create your models here.
class Hotel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'hotel_owner'})
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Tiffin(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='tiffins')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='tiffin_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.name + " " + self.hotel.name