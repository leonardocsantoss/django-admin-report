# -*- coding:utf-8 -*-
from models import ReportType
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from forms import ReportTypeForm
from django import forms
from django.utils.encoding import smart_str
import string

def capitalize(string):
    return string[0].upper()+string[1:]

def get_display(model, report):
    if "__" in report:
        value = getattr(model, report.split("__")[0])
        return get_display(value, report.replace(report.split("__")[0]+"__", ""))
    else:
        try:value = smart_str(capitalize(model._meta.get_field(report).verbose_name))
        except:value = smart_str(capitalize(report))
        return value.replace("_", " ")
    
def get_key(key):
    if key < 10:
        return key
    else:
        return string.ascii_lowercase[key-10]

def create_form(object_id=None):
    if object_id is None:
        return ReportTypeForm
    else:
        obj = ReportType.objects.get(id=object_id)
        choices = [[get_key(key), get_display(obj.modelo.model_class(), campo)] for key, campo in enumerate(admin.site._registry[obj.modelo.model_class()].list_report)]
        campos_dinamicos = {'campos': forms.MultipleChoiceField(required=True, choices=choices, label=_(u"Campos"), help_text=_(u"Selecione os campos desse tipo de relatório."), widget=forms.CheckboxSelectMultiple()), }
        NewReportTypeForm = type('', (ReportTypeForm,), campos_dinamicos)
        return NewReportTypeForm

class AdminReportType(admin.ModelAdmin):

    list_display = ("titulo", "modelo", )
    search_fields = ("titulo", "cabecalho", )
    filter_horizontal = ('permissao', )
    save_on_top = False

    fieldsets = [
        (_(u"Tipo de relatório"),             { "fields" : ("titulo", "cabecalho", ), }, ),
        (_(u"Permissão"),             { "fields" : ("permissao", ), }, ),
        (_(u"Modelo"),             { "fields" : ( "modelo", ), }, ),
    ]
    
    change_form_template = 'report/change_form.html'
    
    class Media:
        js = ('report/js/tiny_mce/tiny_mce.js',
              'report/js/tiny_mce/tiny_mce_settings.js',)
              
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "modelo":
            registry = []
            for model, adm in admin.site._registry.iteritems():
                try:
                    if adm.list_report is not None:
                        registry.append(model._meta.module_name)
                except:pass
            models = ContentType.objects.filter(model__in=registry)
            kwargs["queryset"] = models
        return super(AdminReportType, self).formfield_for_foreignkey(db_field, request, **kwargs)


    def add_view(self, request, form_url="", extra_context=None):
        self.save_on_top = False
        self.readonly_fields = ()
        self.form = create_form()
        self.fieldsets = [
            (_(u"Tipo de relatório"),             { "fields" : ("titulo", "cabecalho", ), }, ),
            (_(u"Permissão"),             { "fields" : ("permissao", ), }, ),
            (_(u"Modelo"),             { "fields" : ( "modelo", ), }, ),
        ]
        return super(AdminReportType, self).add_view(request, form_url, extra_context)
    
    
    def change_view(self, request, object_id, extra_context=None):
        self.form = create_form(object_id)
        self.save_on_top = True
        self.readonly_fields = ("modelo", )
        self.fieldsets = [
            (_(u"Tipo de relatório"),             { "fields" : ("titulo", "cabecalho", ), }, ),
            (_(u"Permissão"),             { "fields" : ("permissao", ), }, ),
            (_(u"Modelo"),             { "fields" : ( "modelo", ), }, ),
            (_(u"Campos"),             { "fields" : ( "campos", ), }, ),
        ]
        return super(AdminReportType, self).change_view(request, object_id, extra_context)
  
admin.site.register(ReportType, AdminReportType)