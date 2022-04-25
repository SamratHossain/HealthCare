from rest_framework import serializers
from doctor.models import Category, Qualification
from accounts.models import UserAccount, Doctor
from doctor.serializers import DoctorSerializer
from .models import StudentModel, MarksModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarksModel
        fields = ['math', 'physics']

class StudentSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(read_only=True, many=True)

    class Meta:
        model = StudentModel
        fields = '__all__'