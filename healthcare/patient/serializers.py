from rest_framework import serializers
from django.contrib.auth import get_user_model
from doctor.models import Category, Qualification
from accounts.models import UserAccount, Doctor
from doctor.serializers import DoctorSerializer
from doctor.models import Qualification, Experience, DoctorInfo, Review
from accounts.models import Doctor


DoctorListInfo = get_user_model()

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ExprienceSerializerForDoctorList(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ['HospitalName', 'CurrentlyWorking']

class QualificationSerializerForDoctorList(serializers.ModelSerializer):

    # expInfo = ExperienceSerializerForDoctorList(read_only=True, many=True)

    class Meta:
        model = Qualification
        fields = ['Specialist', 'DegreeName']




class DoctorInfoSerializerForDoctorList(serializers.ModelSerializer):

    class Meta:
        model = DoctorInfo
        fields = ['ConsultationFee', 'ProfilePhoto']

class DoctorSerializerForDoctorList(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['Title', 'FirstName', 'LastName']

# class ReviewSerializerForDoctorList(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ['ConsultationFee', 'ProfilePhoto']



class UserSerializerForDoctorList(serializers.ModelSerializer):

    qualificationInfo = QualificationSerializerForDoctorList(read_only=True, many=True)
    experienceInfo = ExprienceSerializerForDoctorList(read_only=True, many=True)
    doctorInfo = DoctorInfoSerializerForDoctorList(read_only=True, many=True)
    doctor = DoctorSerializerForDoctorList(read_only=True, many=True)

    class Meta:
        model = DoctorListInfo
        fields = ['id', 'qualificationInfo', 'experienceInfo', 'doctorInfo', 'doctor']
