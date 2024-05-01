from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustUser(AbstractUser):
    choice=(
        ('WardMember','WardMember'),
        ('Users','Users'),
        ('Authority','Authority')
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

class Authority(CustUser):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)

    

class Complaint(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,null=True)
    localbody=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    description=models.TextField()
    choice=(
        ('Accept','Accept'),
        ('Reject','Reject'),
        ('Not Available','Not Available')
    )
    member=models.CharField(max_length=100,choices=choice,null=True,default="Not Available")
    authority=models.CharField(max_length=100,choices=choice,null=True,default="Not Available")
    is_solved=models.BooleanField(default=False)


class Recommendation(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,null=True)   
    localbody=models.CharField(max_length=200)
    ward_number=models.IntegerField()
    recommendation=models.TextField()
    status=models.BooleanField(default=False)

class Tracking(models.Model):
    complaint_id=models.ForeignKey(Complaint,on_delete=models.CASCADE)
    is_member=models.BooleanField(default=False)
    is_authority=models.BooleanField(default=False)
    solved=models.BooleanField(default=False)

class TrackingRecom(models.Model):
    recom_id=models.ForeignKey(Complaint,on_delete=models.CASCADE)
    is_member=models.BooleanField(default=False)
    is_authority=models.BooleanField(default=False)
    solved=models.BooleanField(default=False)


class Informations(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE)
    certificate=models.CharField(max_length=100)
    doc=models.TextField()
    criteria=models.TextField()