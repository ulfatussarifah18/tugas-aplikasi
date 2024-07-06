from .models import Simpanan
from .serializers import SimpananSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SimpananList(APIView):
    def get(self, request, format=None):
        simpanans = Simpanan.objects.all()
        serializer = SimpananSerializer(simpanans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SimpananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

