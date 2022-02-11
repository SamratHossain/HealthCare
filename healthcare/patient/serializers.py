from rest_framework import serializers
from doctor.models import Category, Qualification
from accounts.models import UserAccount, Doctor
from doctor.serializers import DoctorSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
