from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import MasterTable
from django.http import HttpResponse,JsonResponse
from main.models import userLogin
from .serializers import userLoginSerializer,MasterTableSerializer 
from rest_framework import status

@api_view(['Get'])
def api(request):
    ls_api={
        'Home':'',
        'Register':'register/',
        'userExist':'checkuser/',
        'api':'api/',

    }
    return Response(ls_api)

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
    serializer=userLoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("True")
    return HttpResponse("False")

def userExist(request,id):
    user=userLogin.objects.all()
    for i in user:
         if str(id)==str(i.userid):
            return HttpResponse("True")
        
    return HttpResponse("False")

@api_view(['Get'])
def landing(request):
    return HttpResponse('<h1>Home Page</h1>')

@api_view(['GET'])
def pagedata(request,user,section,page):
    table=MasterTable.objects.all()
    pageData=table.filter(user=user,section=section,page=page)
    serializer= MasterTableSerializer(pageData,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def pagedatacreate(request,user,section,page):
    dataReceived = request.data
    serializer = MasterTableSerializer(data=dataReceived)
    if MasterTable.objects.filter(**dataReceived).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def pagedataupdate(request,user,section,page):
    table=MasterTable.objects.get(user=user,section=section,page=page)
    serializer=MasterTableSerializer(instance=table, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
        
    
