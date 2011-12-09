# -*- coding: utf-8 -*-
"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'Cofivi.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from models import ReportType
from admin_tools.menu import items, Menu
from django.db.models import Q


class CustomMenu(Menu):

    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(_('Favoritos')),
            items.AppList(
                _('Applications'),
                exclude=('django.contrib.*',)
            ),
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            ),
        ]


    def init_with_context(self, context):


        request = context['request']

        list_children = []
        if request.user.is_superuser:
            reports = ReportType.objects.all()
        else:
            reports = ReportType.objects.filter(Q(permissao__contains=request.user.groups.all()) | Q(permissao__isnull=True))
        for report in reports:
            list_children.append(items.MenuItem(report.titulo, report.get_absolute_url()))
        self.children += [items.MenuItem(_(u'Relatórios'), children=list_children )]

        return super(CustomMenu, self).init_with_context(context)


