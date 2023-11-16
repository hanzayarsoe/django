from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_name = models.CharField(max_length=100)
    customer_age = models.IntegerField()
    customer_address = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_email = models.EmailField()
    def __str__(self):
        return self.customer_name
    