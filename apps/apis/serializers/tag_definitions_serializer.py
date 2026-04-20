

from rest_framework import serializers
from apps.apis.models.tag_definition import TagDefinitions


class TagDefinitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDefinitions
        fields = "__all__"
