from .models import pinjaman
from .serializers import pinjamanSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class pinjamanList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        pinjamans = pinjaman.objects.all()
        serializer = pinjamanSerializer(pinjamans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = pinjamanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


