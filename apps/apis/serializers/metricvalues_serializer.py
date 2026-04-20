
from rest_framework import serializers
from apps.apis.models.metric_value import MetricValues

class MetricValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricValues
        fields = "__all__"
