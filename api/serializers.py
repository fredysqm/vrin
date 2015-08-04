from rest_framework import serializers
from app.models import participante, universidad


class participante_serializer(serializers.ModelSerializer):
    class Meta:
        model = participante
        #fields = ('dni', 'paterno','materno','nombre','universidad')

class universidad_serializer(serializers.ModelSerializer):
    class Meta:
        model = universidad
        #fields = ('dni', 'paterno','materno','nombre','universidad')