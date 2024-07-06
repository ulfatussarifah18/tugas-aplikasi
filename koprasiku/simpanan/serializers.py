from rest_framework import serializers
from .models import Simpanan

class SimpananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simpanan
        fields = '__all__'
