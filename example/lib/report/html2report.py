# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from datetime import date, datetime
from django.conf import settings


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
        return value.replace("_", " ")


def get_value(query, report):
    if "__" in report:
        value = getattr(query, report.split("__")[0])
        return get_value(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        value = getattr(query, report)
        if value is None or value == "":
            value = " - "
        elif type(value) is date:
            value = value.strftime(settings.DATE_INPUT_FORMATS[0])
        elif type(value) is datetime:
            value = value.strftime(settings.DATETIME_INPUT_FORMATS[0])
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
            @page {size: a4 landscape; margin: 1cm; }
            body {font-family:Helvetica Narrow, sans-serif; font-size:12px; }
            .pad5 {padding: 5px 5px 0 5px;}
            .desc {font-weight: bolder; border-bottom: 2px #000 solid; background: #f4f4f4;}
            .style2 {color: #666; }
            .style3 {color: #666; background: #f4f4f4; }
            .head {padding-bottom: 10px;}
        </style>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td align="center" class="head">"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
              <tr>
                <td width="3%" class="desc pad5">Nº</td>"""
    for report in list_report:
        value = get_display(queryset, report)
        html += "<td width=\"%s%%\" class=\"desc pad5\">%s</td>" % (len(value)+7, value)

    html += "</tr>"

    for i,query in enumerate(queryset):
        html += "<tr>"
        if i%2==0: z=2
        else: z=3
        html += "<td class=\"pad5 style%s\">%s</td>" %(z, i+1)
        for report in list_report:
            value = get_value(query, report)
            html += "<td width=\"%s%%\" class=\"pad5 style%s\">%s</td>" % (len(value)+7, z, value)
        html += "</tr>"

    html += "</table>"
    return html



def html_report_generic_detailed(report_header, fieldsets_report, query):

    html = """
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            body { font-family:Helvetica Narrow, sans-serif; font-size:12px; }
            .desc {font-weight: bolder; border-bottom: 2px #000 solid; font-weight:bolder; padding: 10px 0 0 0;}
            .pad3 {padding: 3px; color: #666;}
            .bottom{ border-bottom: 2px #000 solid;}
            .head {padding-bottom: 10px;}
        </style>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td align="center" class="head">"""+smart_str(report_header)+"""</td>
          </tr>
        </table> """

    html += """
        <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">"""
    for fieldset in fieldsets_report:
        html += """
            <tr>
                <td colspan="2" class="desc">"""+smart_str(fieldset[0])+"""</td>
            </tr>
        """

        for key,field in enumerate(fieldset[1]['fields']):
            if key%2 == 0: html += "<tr>"
            html += """
                <td width="50%" class="pad3"><strong>"""+smart_str(get_display(query, field))+""": </strong>"""+smart_str(get_value(query, field))+"""</td>
            """
            if key%2 != 0: html += "</tr>"
        if len(fieldset[1]['fields'])%2 == 0:
            html += "</tr>"

    html += """<tr>
                    <td width="50%" class="bottom"></td>
                    <td width="50%" class="bottom"></td>
                </tr>
            </table>"""

    return html