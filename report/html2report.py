# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from datetime import date, datetime


def capitalize(string):
    return string[0].upper()+string[1:]

def many_to_many_display(list):
    display = ""
    for i, item in enumerate(list):
        display += smart_str(item)
        if i != len(list)-1: display += ", "
    return display

def get_display(queryset, report):
    try:
        model = queryset.model
    except:
        model = queryset
    if "__" in report:
        value = getattr(model, report.split("__")[0])
        return get_display(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        try:
            value = smart_str(capitalize(model._meta.get_field(report).verbose_name))
        except:
           value = smart_str(capitalize(report))
        return value


def get_value(query, report):
    if "__" in report:
        value = getattr(query, report.split("__")[0])
        return get_value(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        value = getattr(query, report)
        if value is None or value == "":
            value = " - "
        elif type(value) is date:
            value = value.strftime('%d/%m/%Y')
        elif type(value) is datetime:
            value = value.strftime('%d/%m/%Y %H:%M')
        elif type(value) is bool:
            if value:
                value = "Sim"
            else:
                value = "Não"
        elif type(value) is unicode and value != " - " and len(value) <= 3:
            try:
                func = getattr(query, "get_"+report+"_display")
                value = func()
            except:
                pass
        elif "instancemethod" in str(type(value)):
            func = getattr(query, report)
            value = func()
        elif "django.db.models.fields.related.ManyRelatedManager" in str(type(value)):
            value = many_to_many_display(value.all())
        return smart_str(value)


def html_report_generic(report_header, list_report, queryset):

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
            <td align="center">"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
              <tr>
                <td width="3%" class="style1 style3">Nº</td>"""
    for report in list_report:
        value = get_display(queryset, report)
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



def html_report_generic_detailed(report_header, fieldsets_report, query):

    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            .style1 {font-family: Arial, Helvetica, sans-serif; padding-top: 2px;}
            .style4 {font-family: Arial, Helvetica, sans-serif; font-weight: bold; border-bottom: 1px #000 solid; padding-top: 10px;}
        </style>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td align="center">"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">"""
    for fieldset in fieldsets_report:
        html += """
            <tr>
                <td colspan="2" class="style4">"""+smart_str(fieldset[0])+"""</td>
            </tr>
        """
        anterior = False
        for key,field in enumerate(fieldset[1]['fields']):
            if key%2 == 0: anterior = field
            else:
                html += """
                <tr>
                    <td width="50%" class="style1"><strong>"""+smart_str(get_display(query, anterior))+""": </strong>"""+smart_str(get_value(query, anterior))+"""</td>
                    <td width="50%" class="style1"><strong>"""+smart_str(get_display(query, field))+""": </strong>"""+smart_str(get_value(query, field))+"""</td>
                </tr>"""

    html += "</table>"

    return html