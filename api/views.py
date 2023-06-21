from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication

class EmployeeViewSet(viewsets.ModelViewSet): 
    serializer_class = EmployeeSerializer 
    queryset = EmployeeModel.objects.all()
    authentication_classes = (TokenAuthentication,)