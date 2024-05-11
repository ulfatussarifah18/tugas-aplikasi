from .models import simpanan
from .serializers import simpananSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class simpananList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        simpanans = simpanan.objects.all()
        serializer = simpananSerializer(simpanans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = simpananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


