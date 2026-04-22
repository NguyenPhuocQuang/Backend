from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.apis.models.machine import Machines
from apps.apis.serializers.machines_serializer import MachinesSerializer

MACHINES_LIST_CACHE_KEY = "machines:list"
MACHINES_DETAIL_CACHE_KEY = "machines:detail:{pk}"
MACHINES_CACHE_TIMEOUT = 300


class MachinesListCreate(APIView):
    def get(self, request):
        cached_data = cache.get(MACHINES_LIST_CACHE_KEY)
        if cached_data is not None:
            return Response(cached_data)

        data = Machines.objects.all()
        serializer = MachinesSerializer(data, many=True)
        cache.set(MACHINES_LIST_CACHE_KEY, serializer.data, MACHINES_CACHE_TIMEOUT)
        return Response(serializer.data)

    def post(self, request):
        serializer = MachinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(MACHINES_LIST_CACHE_KEY)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachinesDetail(APIView):
    def get(self, request, pk):
        cache_key = MACHINES_DETAIL_CACHE_KEY.format(pk=pk)
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        obj = get_object_or_404(Machines, pk=pk)
        serializer = MachinesSerializer(obj)
        cache.set(cache_key, serializer.data, MACHINES_CACHE_TIMEOUT)
        return Response(serializer.data)
