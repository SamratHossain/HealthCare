from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from chat.models import ChatMessages

User = get_user_model()

# Create your views here.

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def SendMessage(request):
    data = request.data
    print(data)
    print(data["user_from"])
    print(data["user_to"])
    print(data["message"])
    u_from = User.objects.get(id=data['user_from'])
    print(u_from)
    u_to = User.objects.get(id=data['user_to'])
    print(u_to)
    messages = ChatMessages.objects.create(
    user_from=u_from,
    user_to=u_to,
    message=data["message"])
    return Response({'message':'success'})
