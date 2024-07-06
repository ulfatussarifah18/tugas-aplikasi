from .models import Pinjaman
from .serializers import PinjamanSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PinjamanList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        pinjamans = Pinjaman.objects.all()
        serializer = PinjamanSerializer(pinjamans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PinjamanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


