from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

from django.core.mail import send_mail
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

class WardMemberCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role="WardMember")
            return Response(data={'status':1,'data':serializer.data})
        else:
            error_messages = ' '.join([error for errors in serializer.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)      

class AuthorityCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=AuthoritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role="Authority")
            return Response(data={'status':1,'data':serializer.data})
        else:
            error_messages = ' '.join([error for errors in serializer.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)      

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
        return Response(data={'status':1,'data':ser.data})
    def post(self,request):
        ser=ComplaintSerializer(data=request.data)
        if ser.is_valid():
            data=ser.save()
            Tracking.objects.create(complaint_id=data)
            return Response(data={'status':1,'data':ser.data})
        else:
            error_messages = ' '.join([error for errors in ser.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)

class SolvedComplaints(APIView):
    def get(self,request,*args,**kwargs):
            comp=Complaint.objects.filter(is_solved=True)
            print(comp)
            ser=ComplaintSerializer(comp,many=True)
            return Response(data={'status':1,'data':ser.data})

class ComplaintsViewUser(APIView):
    def get(self,request,*args,**kwargs):
            comp=Complaint.objects.filter(user=request.user)
            print(comp)
            ser=ComplaintSerializer(comp,many=True)
            return Response(data={'status':1,'data':ser.data})


class UnSolvedComplaints(APIView):
    def get(self,request,*args,**kwargs):
            comp=Complaint.objects.filter(is_solved=False)
            print(comp)
            ser=ComplaintSerializer(comp,many=True)
            return Response(data={'status':1,'data':ser.data})



class RecommendationView(APIView):
    def get(self,request,*args,**kwargs):
        recom=Recommendation.objects.all()
        print(recom)
        ser=RecommendationSerializer(recom,many=True)
        return Response(data={'status':1,'data':ser.data})
    def post(self,request):
        ser=RecommendationSerializer(data=request.data)
        if ser.is_valid():
            data=ser.save()
            Tracking.objects.create(recom_id=data)
            return Response(data={'status':1,'data':ser.data})
        else:
            error_messages = ' '.join([error for errors in ser.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)

class ApprovedRecommendationsView(APIView):
    def get(self,request,*args,**kwargs):
        recom=RecommendationSerializer.objects.filter(status=True)
        print(recom)
        ser=RecommendationSerializer(recom,many=True)
        return Response(data={'status':1,'data':ser.data})

class RecommendationsViewUser(APIView):
    def get(self,request,*args,**kwargs):
        recom=RecommendationSerializer.objects.filter(user=request.user)
        print(recom)
        ser=RecommendationSerializer(recom,many=True)
        return Response(data={'status':1,'data':ser.data})
    

class TrackingView(APIView):
     def get(self,request,**kwargs):
        pk=kwargs.get('pk')
        comp=Complaint.objects.get(id=pk)
        track=Tracking.objects.get(complaint_id=comp)
        ser=TrackingSerializer(track)
        return Response({'status':1,'data':ser.data})
     

class MemberStatusComp(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Complaint.objects.get(id=id)
        comp.member= "Accept"
        comp.save()
        track=Tracking.objects.get(complaint_id=comp)
        track.is_member=True
        track.save()
        subject = 'Complaint Status Member'
        message = f' Hai {request.user.username} Your Complaint is Accepted'
        from_email = 'demoarun4@gmail.com' 
        
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        return Response({'status':1,'Msg':"Accept Successfully"})

class AuthorityStatusComp(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Complaint.objects.get(id=id)
        comp.authority= "Accept"
        comp.save()

        track=Tracking.objects.get(complaint_id=comp)
        track.is_authority=True
        track.save()
        
        subject = 'Complaint Status Authority'
        message = f' Hai {request.user.username} Your Complaint is Accepted'
        from_email = 'demoarun4@gmail.com' 
        
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return Response({'status':1,'Msg':"Accept Successfully"})

class MemberStatusCompReject(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Complaint.objects.get(id=id)
        comp.member= "Reject"
        comp.save()
        track=Tracking.objects.get(complaint_id=comp)
        track.is_member=True
        track.save()

        subject = 'Complaint Status Member'
        message = f' Hai {request.user.username},Sorry to inform Your Complaint is Rejected'
        from_email = 'demoarun4@gmail.com'
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return Response({'status':1,'Msg':"Rejected"})

class AuthorityStatusCompReject(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Complaint.objects.get(id=id)
        comp.authority= "Reject"
        comp.save()

        track=Tracking.objects.get(complaint_id=comp)
        track.is_authority=True
        track.save()

        subject = 'Complaint Status Authority'
        message = f' Hai {request.user.username},Sorry to inform Your Complaint is Rejected'
        from_email = 'demoarun4@gmail.com'
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        
        return Response({'status':1,'Msg':"Rejected"})
          

class MemberStatusRecom(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Recommendation.objects.get(id=id)
        comp.member= "Accept"
        comp.save()
        track=TrackingRecom.objects.get(recom_id=comp)
        track.is_member=True
        track.save()
        subject = 'Complaint Status Member'
        message = f' Hai {request.user.username} Your Complaint is Accepted'
        from_email = 'demoarun4@gmail.com' 
        
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        return Response({'status':1,'Msg':"Accept Successfully"})

class AuthorityStatusRecom(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Recommendation.objects.get(id=id)
        comp.authority= "Accept"
        comp.save()

        track=TrackingRecom.objects.get(complaint_id=comp)
        track.is_authority=True
        track.save()
        
        subject = 'Complaint Status Authority'
        message = f' Hai {request.user.username} Your Complaint is Accepted'
        from_email = 'demoarun4@gmail.com' 
        
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return Response({'status':1,'Msg':"Accept Successfully"})

class MemberStatusRecomReject(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Recommendation.objects.get(id=id)
        comp.member= "Reject"
        comp.save()
        track=TrackingRecom.objects.get(complaint_id=comp)
        track.is_member=True
        track.save()

        subject = 'Complaint Status Member'
        message = f' Hai {request.user.username},Sorry to inform Your Complaint is Rejected'
        from_email = 'demoarun4@gmail.com'
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return Response({'status':1,'Msg':"Rejected"})

class AuthorityStatusRecomReject(APIView):
     def post(self,request,**kwargs):
        id=kwargs.get('pk')
        comp=Recommendation.objects.get(id=id)
        comp.authority= "Reject"
        comp.save()

        track=TrackingRecom.objects.get(complaint_id=comp)
        track.is_authority=True
        track.save()

        subject = 'Complaint Status Authority'
        message = f' Hai {request.user.username},Sorry to inform Your Complaint is Rejected'
        from_email = 'demoarun4@gmail.com'
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        
        return Response({'status':1,'Msg':"Rejected"})
          

class InformationView(APIView):
    def get(self,request,*args,**kwargs):
        comp=Informations.objects.all()
        print(comp)
        ser=InformationSerializer(comp,many=True)
        return Response(data={'status':1,'data':ser.data})
    def post(self,request):
        ser=InformationSerializer(data=request.data)
        if ser.is_valid():
            data=ser.save()
            Informations.objects.create(complaint_id=data)
            return Response(data={'status':1,'data':ser.data})
        else:
            error_messages = ' '.join([error for errors in ser.errors.values() for error in errors])
            return Response(data={'status':0,'msg': error_messages}, status=status.HTTP_400_BAD_REQUEST)
        

