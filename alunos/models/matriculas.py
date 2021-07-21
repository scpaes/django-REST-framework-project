from django.db import models
from .alunos import Aluno
from .cursos import Curso


class Matricula(models.Model):
    TURNO = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length=1, choices=TURNO, blank=False, null=False, default='M')
