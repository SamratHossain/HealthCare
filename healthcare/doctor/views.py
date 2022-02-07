import datetime
from datetime import date
from email import message
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Experience, Qualification, DoctorInfo, Category
from accounts.models import Doctor
from .serializers import ExperienceSerializer, QualificationSerializer, DoctorInfoSerializer, DoctorSerializer, CategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewPersonalInfo(request):
    current_user = request.user
    doctor = Doctor.objects.get(User=current_user)
    doctorSerializer = DoctorSerializer(doctor)
    return Response(doctorSerializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdatePersonalInfo(request):
    data = request.data
    pk = data['Id']
    doctor = Doctor.objects.get(id=pk)
    doctor.Title = data['Title']
    doctor.FirstName = data['FirstName']
    doctor.LastName = data['LastName']
    doctor.User.email = data['Email']
    doctor.Mobile = data['Mobile']
    doctor.Gender = data['Gender']
    doctor.DateOfBirth = data['DateOfBirth']
    doctor.save()
    doctor.User.save()
    message = {'success':'Personal Information Successfully Updated'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewDoctorInfo(request):
    current_user = request.user
    doctorInfo = DoctorInfo.objects.get(user=current_user)
    doctorInfoSerializer = DoctorInfoSerializer(doctorInfo)
    return Response(doctorInfoSerializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateDoctorlInfo(request):
    data = request.data
    print(data)

    Start = data['StartTime']
    End = data['EndTime']

    if Start and End is not '':

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

        pk = data['Id']
        doctor = DoctorInfo.objects.get(id=pk)
        doctor.AvailableTime = AvailableTime
        doctor.AvailableDay = data['AvailableDay']
        doctor.ConsultationFee = data['ConsultationFee']
        doctor.FollowUpFee = data['FollowupFee']
        doctor.WithinDuration = data['FollowUpDuration']
        doctor.ConsultancyDuration = data['ConsultDuration'] 
        doctor.save()
        
    else:
        pk = data['Id']
        doctor = DoctorInfo.objects.get(id=pk)
        doctor.AvailableDay = data['AvailableDay']
        doctor.ConsultationFee = data['ConsultationFee']
        doctor.FollowUpFee = data['FollowupFee']
        doctor.WithinDuration = data['FollowUpDuration']
        doctor.ConsultancyDuration = data['ConsultDuration'] 
        doctor.save()

    
    message = {'success':'Doctor Information Successfully Updated'}
    return Response(message, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ChangeDoctorProfilePic(request):
    data = request.data
    print(data)
    pk = data['Id']
    photo = DoctorInfo.objects.get(id=pk)
    photo.ProfilePhoto = request.FILES.get('ProfilePhoto')
    photo.save()

    message = {'success':'Change Doctor Profile Photo Successfully'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddExperience(request):
    data = request.data
    print(data)
    current_user = request.user

    From = data["From"]
    To = data["To"]

    EmploymentPeriod = None

    if data["CurrentlyWorking"]:
        CurrentlyWorking = True
    else:
        CurrentlyWorking = False


    print("current",data["CurrentlyWorking"])

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
                 user = current_user,
                 HospitalName = data['HospitalName'],
                 Designation = data['Designation'],
                 Department = data['Department'],
                 EmploymentPeriod = EmploymentPeriod,
                 CurrentlyWorking = CurrentlyWorking,
                 From = data['From'],
                 To = data['To']
    )

    message = {'success':'Experience Successfully Added'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewExperience(request):
    current_user = request.user
    experience = Experience.objects.filter(user=current_user).order_by('-id')
    experienceSerializer = ExperienceSerializer(experience, many=True)
    return Response(experienceSerializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateExperience(request):
    data = request.data
    print(data)
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

    print(EmploymentPeriod)
    pk = data['Id']
    experience = Experience.objects.get(id=pk)
    experience.HospitalName = data['HospitalName']
    experience.Designation = data['Designation']
    experience.Department = data['Department']
    experience.CurrentlyWorking = CurrentlyWorking
    experience.EmploymentPeriod = EmploymentPeriod
    experience.From = data['From']
    experience.To = data['To']
    experience.save()
    message = {'success':'Experience Successfully Updated'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteExperience(request):
    data = request.data
    pk = data['Id']

    print(pk)
    
    experience = Experience.objects.get(id=pk)
    experience.delete()

    message = {'success':'Experience Successfully Deleted'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewQualification(request):
    current_user = request.user
    qualification = Qualification.objects.get(user=current_user)
    qualificationSerializer = QualificationSerializer(qualification)
    return Response(qualificationSerializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateQualification(request):
    data = request.data
    print(data)
    pk = data['Id']

    qualification = Qualification.objects.get(id=pk)
    qualification.Specialist = data['Specialist']
    qualification.DegreeName = data['DegreeName']
    qualification.InstituteName = data['InstituteName']
    qualification.Country = data['Country']
    qualification.PassingYear = data['PassingYear']
    qualification.save()

    message = {'success':'Qualification Successfully Updated'}
    return Response(message, status=status.HTTP_200_OK)



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def AddCategory(request):
    data = request.data

    category = Category.objects.create(
         name = data['Name'],
         about = data['About'],
     )
    message = {'success':'Category Added Successfully'}
    return Response(message, status=status.HTTP_200_OK)


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
        
    
    