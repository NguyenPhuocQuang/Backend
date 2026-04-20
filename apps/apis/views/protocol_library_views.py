

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.protocol_librarys_serializer  import ProtocolLibrarysSerializer
from apps.apis.models.protocol_library import ProtocolLibrarys


class ProtocolLibrarysListCreateAPIView(APIView):
    def get(self, request):
        data = ProtocolLibrarys.objects.all()
        serializer = ProtocolLibrarysSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProtocolLibrarysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtocolLibrarysDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(ProtocolLibrarys, pk=pk)
        serializer = ProtocolLibrarysSerializer(obj)
        return Response(serializer.data)