# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import admin
from django.utils.encoding import smart_str
import ho.pisa as pisa
from html2report import html_report_generic

from models import ReportType
from django import forms
from django.db import models
from django.utils.translation import ugettext as _
import string

from datetime import datetime


def get_field(modelo, campo):
    return modelo._meta.get_field(campo)

def get_value(obj, campo):
    return getattr(obj, campo)

def get_key(key):
    try:
        return int(key)
    except:
        return string.ascii_lowercase.index(key)+10

@login_required
def report(request, report_id, template_name="report/report.html"):
    if request.user.is_staff:
        rtype = get_object_or_404(ReportType, id=report_id)
        if not request.user.is_superuser:
            if rtype.permissao.count() and not len([val for val in  rtype.permissao.all() if val in request.user.groups.all()]):
                raise Http404
        rtadmin = admin.site._registry[rtype.modelo.model_class()]

        campos_dinamicos = {}
        for filtro in rtadmin.list_filter:

            field = get_field(rtype.modelo.model_class(), filtro)
            if type(field) == models.BooleanField:
                choices = (('1', _(u'Sim')), ('0', _(u'Não')), ('', _(u'Todos')))
                campos_dinamicos[filtro] = forms.ChoiceField(required=False, choices=choices, label=_(field.verbose_name), widget=forms.RadioSelect())

            elif type(field) == models.CharField:
                if field.choices:
                    choices = field.choices
                    campos_dinamicos[filtro] = forms.MultipleChoiceField(required=False, choices=choices, label=_(field.verbose_name), widget=forms.CheckboxSelectMultiple())
                else:
                    choices = set()
                    for obj in rtype.modelo.model_class().objects.all():
                        choices.add((get_value(obj, filtro), get_value(obj, filtro)))
                    choices = list(choices)
                    campos_dinamicos[filtro] = forms.MultipleChoiceField(required=False, choices=choices, label=_(field.verbose_name), widget=forms.SelectMultiple())

            elif type(field) == models.DateField or type(field) == models.DateTimeField:
                choices = (('q', _(u'Qualquer data')), ('h', _(u'Hoje')), ('m', _(u'Este mês')), ('a', _(u'Este ano')))
                campos_dinamicos[filtro] = forms.ChoiceField(required=False, choices=choices, initial='q', label=_(field.verbose_name), widget=forms.RadioSelect())

            elif type(field) == models.ForeignKey or type(field) == models.OneToOneField:
                queryset = rtype.modelo.model_class()._meta.get_field(filtro).rel.to.objects.all()
                campos_dinamicos[filtro] = forms.ModelMultipleChoiceField(required=False, queryset=queryset, label=_(field.verbose_name), widget=forms.SelectMultiple())
            else:
                choices = set()
                for obj in rtype.modelo.model_class().objects.all():
                    choices.add((get_value(obj, filtro), get_value(obj, filtro)))
                choices = list(choices)
                campos_dinamicos[filtro] = forms.MultipleChoiceField(required=False, choices=choices, label=_(field.verbose_name), widget=forms.SelectMultiple())

        FilterForm = type('', (forms.Form,), campos_dinamicos)

        if request.method == "POST":

            response = HttpResponse(mimetype='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % smart_str(rtype.titulo).replace(" ", "_")
            queryset = rtype.modelo.model_class().objects.all()

            for field_name in rtadmin.list_filter:
                field = get_field(rtype.modelo.model_class(), field_name)

                sql = {}
                if type(field) == models.DateField or type(field) == models.DateTimeField:
                    try:
                        value = request.POST[field_name]
                        if value == 'q': pass
                        elif value == 'h': sql["%s__day" % field_name] = datetime.now().day
                        elif value == 'm': sql["%s__month" % field_name] = datetime.now().month
                        elif value == 'a': sql["%s__year" % field_name] = datetime.now().year
                    except: pass
                elif type(field) == models.BooleanField:
                    try:
                        value = request.POST[field_name]
                        sql["%s" % field_name] = value
                    except: pass
                else:
                    try:
                        value = request.POST.getlist(field_name)
                        if len(value) == 0: continue
                        sql["%s__in" % field_name] = value
                    except: pass

                query = models.Q(**sql)
                queryset = queryset.filter(query)

            campos = rtype.campos.replace('[', '').replace(']', '').replace('u\'', '').replace('\'', '').replace(',', '').split(' ')
            list_report = []
            for c in campos:
               list_report.append(rtadmin.list_report[get_key(c)])

            html = html_report_generic(smart_str(rtype.cabecalho), list_report, queryset)
            pdf = pisa.CreatePDF(html, response)
            return response
        else:
            form = FilterForm()
            return render_to_response(template_name, {
                'form': form,
                'title': rtype.titulo,
                'rtype': rtype,
                'rtadmin' : rtadmin,
            }, context_instance=RequestContext(request))
    else:
        raise PermissionDenied