from alunos.views.listview import ListaAlunosMatriculados, ListaMatriculasAluno
from django.contrib import admin
from django.urls import path, include

from alunos.views import AlunoViewSet, CursoViewSet, MatriculaViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='alunos')
router.register('cursos', CursoViewSet, basename='cursos')
router.register('matriculas', MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view(), name='lista-matricula-aluno'),
    path('curso/<int:pk>/alunos/', ListaAlunosMatriculados.as_view(), name='lista-alunos-matriculados'),
]
