from rest_framework import viewsets
from alunos.models import Curso
from alunos.serializer import CursoSeralizer


class CursoViewSet(viewsets.ModelViewSet):
    """Endpoint de cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSeralizer
