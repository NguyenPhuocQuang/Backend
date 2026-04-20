from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.apis.serializers.metricvalues_serializer  import MetricValuesSerializer
from apps.apis.models.metric_value import MetricValues




class MetricValuesListCreateAPIView(APIView):
    def get(self, request):
        data = MetricValues.objects.all()
        serializer = MetricValuesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MetricValuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetricValuesDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(MetricValues, pk=pk)
        serializer = MetricValuesSerializer(obj)
        return Response(serializer.data)