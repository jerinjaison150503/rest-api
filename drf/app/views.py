from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.

def fun0(request):
    if request.method=='GET':
        data=stud.objects.all()
        s= studSerializers(data,many=True)
        
    return JsonResponse(s.data,safe=False)