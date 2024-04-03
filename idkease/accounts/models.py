from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustUser(AbstractUser):
    choice=(
        ('Ward Member','Ward Member'),
        ('Users','Users'),
    )
    role=models.CharField(max_length=100,choices=choice,default="Users")


class Users(CustUser):
    aadhar=models.BigIntegerField(null=True)
    phone=models.IntegerField(null=True)
    options=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    gender=models.CharField(max_length=50,choices=options,default='Male')
    address=models.TextField(null=True)
    pincode=models.IntegerField(null=True)
    local_body=models.CharField(max_length=100,null=True)
    ward=models.CharField(max_length=100,null=True)

class Complaint(models.Model):
    localbody=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    description=models.TextField()
    is_solved=models.BooleanField(default=False)