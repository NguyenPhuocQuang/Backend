
from  rest_framework import serializers
from apps.apis.models.machine_log_for_day import MachineLogForDays


class MachineLogForDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLogForDays
        fields = "__all__"
