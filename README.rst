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


Usage
===============
- In your application's admin.py, import the following 'action' like so:

    from report.actions import report_generic

- Also in admin.py, in your model's ModelAdmin specify a variable called "list_report" that should contain an iterable with the model attributes that should appear on the report, e.g.

    list_report = ('some_attribute', 'other_attribute', )

- Finally, make sure you also add the aforementioned 'action' to your ModelAdmin's list of actions, like so:

    actions = [report_generic, ]