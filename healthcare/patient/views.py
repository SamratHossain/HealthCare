from django.shortcuts import render
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from doctor.models import Category, Qualification
from accounts.models import UserAccount, Doctor
from doctor.models import Review
from .serializers import CategorySerializer, UserSerializerForDoctorList
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from doctor.models import Experience
from doctor.serializers import ExperienceSerializer

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchCategory(request, name):
        print(name)
        category = Category.objects.filter(name__icontains=name)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def DoctorListInformation(request):
        doctorlist = User.objects.filter(IsDoctor=True)
        serializer = UserSerializerForDoctorList(doctorlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def DoctorListInformationTest(request):
        doctorlist = Qualification.objects.filter(Specialist='Neurology')
        serializer = ExperienceSerializerForDoctorList(doctorlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewExperience(request,id):
      experience = Experience.objects.filter(user=id)
      experienceSerializer = ExperienceSerializer(experience, many=True)
      return Response(experienceSerializer.data)

@api_view(['GET'])
def getReview(request):
        review = Review.objects.all()
        print(review)
        r = review.count()
        message = {"review": r}
        return Response(message)
        