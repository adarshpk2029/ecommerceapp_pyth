from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product_images")
    options=(
        ('smart Phones','smart Phones'),
        ('Shorts','Shorts'),
        ('Tablet','Tablet'),
        ('Smart Watch','Smart Watch')

    )
    categories=models.CharField(max_length=200,choices=options)
    stock=models.IntegerField()
    def __str__(self):
        return self.title


class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default="added")

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500)
    options=(
        ("Order Placed","Order Placed"),
        ("Cancelled","Cancelled"),
        ("Shipped","Shipped"),
        ("Out For Delivery","Out For Delivery"),
        ("Delivered","Delivered")
    )
    order_status=models.CharField(max_length=100,default="Order Placed")


class Review(models.Model):
    review=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)