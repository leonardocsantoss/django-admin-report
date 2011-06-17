# -*- coding: utf-8 -*-
from html2report import html_report_generic, html_report_generic_detailed
from django.http import HttpResponse
from django.conf import settings
import ho.pisa as pisa
from cStringIO import StringIO
import zipfile
import os
from django.utils.encoding import smart_str


def report_generic(self, request, queryset):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=RelatorioGeral-%s.pdf' % smart_str(queryset.model._meta.verbose_name.upper())

    html = html_report_generic(queryset.model._meta.verbose_name.upper() , self.list_report, queryset)
    pdf = pisa.CreatePDF(html, response)

    return response

report_generic.short_description = u"Gerar relatório geral"


def report_generic_detailed(self, request, queryset):
    if len(queryset) == 1:
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=RelatorioDetalhado-%s.pdf' % (smart_str(queryset.model._meta.verbose_name.upper()))
        html = html_report_generic_detailed(queryset.model._meta.verbose_name.upper() , self.fieldsets_report, queryset[0])
        pdf = pisa.CreatePDF(html, response)
        return response
    else:
        response = HttpResponse(mimetype='application/zip')
        response['Content-Disposition'] = 'filename=RelatorioDetalhado.zip'
        buffer = StringIO()
        zip = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED)

        local = settings.MEDIA_ROOT
        for key,query in enumerate(queryset):
            nome =  "RelatorioDetalhado-%s-%s.pdf" % smart_str(queryset.model._meta.verbose_name.upper(), key)

            html = html_report_generic_detailed(queryset.model._meta.verbose_name.upper(), self.fieldsets_report, query)
            arquivo = file(local+nome, 'w')
            pdf = pisa.CreatePDF(html, arquivo)
            arquivo.close()
            zip.write(local+nome, nome)
            os.remove(local+nome)
        zip.close()
        buffer.flush()
        ret_zip = buffer.getvalue()
        buffer.close()
        response.write(ret_zip)
        return response

report_generic_detailed.short_description = u"Gerar relatório detalhado"