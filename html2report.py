# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.encoding import smart_str

from datetime import date


def get_display(report, queryset):
    try:
        value = smart_str(queryset.model._meta.get_field(report).verbose_name)
    except:
        value = smart_str(report[0].upper()+report[1:])
    return value


def get_value(query, report):
    value = getattr(query, report)
    if value is None or value == "":
        value = " - "
    elif type(value) is date:
        value = value.strftime('%d/%m/%Y')
    elif type(value) is unicode and value != " - " and len(value) <= 3:
        try:
            func = getattr(query, "get_"+report+"_display")
            value = func()
        except:
            pass
    elif "instancemethod" in str(type(value)):
        func = getattr(query, report)
        value = func()
    return smart_str(value)

def html_report_generic(nome_relatorio, list_report, queryset):

    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            @page {
              size: a4 landscape;
              margin: 1cm;
            }
            .style0 {font-family: Arial, Helvetica, sans-serif; text-align: center; padding-top: 3px; padding-bottom: 3px; }
            .style1 {font-family: Arial, Helvetica, sans-serif; text-align: center; font-weight: bold; padding-top: 3px; padding-bottom: 3px; }
            .style2 {font-family: Arial, Helvetica, sans-serif; text-align: center; padding-top: 3px;}
            .style3 {font-family: Arial, Helvetica, sans-serif; text-align: center; padding-top: 3px; background: #f0f0f0;}
        </style>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>

            <td align="center"><span class="style1"><br />
                <strong>"""+smart_str(nome_relatorio)+""" - RELATÓRIO GERAL</strong><br />
              <br />
            </span></td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
              <tr>
                <td width="3%" class="style1 style3">Nº</td>"""
    for report in list_report:
        value = get_display(report, queryset)
        html += "<td width=\"%s%%\" class=\"style1 style3\">%s</td>" % (len(value)+7, value)

    html += "</tr>"

    for i,query in enumerate(queryset):
        html += "<tr>"
        if i%2==0: z=2
        else: z=3
        html += "<td class=\"style%s\">%s</td>" %(z, i+1)
        for report in list_report:
            value = get_value(query, report)
            html += "<td width=\"%s%%\" class=\"style%s\">%s</td>" % (len(value)+7, z, value)
        html += "</tr>"

    html += "</table>"
    return html