from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

#companies/{companyid}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        company = Company.objects.get(pk=pk)
        employees = Employee.objects.filter(company=company)
        serializer = EmployeeSerializers(employees,many=True, context ={'request': request})
        return Response(serializer.data)
     
    
    


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

