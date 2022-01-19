from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.db.models import Q
from accounts.models import Doctor, Patient
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


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
        data['IsPatient'] = self.user.IsPatient
        data['IsDoctor'] = self.user.IsDoctor
        data['is_superuser'] = self.user.is_superuser
        data['IsApproved'] = self.user.IsApproved
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# & Doctor.objects.exclude(Q(NidOrPassport=NidOrPassport) & Q(RegistrationNumberBMDC=Registration))

@api_view(['POST'])
def CheckExistingDoctor(request):
    data = request.data
    Email = data['Email']
    NidOrPassport = data['NidOrPassport']
    Registration = data['Registration']

    
    if User.objects.filter(email=Email):
        message = {'EmailError':'user with this email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    elif Doctor.objects.filter(NidOrPassport=NidOrPassport):
        message = {'NidOrPassportError':'user with this nid/passport already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    elif Doctor.objects.filter(RegistrationNumberBMDC=Registration):
        message = {'RegistrationError':'user with this registration already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    else:
        
        return Response({'success':'Existing Account Check Successfully'})
    
# @api_view(['POST'])
# def DoctorSignUp(request):
#     data = request.data
#     Email = data['Email']
#     NidOrPassport = data['NidOrPassport']
#     Registration = data['Registration']

    
#     if User.objects.filter(email=Email):
#         message = {'EmailError':'user with this email already exist'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

#     elif Doctor.objects.filter(NidOrPassport=NidOrPassport):
#         message = {'NidOrPassportError':'user with this nid/passport already exist'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

#     elif Doctor.objects.filter(RegistrationNumberBMDC=Registration):
#         message = {'RegistrationError':'user with this registration already exist'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         user = User.objects.create(
#             email = data['Email'],
#             password = make_password(data['Password']),
#             IsDoctor = True
#             )
            
#         doctor = Doctor.objects.create(
#             User = user,
#             Title = data['Title'],
#             FirstName = data['FirstName'],
#             LastName = data['LastName'],
#             Mobile = data['Mobile'],
#             Gender = data['Gender'],
#             DateOfBirth = data['DateOfBirth'],
#             NidOrPassport = data['NidOrPassport'],
#             RegistrationNumberBMDC = data['Registration']
#             )
#         return Response({'success':'Doctor Register Successfully'})
    


@api_view(['POST'])
def PatientSignUp(request):
    data = request.data
    Email = data['Email']
    if User.objects.filter(email=Email):
        return Response({'error':'user with this email already exist'})
    else:
        user = User.objects.create(
        email = data['Email'],
        password = make_password(data['Password']),
        IsPatient = True
        )
        patient = Patient.objects.create(
            User = user,    
            FirstName = data['FirstName'],
            LastName = data['LastName'],
            Mobile = data['Mobile'],
            Gender = data['Gender'],
            DateOfBirth = data['DateOfBirth'],
        )
        return Response({'success':'Patient Register Successfully'})



