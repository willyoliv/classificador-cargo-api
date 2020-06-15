from rest_framework import serializers
from .models import Historico

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ["id", "historico", "timestamp"]