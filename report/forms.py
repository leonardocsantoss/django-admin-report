# -*- coding:utf-8 -*-
from models import ReportType
from django import forms


class ReportTypeForm(forms.ModelForm):

    class Meta:
        model = ReportType