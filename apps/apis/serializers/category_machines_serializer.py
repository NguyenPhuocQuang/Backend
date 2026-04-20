from rest_framework import serializers
from apps.apis.models.category_machine import CategoryMachines

class CategoryMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMachines
        fields = "__all__"
