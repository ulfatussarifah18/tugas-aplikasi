from .models import Investasi
from .serializers import InvestasiSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InvestasiList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        investasi = Investasi.objects.all()
        serializer = InvestasiSerializer(investasi, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvestasiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
