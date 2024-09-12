from rest_framework import serializers
from api.models import Company,Employee

# Create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = Company  # Corrected assignment
        fields = "__all__"  # Ensure this is a string for all fields

# Create serializers
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    #id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields = ['name', 'email', 'address'] # Ensure this is a string for all fields

# Create serializers
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    #id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields = "__all__"        