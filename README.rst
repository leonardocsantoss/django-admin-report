===================
 Django Admin Report
===================

Django Admin Report is a small django application that allows for easy exporting of PDF reports through the admin interface.


Dependencies
===============

- Pisa(http://www.xhtml2pdf.com/)(Required)
- Django-admin-tools(https://bitbucket.org/izi/django-admin-tools/wiki/Home)(Recommended)


Installation
===============

- 1. Download the application
- 2. Add the package "report" to your path.
- 3. Add the app "report" into your settings.py

    INSTALLED_APPS = (
        ...
        'report',
    )

- 4. Add the urls of the app "report" into your urls.py

    (r'^report/', include('report.urls')),

- 5. Copy the folder "media/report" to your media folder

- 6. If you use the app "django-admin-tools, add the variable "ADMIN_TOOLS_MENU" into your settings.py

    ADMIN_TOOLS_MENU = 'report.menu.CustomMenu'


Usage General Report
===============

- 1. Also in admin.py, in your model's ModelAdmin specify a variable called "list_report" that should contain an iterable with the model attributes that should appear on the report, e.g.

    list_report = ('some_attribute', 'other_attribute', )

- 2. Now you simply create your types of repot, using the administration interface. When created, it automatically creates a menu in the admin-tools, where the reports will be generated.


Usage Detailed Report
===============
- 1. In your application's admin.py, import the following 'action' like so:

    from report.actions import report_generic_detailed

- 2. Also in admin.py, in your model's ModelAdmin specify a variable called "fieldsets_report" that should contain an iterable with the model attributes that should appear on the report, e.g.

    fieldsets_report = [

        (u'Description block 1',             {'fields' : ( 'some_attribute', 'other_attribute', ), }, ),
        
        (u'Description block 2',             {'fields' : ( 'some_attribute_new', 'other_attribute_new', ), }, ),
        
    ]

- 3. In admin.py, in your model's ModelAdmin specify a variable called  "report_header_detailed" for the Detailed Report, this variable is string, that contains the reader in HTML.

    report_header_detailed = "<h1>Test of header detailed</h1>"

- 4. Finally, make sure you also add the aforementioned 'action' to your ModelAdmin's list of actions, like so:

    actions = [report_generic_detailed, ]