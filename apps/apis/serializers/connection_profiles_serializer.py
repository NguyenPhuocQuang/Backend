from rest_framework import serializers
from apps.apis.models.connection_profile import ConnectionProfiles


class ConnectionProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionProfiles
        fields = "__all__"
