from django.urls import path
from . import views

urlpatterns=[
    path('',views.landing),
    path('api/',views.api),
    path('home/<str:user>', views.home, name='home'),
    path('register/',views.addUser),
    path("<str:id>",views.userExist),
    path('home/<str:user>/<str:section>/<str:page>',views.pagedata),
    #url for creating a new pagedata
    path('home/<str:user>/<str:section>/<str:page>/createpagedata/',views.pagedatacreate),
    #url for updating a already existing pagadata
    path('home/<str:user>/<str:section>/<str:page>/updatepagedata/',views.pagedataupdate),
    path("user/auth/",views.userAuth),
    path('renamePage/', views.renamePage),
    path('deletePage/', views.deletePage),
]
