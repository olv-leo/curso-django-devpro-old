from django.db import models
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=62)
    publico = models.TextField()
    descricao = models.TextField()
