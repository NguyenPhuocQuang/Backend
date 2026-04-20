
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.departments_serializer import DepartmentsSerializer
from apps.apis.models.department import Departments

class DepartmentsListCreate(APIView):
    def get(self, request):
        data = Departments.objects.all()
        serializer = DepartmentsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentsDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Departments, pk=pk)
        serializer = DepartmentsSerializer(obj)
        return Response(serializer.data)