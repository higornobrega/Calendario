from django.db import models

class Evento(models.Model):
    tipo = models.CharField(max_length=250)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=250)
    importante = models.BooleanField()

    

    def __str__(self):
        return str(self.id)
