# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Aluno
from report.actions import report_generic_detailed
from django.utils.translation import ugettext as _


class AdminAluno(admin.ModelAdmin):

  
    list_display = ("matricula", "nome", "sexo", "data_nascimento", "acoes", )
    list_filter = ("sexo", "data_nascimento", )
    save_on_top = True

    list_report = ('matricula', 'nome', 'sexo', 'cor_raca', 'data_nascimento', 'rg', 'cpf', )
    fieldsets_report = [
        (_(u'Aluno'),             {'fields' : ( 'nome', 'sexo', 'cor_raca', 'data_nascimento', ), }, ),
        (_(u'Documentos'),             {'fields' : ('rg', 'cpf', ), }, ),
    ]
    actions = [report_generic_detailed ]


admin.site.register(Aluno, AdminAluno)
