# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse


class ReportType(models.Model):

        class Meta:
            verbose_name = _(u'Tipo de relatório')
            verbose_name_plural = _(u'Tipos de relatórios')

        titulo = models.CharField(max_length=150, verbose_name=_(u'Título'), help_text=_(u'Insira o título do tipo de relatório.'))
        cabecalho = models.TextField(verbose_name=_(u'Cabeçalho'), help_text=_(u'Insira o cabeçalho do tipo de relatório.'))
        permissao = models.ManyToManyField(Group, blank=True, verbose_name=_(u'Permissão'), help_text=_(u'Selecione os grupos que tem permissão para imprimir esse tipo de relatório.'))
        modelo = models.ForeignKey(ContentType, verbose_name=_(u'Modelo'), help_text=_(u'Selecione o modelo do tipo de relatório.'))
        campos = models.CharField(max_length=255, blank=True, null=True, verbose_name=_(u'Campos'), help_text=_(u'Selecione os campos do tipo de relatório.'))
        
        def __unicode__(self):
            return u"%s" % self.titulo
        
        def get_absolute_url(self):
            return reverse('report.views.report',kwargs={'report_id': self.id})