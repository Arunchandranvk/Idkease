from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Users,Complaint
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
# Create your views here.


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        users=Users.objects.get(id=user.id)
        role = user.role
        name=user.username
        aadhar=users.aadhar
        email=user.email
        phone=users.phone
        gender=users.gender
        address=users.address
        pincode=users.pincode
        local_body=users.local_body
        ward=users.ward
        
        return Response(data={'status':1,'token': token.key,'data':{
            
            'role': role,
            'username':name,
            'aadhar':aadhar,
            'email':email,
            'phone_no':phone,
            'gender':gender,
            'address':address,
            'pincode':pincode,
            'local_body':local_body,
            'ward':ward
            }})

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role="Users")
            return Response(data={'status':1,'data':serializer.data})
        else:
            error_messages = ' '.join([error for errors in serializer.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)      
        

class Complaints(APIView):
    def get(self,request,*args,**kwargs):
        comp=Complaint.objects.all()
        print(comp)
        ser=ComplaintSerializer(comp,many=True)
        return Response(ser.data)
    def post(self,request):
        ser=ComplaintSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data={'status':1,'data':ser.data})
        else:
            error_messages = ' '.join([error for errors in ser.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)
