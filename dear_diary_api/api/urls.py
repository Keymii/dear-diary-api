from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.addUser),
    path('',views.home)
]
