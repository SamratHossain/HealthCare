from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from chat.models import ChatMessages
from .serializers import MessageSerializer
from django.db.models import Q
from accounts.models import Patient
from .serializers import PatientInfoSerializer
import json

from twilio.rest import Client

User = get_user_model()

# Create your views here.

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def SendMessage(request):
    data = request.data
    print(data)
    message = data['message']
    mobile = data['mobile']
    sid='AC3948eeff2a9599e2c69f8cdeae9d5034'
    authToken='39f38f9c214e048f6f3231a1ffe19339'
    client = Client(sid, authToken)
    message = client.messages.create(to=f'whatsapp:+880{mobile}',
                                 from_='whatsapp:+14155238886',
                                 body=message)

    return Response({'message':'success'})

