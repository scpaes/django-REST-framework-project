from alunos.serializer import MatriculaSerializer
from rest_framework import viewsets
from alunos.models import Matricula


class MatriculaViewSet(viewsets.ModelViewSet):
    """Endpoint de matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer