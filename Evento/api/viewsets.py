from rest_framework import viewsets
from rest_framework.response import Response
from Evento import models
#from models import Evento
from Evento.api import serializers

class EventoViewsets(viewsets.ModelViewSet):
    '''
        Esse objeto representa uma data importante para o calendário acadêmico da UNIFIP 


    -
    '''
    serializer_class = serializers.EventoSerializer
    queryset = models.Evento.objects.all()

    # def get_queryset(self):

    #     return self.get_serializer().Meta.model.objects.filter(state = True)
    
    # def list(self,request):
    #     '''
    #     Esse objeto representa uma data importante para o calendário acadêmico da UNIFIP 


    #     tipo - Representa o tipo da data podendo ser Feriados Nacionais e Estaduais, Feriados Municipais, Datas Comemorativas, Datas da Instituinção.
    #     data_inicio - Representa a data que inicia o evento.
    #     data_fim - Representa a data que finaliza o evento podendo ser nula caso termine no mesmo dia.
    #     descricao - Representa uma descrição ou nome do evento
    #     importante - Informa se o evento é será marcado no calendário.
    #     '''
    #     data = self.get_queryset()
    #     data = self.get_serializer(data, many=True)
    #     return Response(data.data)