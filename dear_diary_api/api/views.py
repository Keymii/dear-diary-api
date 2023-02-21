from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from main.models import userLogin
from .serializers import ItemSerializer

@api_view(['POST'])
def addUser(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Diary created Successfully! Congratulation..")
    return HttpResponse("User Alrady exist")

@api_view(['GET'])
def home(request):
    return HttpResponse("Home Page")