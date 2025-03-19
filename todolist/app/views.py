from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import Taskserializers

# Create your views here.

class TaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=Taskserializers