from django.db import models

# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    
