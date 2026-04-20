
from rest_framework import serializers
from  apps.apis.models.machine import Machines

class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = "__all__"
