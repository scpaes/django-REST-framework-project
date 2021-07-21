from rest_framework import viewsets
from alunos.serializer import AlunoSerializer
from alunos.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
    """Endpoint de alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
