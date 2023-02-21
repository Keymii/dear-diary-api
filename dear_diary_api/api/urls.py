from django.urls import path
from . import views

urlpatterns=[
    path('home/<int:id>', views.home, name='home'),
]