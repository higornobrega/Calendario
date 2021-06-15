from django.db import models

class Evento(models.Model):
    SHIRT_SIZES = (
        ('Feriados Nacionais e Estaduais', 'Feriados Nacionais e Estaduais'),
        ('Feriados Municipais', 'Feriados Municipais'),
        ('Datas Comemorativas', 'Datas Comemorativas'),
        ('Datas da Instituinção', 'Datas da Instituinção'),
    )
    tipo = models.CharField(max_length=250, choices=SHIRT_SIZES)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=250)
    importante = models.BooleanField()

    

    def __str__(self):
        return str(self.id)
