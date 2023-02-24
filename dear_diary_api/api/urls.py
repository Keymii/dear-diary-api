from django.urls import path
from . import views

urlpatterns=[
    path('',views.landing),
    path('api/',views.api),
    path('home/<str:user>', views.home, name='home'),
    path('register/',views.addUser),
    path("<str:id>",views.userExist),
    path("user/auth/",views.userAuth),
]
