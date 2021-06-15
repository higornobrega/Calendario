from django.contrib import admin

from .models import Evento
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display=('tipo', 'data_inicio', 'data_fim', 'descricao', 'importante')
