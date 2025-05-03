# models.py
from django.db import models

class CustomerMainPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()

    def __str__(self):
        return "Customer Main Page"

class Customer(models.Model):
    page = models.ForeignKey(CustomerMainPage, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='customers/logos/')
    description = models.TextField()

    def __str__(self):
        return self.name