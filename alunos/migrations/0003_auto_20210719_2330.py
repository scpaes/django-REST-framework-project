# Generated by Django 3.2.5 on 2021-07-20 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_cursos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alunos',
            new_name='Aluno',
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
    ]
