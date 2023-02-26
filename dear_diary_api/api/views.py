from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import MasterTable,userLogin
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from main.models import userLogin
from .serializers import userLoginSerializer, MasterTableSerializer

@api_view(['Get'])
def api(request):
    ls_api={
        'Home':'',
        'Register':'register/',
        'userExist':'checkuser/',
        'userAuthantication':'user/auth/',
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

@api_view(['POST'])
def userAuth(request):
    user=userLogin.objects.all()
    inUser=request.data
    for i in user:
        if ((str(i.userid)==str(inUser['userid'])) & (str(i.pswd) == str(inUser['pswd']))):
            return HttpResponse("True")
    return HttpResponse("False")

@api_view(['Get'])
def landing(request):
    return HttpResponse('<h1>Home Page</h1>')

@api_view(['GET', 'POST'])
def renamePage(request):
    user=request.GET.get('user')
    section=request.GET.get('section')
    page=request.GET.get('page')
    new_page=request.GET.get('new_page')
    t=MasterTable.objects.get(user=user, section=section, page=page)
    t.page=new_page
    t.save()
    return redirect('/home/%s' %user)
    

