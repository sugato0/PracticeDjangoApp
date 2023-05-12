from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=50)
    email_verified = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20,blank=True)
    mobile_verified = models.BooleanField(default=False)
    site_id = models.BigIntegerField(blank=True)
    token = models.CharField(max_length=1000)
    
