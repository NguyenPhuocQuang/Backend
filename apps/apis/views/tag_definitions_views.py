from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.apis.models.tag_definition import TagDefinitions
from apps.apis.serializers.tag_definitions_serializer import TagDefinitionsSerializer

TAG_DEFINITIONS_LIST_CACHE_KEY = "tag_definitions:list"
TAG_DEFINITIONS_DETAIL_CACHE_KEY = "tag_definitions:detail:{pk}"
TAG_DEFINITIONS_CACHE_TIMEOUT = 900


class TagDefinitionsListCreate(APIView):
    def get(self, request):
        cached_data = cache.get(TAG_DEFINITIONS_LIST_CACHE_KEY)
        if cached_data is not None:
            return Response(cached_data)

        data = TagDefinitions.objects.all()
        serializer = TagDefinitionsSerializer(data, many=True)
        cache.set(TAG_DEFINITIONS_LIST_CACHE_KEY, serializer.data, TAG_DEFINITIONS_CACHE_TIMEOUT)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagDefinitionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(TAG_DEFINITIONS_LIST_CACHE_KEY)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDefinitionsDetail(APIView):
    def get(self, request, pk):
        cache_key = TAG_DEFINITIONS_DETAIL_CACHE_KEY.format(pk=pk)
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        obj = get_object_or_404(TagDefinitions, pk=pk)
        serializer = TagDefinitionsSerializer(obj)
        cache.set(cache_key, serializer.data, TAG_DEFINITIONS_CACHE_TIMEOUT)
        return Response(serializer.data)
