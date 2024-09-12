from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer,LoginSerializer



# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
  queryset=Company.objects.all()
  serializer_class=CompanySerializer



# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class LoginAPI(APIView):
    def post(self,request):
        data=request.data
        print(data)
        return Response({
             "status": True,
             "data":{}
    })    


            
        
    

