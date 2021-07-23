from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from alunos.serializer import AlunoSerializer
from alunos.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
    """Endpoint de alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
