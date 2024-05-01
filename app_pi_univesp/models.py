# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Polos(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)
    polos = models.TextField(blank=True, null=True)
    contato = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    num_vagas_eixo = models.TextField(blank=True, null=True)
    total_vagas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polos'

class Cursos(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)
    período = models.TextField(db_column='Período', blank=True, null=True)  # Field name made lowercase.
    polo = models.TextField(db_column='Polo', blank=True, null=True)  # Field name made lowercase.
    curso = models.TextField(db_column='Curso', blank=True, null=True)  # Field name made lowercase.
    eixo = models.TextField(db_column='Eixo', blank=True, null=True)  # Field name made lowercase.
    disciplina = models.TextField(db_column='Disciplina', blank=True, null=True)  # Field name made lowercase.
    turma = models.TextField(db_column='Turma', blank=True, null=True)  # Field name made lowercase.
    código_disciplina = models.TextField(db_column='Código Disciplina', blank=True, null=True)  # Field name made lowercase. Field renam
    código_prof_respons_field = models.TextField(db_column='Código Prof. Respons.', blank=True, null=True)  # Field name made lowercase.
    código_prof_videoaula = models.TextField(db_column='Código Prof. Videoaula', blank=True, null=True)  # Field name made lowercase. Fi

    class Meta:
        managed = False
        db_table = 'cursos'

