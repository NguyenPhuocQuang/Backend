
from rest_framework import serializers
from apps.apis.models.department import Departments



class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"