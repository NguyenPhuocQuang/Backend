

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.livetags_serializer import LiveTagsSerializer
from apps.apis.models.live_tag import LiveTags




class LiveTagsListCreateAPIView(APIView):
    def get(self, request):
        data = LiveTags.objects.all()
        serializer = LiveTagsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LiveTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiveTagsDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(LiveTags, pk=pk)
        serializer = LiveTagsSerializer(obj)
        return Response(serializer.data)