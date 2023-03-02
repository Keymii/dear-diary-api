from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import MasterTable,userLogin,Session
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from django.contrib.auth.hashers import check_password
from main.models import userLogin
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
        'renamePage':'renamePage/',
        'creating pageData':'home/userid/page/createpagedata/',
        'Updating pageData':'home/userid/page/updatepagedata/',
        'Showing pageData':'home/userid/page/',

        }
    return Response(ls_api)

@api_view(['GET','POST'])
def login(request):
    data=request.data
    session_key=data['session_key']
    userid=data['userid']
    if session_key:
        try:
            session=Session.objects.get(session_key=session_key)
            return HttpResponse(True)
        except Session.DoesNotExist:
            pass
    pswd=data['pswd']
    try:
        user=userLogin.objects.get(userid=userid)
        if check_password(pswd, user.pswd):
            session1=Session.create(user, request.session.session_key)
            request.session['session_key'] = session1.session_key
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    except userLogin.DoesNotExist:
        return HttpResponse(False)

    
    
@api_view(['GET', 'POST'])
def logout(request):
    data=request.data
    session_key=data['session_key']
    if session_key:
        try:
            session=Session.objects.get(session_key=session_key)
            session.delete()
        except Session.DoesNotExist:
            pass
    request.session.flush()
    return HttpResponse(True)

@api_view(['GET'])
def home(request, userid):
    table=MasterTable.objects.all()
    user=table.filter(userid=userid)
    sections=[userid]
    pages=[]
    for section in sections:
        page=user.filter(userid=userid)
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

@api_view(['GET'])
def userExist(request,userid):
    user=userLogin.objects.all()
    for i in user:
         if str(userid)==str(i.userid):
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

@api_view(['GET'])
def pagedata(request,userid,page):
    table=MasterTable.objects.all()
    pageData=table.filter(userid=userid,page=page)
    serializer= MasterTableSerializer(pageData,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def pagedatacreate(request,userid,page):
    dataReceived = request.data
    serializer = MasterTableSerializer(data=dataReceived)
    if MasterTable.objects.filter(**dataReceived).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif serializer.is_valid():
        serializer.save()
    return Response(dataReceived)

@api_view(['PUT'])
def pagedataupdate(request,userid,page):
    dataReceived = request.data
    table=MasterTable.objects.get(userid=userid,page=page)
    serializer=MasterTableSerializer(instance=table, data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)
        
@api_view([ 'POST'])
def renamePage(request):
    inUser=request.data
    userid=inUser['userid']
    page=inUser['page']
    new_page=inUser['new_page']
    t=MasterTable.objects.get(userid=userid,page=page)
    t.page=new_page
    t.save()
    return redirect('/home/%s' %userid)

@api_view(['POST','DELETE'])
def deletePage(request):
    inUser=request.data
    userid=inUser['userid']
    page=inUser['page']
    t=MasterTable.objects.get(userid=userid,page=page)
    t.delete()
    return redirect('/home/%s' %userid)


