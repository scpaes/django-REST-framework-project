from alunos.serializer import ListaAlunosMatriculadosSerializer, ListaMatriculaAlunoSerializer
from alunos.models.matriculas import Matricula
from rest_framework import generics

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ListaMatriculasAluno(generics.ListAPIView):
    """ Endpoint de listagem de matriculas de um aluno """
    serializer_class = ListaMatriculaAlunoSerializer

    def get_queryset(self):
        matriculas = Matricula.objects.filter(aluno__id=self.kwargs['pk'])

        return matriculas

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Endpoint de listagem de alunos matriculados em determinado curso"""
    serializer_class = ListaAlunosMatriculadosSerializer

    def get_queryset(self):
        alunos = Matricula.objects.filter(curso__id=self.kwargs['pk'])
        return alunos

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
