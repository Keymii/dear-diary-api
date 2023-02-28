from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import MasterTable,userLogin, Session
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from .serializers import userLoginSerializer,MasterTableSerializer 
from rest_framework import status

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

def login(request):
    session_key = request.session.get('session_key')
    userid=request.POST.get('userid')
    if session_key:
        try:
            session = Session.objects.get(session_key=session_key)
            return redirect('/home/%s' %userid)
        except Session.DoesNotExist:
            pass
    if request.method=='POST':
        pswd = request.POST.get('pswd')
        try:
            user=userLogin.objects.get(userid=userid)
            if check_password(pswd, user.pswd):
                session=Session.create(user, request.session.session_key)
                request.session['session_key'] = session.session_key
                return redirect('/home/%s' %userid)
            
            else:
                return render(request, 'login.html', {'error_message': 'Incorrect password.'})
        except userLogin.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'User does not exist.'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    session_key=request.session.get('session_key')
    if session_key:
        try:
            session=Session.objects.get(session_key=session_key)
            session.delete()
        except Session.DoesNotExist:
            pass
    request.session.flush()
    return render(request, 'login.html')



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
