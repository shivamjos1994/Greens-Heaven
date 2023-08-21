from django.db import models

# Create your models here.
class Checkout(models.Model):
     name=models.CharField(max_length=30)
     email=models.EmailField()
     address=models.CharField(max_length=30)
     invoice_no=models.IntegerField(unique=True)
     total_bill=models.IntegerField()
     payment=models.CharField(max_length=30)
     #suggestions=models.TextField(max_length=100)
     class Meta:
         db_table="Checkout"


