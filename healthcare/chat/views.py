from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from chat.models import ChatMessages
from .serializers import MessageSerializer
from django.db.models import Q

User = get_user_model()

# Create your views here.

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def SendMessage(request):
    data = request.data
    print(data)
    u_from = User.objects.get(id=data['user_from'])
    print(u_from)
    u_to = User.objects.get(id=data['user_to'])
    print(u_to)
    messages = ChatMessages.objects.create(
    user_from=u_from,
    user_to=u_to,
    message=data["message"])
    return Response({'message':'success'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetMessage(request):
    data = request.data
    user_id = data["user_from"]
    other_id = data["user_to"]
    # messages = ChatMessages.objects.all()
    messages = ChatMessages.objects.filter(Q(user_from=user_id, user_to=other_id) | Q(user_from=other_id, user_to=user_id))
    messaageSerializer = MessageSerializer(messages, many=True)
    return Response(messaageSerializer.data)
