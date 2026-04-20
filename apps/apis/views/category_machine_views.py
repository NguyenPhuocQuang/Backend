from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.category_machines_serializer import CategoryMachinesSerializer
from apps.apis.models.category_machine import CategoryMachines


class CategoryMachinesListCreate(APIView):
    def get(self, request):
        data = CategoryMachines.objects.all()
        serializer = CategoryMachinesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryMachinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryMachinesDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(CategoryMachines, pk=pk)
        serializer = CategoryMachinesSerializer(obj)
        return Response(serializer.data)