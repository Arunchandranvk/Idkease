from rest_framework import serializers
from .models import *

class  UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Users
        fields=["id","username","aadhar","phone","gender","address","pincode","local_body","ward","username","password"]    

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data) 


class  ComplaintSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Complaint
        fields=['id','localbody','ward','subject','description','is_solved']