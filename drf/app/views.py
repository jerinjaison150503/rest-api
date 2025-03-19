from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# def fun0(request):
#     if request.method=='GET':
#         data=stud.objects.all()
#         s= studSerializers(data,many=True)
        
#     return JsonResponse(s.data,safe=False)

# @csrf_exempt  
# def fun1(request,pk):
#     try:
#         demo=stud.objects.get(pk=pk)
        
#     except:
#         return HttpResponse("invalid")
#     if request.method=='GET':
#         s=studModelSerilizer(demo)
#         return JsonResponse(s.data)



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
    
    
# @api_view(['GET','PUT','DELETE'])
# def fun1(req,pk):
#     try:
#         demo=stud.objects.get(pk=pk)
#     except stud.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if req.method=='GET':
#         s=studModelSerilizer(demo)
#         return Response(s.data)
#     elif req.method=='PUT':
#         s=studModelSerilizer(demo,data=req.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response (status=status.HTTP_204_NO_CONTENT)
#     elif req.method=='DELETE':
#         demo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)             
            
            
class fun2(APIView):
    
    def get(self,req,pk):
        try:    
            demo=stud.objects.get(pk=pk)
            s=studModelSerilizer(demo)
            return Response(s.data)
        except stud.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)
        
    def put(self,req,pk):
        try:
            demo=stud.objects.get(pk=pk)
            s=studModelSerilizer(demo,data=req.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except stud.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,req,pk):
        try:
            demo=stud.objects.get(pk=pk)
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)