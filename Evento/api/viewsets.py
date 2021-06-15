from rest_framework import viewsets
from Evento import models
from Evento.api import serializers

class EventoViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.EventoSerializer
    queryset = models.Evento.objects.all()
