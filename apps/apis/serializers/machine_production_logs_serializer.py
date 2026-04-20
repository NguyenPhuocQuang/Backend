
from rest_framework import serializers
from apps.apis.models.machine_production_log import MachineProductionLogs



class MachineProductionLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineProductionLogs
        fields = "__all__"
