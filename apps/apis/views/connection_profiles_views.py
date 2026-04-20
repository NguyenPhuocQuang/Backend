

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.connection_profiles_serializer import ConnectionProfilesSerializer
from apps.apis.models.connection_profile import ConnectionProfiles

class ConnectionProfilesListCreateAPIView(APIView):
    def get(self, request):
        data = ConnectionProfiles.objects.all()
        serializer = ConnectionProfilesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConnectionProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionProfilesDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(ConnectionProfiles, pk=pk)
        serializer = ConnectionProfilesSerializer(obj)
        return Response(serializer.data)