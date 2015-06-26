from rest_framework import viewsets
from .serializers import participante_serializer, universidad_serializer
from app.models import participante, universidad

class participante_view_set(viewsets.ModelViewSet):
    queryset = participante.objects.all()
    serializer_class = participante_serializer

class universidad_view_set(viewsets.ModelViewSet):
    queryset = universidad.objects.all()
    serializer_class = universidad_serializer