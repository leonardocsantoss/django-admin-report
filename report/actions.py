# -*- coding: utf-8 -*-
from html2report import html_report_generic
from django.http import HttpResponse
import ho.pisa as pisa
from django.utils.encoding import smart_str

def report_generic(self, request, queryset):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=RelatorioGeral-%s.pdf' % smart_str(queryset.model._meta.verbose_name.upper())

    html = html_report_generic(queryset.model._meta.verbose_name.upper() , self.list_report, queryset)
    pdf = pisa.CreatePDF(html, response)

    return response

report_generic.short_description = u"Gerar relatório geral"