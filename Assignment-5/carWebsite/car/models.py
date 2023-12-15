from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='car/media/car_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self) :
        return f"Car:{self.name}, Brand:{self.brand.name}" 
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)