from django.urls import path
from .views import *


urlpatterns = [
    path("signup/",UserCreationView.as_view(),name="signup"), # signup User
    path("membersignup/",WardMemberCreationView.as_view(),name="membersignup"), # signup Member
    path("authoritysignup/",AuthorityCreationView.as_view(),name="authoritysignup"), # signup Member
    path('login/',CustomAuthToken.as_view(), name='token'), # sign in 

    path('complaints/',Complaints.as_view(),name='comp'),  # Complaints submit and all complaints view
    path('complaintsuser/',ComplaintsViewUser.as_view(),name='c_user'),  # user complaints view
    path('solvedcomplaints/',SolvedComplaints.as_view(),name='solve'),  # Solved complaints view
    path('Unsolvedcomplaints/',UnSolvedComplaints.as_view(),name='unsolve'),  # UnSolved complaints view

    path('recommendations/',RecommendationView.as_view(),name='recom'),  # Recommendations submit and all recommendations view
    path('recommendationsUser/',RecommendationsViewUser.as_view(),name='r_user'),  # user recommendations view
    path('aopprovedrecommendations/',ApprovedRecommendationsView.as_view(),name='apprecom'),  # Approved Recommendations view

    path('tracking/<int:pk>/',TrackingView.as_view(),name='track'),  # tracking  ,pass complaint id

    path('memberstatus/<int:pk>/',MemberStatusComp.as_view(),name='memstatus'),  #  member status complaint accept
    path('authoritystatus/<int:pk>/',AuthorityStatusComp.as_view(),name='memstatus'),  #  Authority status complaint accept
    path('memberstatusreject/<int:pk>/',MemberStatusCompReject.as_view(),name='memstatusreject'),  #  member status complaint reject
    path('authoritystatusreject/<int:pk>/',AuthorityStatusCompReject.as_view(),name='memstatusreject'),  #  Authority status complaint reject

    path('memberstatusRecommendation/<int:pk>/',MemberStatusRecom.as_view(),name='memstatusrecom'),  #  member status recommendation accept
    path('authoritystatusRecommendation/<int:pk>/',AuthorityStatusRecom.as_view(),name='memstatusrecom'),  #  Authority status recommendation accept
    path('memberstatusrejectRecommendation/<int:pk>/',MemberStatusRecomReject.as_view(),name='memstatusrejectrecom'),  #  member status recommendation reject
    path('authoritystatusrejectRecommendation/<int:pk>/',AuthorityStatusRecomReject.as_view(),name='memstatusrejectrecom'),  #  Authority status recommendation reject

    path('informations/',InformationView.as_view(),name='inform'),  # informations submit and all informations view
    
]