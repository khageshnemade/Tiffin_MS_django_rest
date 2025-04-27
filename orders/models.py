from django.db import models
from accounts.models import User
from hotels.models import Tiffin

# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders',limit_choices_to={'role':'customer'})
    tiffin=models.ForeignKey(Tiffin,on_delete=models.CASCADE)
    delivery_boy=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='deliveries',limit_choices_to={'role':'delivery_boy'})
    delivery_location = models.CharField(max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.email}"