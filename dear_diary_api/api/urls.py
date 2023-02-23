from django.urls import path
from . import views

urlpatterns=[
    path('home/<str:user>', views.home, name='home'),
    path('register/',views.addUser),
    path('',views.home)
]
