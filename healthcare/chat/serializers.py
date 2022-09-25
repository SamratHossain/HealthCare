from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ChatMessages
from accounts.models import Patient

PatientInfo = get_user_model()

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessages
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class PatientInfoSerializer(serializers.ModelSerializer):

    patientInfo = PatientSerializer(read_only=True, many=True)
    chatInfo = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = PatientInfo
        fields = ['patientInfo', 'chatInfo']



