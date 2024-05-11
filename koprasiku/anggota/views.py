from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Anggota
from .serializers import AnggotaSerializer


@api_view(['GET', 'POST'])
def Anggota_list(request):
    if request.method == 'GET':
        anggota = Anggota.objects.all()
        serializer = AnggotaSerializer(anggota, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnggotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)