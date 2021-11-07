from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from accounts.models import Doctor, Patient
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


User = get_user_model()

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['email'] = self.user.email
        data['isPatient'] = self.user.IsPatient
        data['IsDoctor'] = self.user.IsDoctor
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def DoctorSignUp(request):
    data = request.data
    email = data['email']
    NidOrPassport = data['NidOrPassport']
    RegistrationNumberBMDC = data['RegistrationNumberBMDC']
    if User.objects.filter(email=email):
        return Response({'error':'user with this email already exist'})

    elif Doctor.objects.filter(NidOrPassport=NidOrPassport):
        return Response({'error':'user with this nid or passport number already exist'})

    elif Doctor.objects.filter(RegistrationNumberBMDC=RegistrationNumberBMDC):
        return Response({'error':'user with this RegistrationNumber(BMDC) number already exist'})
    else:
        user = User.objects.create(
        email = data['email'],
        password = make_password(data['password']),
        IsDoctor = True
        )
        doctor = Doctor.objects.create(
            User = user,
            Title = data['Title'],
            FirstName = data['FirstName'],
            LastName = data['LastName'],
            Mobile = data['Mobile'],
            Gender = data['Gender'],
            DateOfBirth = data['DateOfBirth'],
            NidOrPassport = data['NidOrPassport'],
            RegistrationNumberBMDC = data['RegistrationNumberBMDC']
            )
        return Response({'success':'Doctor Register Successfully'})
   


@api_view(['POST'])
def PatientSignUp(request):
    data = request.data
    user = User.objects.create(
        email = data['email'],
        password = make_password(data['password']),
        IsPatient = True
    )
    patient = Patient.objects.create(
        User = user,    
        FirstName = data['FirstName'],
        LastName = data['LastName'],
        Mobile = data['Mobile'],
        Gender = data['Gender'],
        DateOfBirth = data['DateOfBirth'],
        District = data['District']
    )
    patient.save()
    return Response({'success':'Patient Register Successfully'})


