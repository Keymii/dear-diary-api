from django.urls import path
from . import views
urlpatterns = [
     path('',views.home),
    path('api/',views.api),
    path('register/',views.addUser),
    path("<str:id>",views.userExist),
]
