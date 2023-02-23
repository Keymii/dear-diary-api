from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import MasterTable
from django.http import HttpResponse
from main.models import userLogin
from .serializers import ItemSerializer

@api_view(['GET'])
def home(request, user):
    table=MasterTable.objects.all()
    user=table.filter(user=user)
    sections=[]
    pages=[]
    for i in user:
        sections.append(i.section)
    sections=[*set(sections)]
    for section in sections:
        page=user.filter(section=section)
        section_page=[]
        for j in page:
            section_page.append(j.page)
        pages.append(section_page)
    data=dict(zip(sections, pages))
    return Response(data)

@api_view(['POST'])
def addUser(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Diary created Successfully! Congratulation..")
    return HttpResponse("User Alrady exist")

@api_view(['GET'])
def landing(request):
    return HttpResponse("Home Page")
