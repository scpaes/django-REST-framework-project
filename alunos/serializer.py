from alunos.models.matriculas import Matricula
from django.db.models import fields
from rest_framework import serializers
from .models import Aluno, Curso
from alunos import models


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'turno']

    def get_turno(self, obj):
        return obj.get_turno_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno']
