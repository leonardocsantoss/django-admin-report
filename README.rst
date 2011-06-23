===================
 Django Admin Report
===================

Django Admin Report is a small django application that allows for easy exporting of PDF reports through the admin interface.


Dependencies
===============

-Pisa(http://www.xhtml2pdf.com/)


Installation
===============

-Download the application
-Add the package "report" to your path.


Usage General Report
===============
- In your application's admin.py, import the following 'action' like so:

    from report.actions import report_generic

- Also in admin.py, in your model's ModelAdmin specify a variable called "list_report" that should contain an iterable with the model attributes that should appear on the report, e.g.

    list_report = ('some_attribute', 'other_attribute', )

- Finally, make sure you also add the aforementioned 'action' to your ModelAdmin's list of actions, like so:

    actions = [report_generic, ]


Usage Detailed Report
===============
- In your application's admin.py, import the following 'action' like so:

    from report.actions import report_generic_detailed

- Also in admin.py, in your model's ModelAdmin specify a variable called "fieldsets_report" that should contain an iterable with the model attributes that should appear on the report, e.g.

    fieldsets_report = [

        (u'Description block 1',             {'fields' : ( 'some_attribute', 'other_attribute', ), }, ),
        
        (u'Description block 2',             {'fields' : ( 'some_attribute_new', 'other_attribute_new', ), }, ),
        
    ]

- Finally, make sure you also add the aforementioned 'action' to your ModelAdmin's list of actions, like so:

    actions = [report_generic_detailed, ]


Edit the Header Report
===============

- In admin.py, in your model's ModelAdmin specify a variable called "report_header" for the General Report and specify a variable called "report_header_detailed" for the Detailed Report, these variables are strings, that contains the reader in HTML.

    report_header = "<h1>Test of header geral</h1>"
    
    report_header_detailed = "<h1>Test of header detailed</h1>"

- If not specify the variables "report_header" or "report_header_detailed", the report put the model name as a header.