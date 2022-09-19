import email
from django.contrib.postgres import fields
from rest_framework import serializers
from .models import Experience, Qualification, DoctorInfo, Category
from accounts.models import Doctor

class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(read_only=True)
    qualificationInfo = QualificationSerializer(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = '__all__'

    def get_email(self, obj):
        email = obj.User.email
        return email

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'

class DoctorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorInfo
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


