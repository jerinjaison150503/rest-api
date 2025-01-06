from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
# Create your views here.

# def fun0(request):
#     if request.method=='GET':
#         data=stud.objects.all()
#         s= studSerializers(data,many=True)
        
#     return JsonResponse(s.data,safe=False)

@csrf_exempt  
def fun1(request,pk):
    try:
        demo=stud.objects.get(pk=pk)
        
    except:
        return HttpResponse("invalid")
    if request.method=='GET':
        s=studModelSerilizer(demo)
        return JsonResponse(s.data)
    # if request.method=='GET':
    #     data=stud.objects.all()
    #     s= studModelSerilizer(data,many=True)
    #     return JsonResponse(s.data,safe=False)
    # elif request.method=='POST':
    #     d=JSONParser().parse(request)
    #     s=studModelSerilizer(data=d)
    #     if s.is_valid():
    #         s.save()
    #         return JsonResponse(s.data,safe=False)
    #     else:
    #         return JsonResponse(s.errors)
            
            
            
