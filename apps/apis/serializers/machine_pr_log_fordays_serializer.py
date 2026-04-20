
from rest_framework import serializers
from apps.apis.models.machine_pr_Log_for_day import MachineProductionLogForDays
class MachineProductionLogForDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineProductionLogForDays
        fields = "__all__"
