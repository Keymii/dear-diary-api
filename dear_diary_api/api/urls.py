from django.urls import path
from . import views

urlpatterns=[
    path('',views.landing),
    path('api/',views.api),
    path('renamepage/', views.renamePage),
    path('register/',views.addUser),
    path("user/auth/",views.userAuth),
    path('renamePage/', views.renamePage),
    path('deletePage/', views.deletePage),
    path('home/<str:userid>/', views.home, name='home'),
    path('home/<str:userid>/<str:section>/<str:page>/',views.pagedata),
    #url for creating a new pagedata
    path('home/<str:userid>/<str:section>/<str:page>/createpagedata/',views.pagedatacreate),
    #url for updating a already existing pagadata
    path('home/<str:userid>/<str:section>/<str:page>/updatepagedata/',views.pagedataupdate),
    path("<str:userid>/",views.userExist),   
]
