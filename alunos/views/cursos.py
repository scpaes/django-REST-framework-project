from rest_framework import viewsets
from alunos.models import Curso
from alunos.serializer import CursoSeralizer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CursoViewSet(viewsets.ModelViewSet):
    """Endpoint de cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSeralizer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
