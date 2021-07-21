from django.contrib import admin
from alunos.models import *


class AlunosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'rg',
        'cpf',
        'data_nascimento'
    )
    list_display_links = (
        'id',
        'nome'
    )
    search_fields = (
        'nome',
    )
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'descricao',
        'codigo_curso',
        'nivel'
    )
    list_display_links = (
        'id',
        'descricao'
    )
    search_fields = ('descricao', 'codigo_curso')


class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aluno',
        'curso',
        'turno',
    )
    list_display_links = (
        'id',
        'aluno'
    )


admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
