from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.tag_definitions_serializer  import TagDefinitionsSerializer
from apps.apis.models.tag_definition import TagDefinitions




class TagDefinitionsListCreate(APIView):
    def get(self, request):
        data = TagDefinitions.objects.all()
        serializer = TagDefinitionsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagDefinitionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDefinitionsDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(TagDefinitions, pk=pk)
        serializer = TagDefinitionsSerializer(obj)
        return Response(serializer.data)