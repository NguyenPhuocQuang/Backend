

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.machines_serializer import MachinesSerializer
from apps.apis.models.machine import   Machines 


class MachinesListCreate(APIView):
    def get(self, request):
        data = Machines.objects.all()
        serializer = MachinesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MachinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachinesDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Machines, pk=pk)
        serializer = MachinesSerializer(obj)
        return Response(serializer.data)