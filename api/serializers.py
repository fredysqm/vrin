from rest_framework import serializers
from app.models import participante, universidad


class participante_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = participante
        fields = ('dni', 'paterno','materno','nombre','universidad')

class universidad_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = universidad
        #fields = ('dni', 'paterno','materno','nombre','universidad')