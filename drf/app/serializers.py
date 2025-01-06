from rest_framework import serializers
from .models import *

# class studSerializers(serializers.Serializer):
#     name=serializers.CharField()
#     email=serializers.CharField()
    
    
class studModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model=stud
        fields='__all__'
    