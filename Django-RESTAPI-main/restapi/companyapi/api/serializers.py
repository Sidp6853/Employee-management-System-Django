#creating serializers
from rest_framework import serializers;
from api.models import Company,Employee;


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


#Empolyee serializers

class EmployeeSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'
