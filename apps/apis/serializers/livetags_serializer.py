from rest_framework import serializers
from apps.apis.models.live_tag import LiveTags


class LiveTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveTags
        fields = "__all__"
