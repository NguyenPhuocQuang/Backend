
from rest_framework import serializers

from apps.apis.models.protocol_library import ProtocolLibrarys

class ProtocolLibrarysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocolLibrarys
        fields = "__all__"
