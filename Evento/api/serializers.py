from django.db.models import fields
from rest_framework import serializers
from Evento import models
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evento
        fields = '__all__'