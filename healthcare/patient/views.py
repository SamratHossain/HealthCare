from django.shortcuts import render
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from doctor.models import Category, Qualification
from accounts.models import UserAccount, Doctor
from .serializers import CategorySerializer, MarkSerializer, StudentSerializer
from rest_framework import viewsets

from .models import StudentModel, MarksModel

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewCategory(request):
    data = request.data
    print(data)
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
        

class StudentApi(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class MarksApi(viewsets.ModelViewSet):
    queryset = MarksModel.objects.all()
    serializer_class = MarkSerializer
    