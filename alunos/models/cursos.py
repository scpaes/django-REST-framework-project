from django.db import models


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('A', 'Avançado'),
        ('I', 'Intermediário'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(
        max_length=1, choices=NIVEL, blank=False, null=False)

    def __str__(self) -> str:
        return self.descricao
