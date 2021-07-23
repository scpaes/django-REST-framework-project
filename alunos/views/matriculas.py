from alunos.serializer import MatriculaSerializer
from rest_framework import viewsets
from alunos.models import Matricula

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class MatriculaViewSet(viewsets.ModelViewSet):
    """Endpoint de matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
