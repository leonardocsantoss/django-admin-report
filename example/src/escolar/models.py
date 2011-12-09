# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

TIPO_SEXO = (
    ("M", _(u"Masculino")),
    ("F", _(u"Feminino")),

)

COR_RACA = (
    ("B", _(u"Branca")),
    ("P", _(u"Preta")),
    ("A", _(u"Amarela")),
    ("D", _(u"Parda")),
    ("I", _(u"Indígena")),
)


class Aluno(models.Model):
    """
        Modelo onde contém os dados do Aluno
    """
    matricula = models.AutoField(primary_key=True, unique=True, verbose_name=_(u"Matrícula"), help_text=_(u"Digite a matrícula do aluno."))
    nome = models.CharField(max_length=255, verbose_name=_(u"Nome do aluno"), help_text=_(u"Digite o nome do aluno."))
    sexo = models.CharField(max_length=1, choices=TIPO_SEXO, verbose_name=_(u"Sexo"), help_text=_(u"Selecione o sexo do aluno."))
    data_nascimento = models.DateField(verbose_name=_(u"Data de nascimento"), help_text=_(u"Data de nascimento do aluno."))
    cor_raca = models.CharField(max_length=1, choices=COR_RACA, verbose_name=_(u"Cor/raça"), help_text=_(u"Selecione a cor/raça do aluno."))
    rg = models.PositiveIntegerField(null=True, blank=True, verbose_name=_(u"RG"), help_text=_(u"Informe o RG do aluno"))
    cpf = models.CharField(null=True, blank=True, max_length=14, verbose_name=_(u"CPF"), help_text=_(u"Informe o CPF do aluno."))
    
    class Meta:
         ordering = ("matricula",)
         verbose_name = _(u"Aluno")
         verbose_name_plural = _(u"Alunos")

    def acoes(self):
        a1 = u"<a style=\"padding-left: 7px;\" href=\"%s\">%s</a>" % (self.pk, _(u"Editar"))
        a2 = u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'report_generic_detailed'); $('#changelist-form').submit(); })(jQuery);\" >%s</a>" % (self.pk, _(u"Imprimir"))
        return a1+a2
    acoes.allow_tags = True
    acoes.short_description = _(u"Ações")

