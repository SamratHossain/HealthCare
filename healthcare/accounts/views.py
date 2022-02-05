from django.shortcuts import render
from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.db.models import Q
from doctor.models import Experience, Qualification, DoctorInfo
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
        data['id'] = self.user.id
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
    
@api_view(['POST'])
def DoctorSignUp(request):
    data = request.data
    print("Doctor Data: ", data)

    user = User.objects.create(
            email = data['Email'],
            password = make_password(data['Password']),
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
            RegistrationNumberBMDC = data['Registration']
            )
    
    qualification = Qualification.objects.create(
            user = user,
            Specialist = data['Specialist'],
            DegreeName = data['DegreeName'],
            InstituteName = data['InstituteName'],
            Country = data['Country'],
            PassingYear = data['PassingYear'],
    )

    From = data["From"]
    To = data["To"]

    EmploymentPeriod = None

    if data["CurrentlyWorking"]:
        CurrentlyWorking = True
    else:
        CurrentlyWorking = False

    if not data["CurrentlyWorking"]:
        FromDateSplit = From.split("-")
        ToDateSplit = To.split("-")

        FromYear = int(FromDateSplit[0])
        FromMonth = int(FromDateSplit[1])
        FromDay = int(FromDateSplit[2])

        ToYear = int(ToDateSplit[0])
        ToMonth = int(ToDateSplit[1])
        ToDay = int(ToDateSplit[2])

        FromDate = date(FromYear, FromMonth, FromDay)
        ToDate = date(ToYear, ToMonth, ToDay)

        NumberOfDays = ToDate - FromDate

        number_of_days = NumberOfDays.days

        years = number_of_days // 365

        months = (number_of_days - years *365) // 30

        if years == 0:
            EmploymentPeriod = str(months) + " Month "
        else:     
            EmploymentPeriod = str(years) + " Years " +  str(months) + " Month "

    experience = Experience.objects.create(
           user = user,
           HospitalName = data['HospitalName'],   
           Designation = data['Designation'],   
           Department = data['Department'],   
           EmploymentPeriod = EmploymentPeriod,   
           CurrentlyWorking = CurrentlyWorking,   
           From = data['From'],   
           To = data['To'],   
    )


    Start = data['Start']
    End = data['End']

    StartTime = Start.split(":")
    StartHour = int(StartTime[0])
    StartMinute = StartTime[1]

    EndTime = End.split(":")
    EndHour = int(EndTime[0])
    EndMinute = EndTime[1]

    if StartHour > 12:
        StartHour = StartHour - 12
        Start = f'{StartHour}:{StartMinute} PM'
    else:
        Start = f'{StartHour}:{StartMinute} AM'


    if EndHour > 12:
        EndHour = EndHour - 12
        End = f'{EndHour}:{EndMinute} PM'
    else:
        End = f'{EndHour}:{EndMinute} AM'

    AvailableTime = f'{Start} - {End}'
    

    doctorInfo = DoctorInfo.objects.create(
          user = user,
          AvailableTime = AvailableTime,
          AvailableDay = data['AvailableDays'],
          ConsultationFee = data['ConsultationFee'],
          FollowUpFee = data['FollowUpFee'],
          WithinDuration = data['WithinDuration'],
          ConsultancyDuration = data['ConsultancyDuration'],
          NIDPhoto = data['NidPhoto'],
          ProfilePhoto = data['ProfilePhoto'],
        #   About = data['About'],

    )

    return Response({'success':'Doctor Register Successfully'})
    


@api_view(['POST'])
def PatientSignUp(request):
    data = request.data
    print(data)
    FirstName = data['FirstName']
    print('fName',FirstName)
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



