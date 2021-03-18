from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=10, null=True)
    Email = models.CharField(max_length=100, null=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.Name


class Tag(models.Model):
    Name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name


class Products(models.Model):
    CATEGORY= (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    Name = models.CharField(max_length=100, null=True)
    Price = models.FloatField(null=True)
    Category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    Description = models.CharField(max_length=200, null=True, blank=True)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    Tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    Status = models.CharField(max_length=200, null=True, choices= STATUS)
    note = models.CharField(max_length=1000, null=True )

    def __str__(self):
        return self.Products.Name