from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth.models import User

import datetime

# Create your views here.

def homeview(request):
    time=datetime.datetime.now()
    return HttpResponse(f'today is {time}')

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


