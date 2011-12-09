# -*- coding: utf-8 -*-
from html2report import html_report_generic_detailed
from django.http import HttpResponse
from django.conf import settings
import ho.pisa as pisa
from cStringIO import StringIO
import zipfile
import os
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _
from unicodedata import normalize



def remove_sc(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')


def get_header_detailed(self, queryset):
    try:
        return self.report_header_detailed
    except:
        return queryset.model._meta.verbose_name.upper()


def report_generic_detailed(self, request, queryset):
    if len(queryset) == 1:
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % (smart_str(queryset.model._meta.verbose_name.upper()))
        html = html_report_generic_detailed(get_header_detailed(self, queryset), self.fieldsets_report, queryset[0])
        pdf = pisa.CreatePDF(html, response)
        return response
    else:
        response = HttpResponse(mimetype='application/zip')
        response['Content-Disposition'] = 'filename='+_('Relatorio')+'.zip'
        buffer = StringIO()
        zip = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED)

        local = settings.MEDIA_ROOT
        for key,query in enumerate(queryset):
            nome =  "%s-%s.pdf" % (remove_sc(smart_str(queryset.model._meta.verbose_name.upper())), key)

            html = html_report_generic_detailed(get_header_detailed(self, queryset), self.fieldsets_report, query)
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

report_generic_detailed.short_description = _(u"Imprimir relatório detalhado")