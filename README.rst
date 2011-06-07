===================
 Django Admin Report
===================

Django Admin Report é uma pequena aplicação Django, que permite de forma simples a exportação em pdf de relatórios usando a interface de administração do django.


Dependências
===============

-Pisa(__http://www.xhtml2pdf.com/)


Instalação
===============

1. Baixe a aplicação
2. Coloque-a no path do seu projeto


Como usar
===============
-No arquivo admin.py da sua aplicação importe a action:

 $from report.actions import report_generic

-Na classe de administração do model, ainda no arquivo admin.py adicione uma variável chamada "list_report" contendo uma lista com os nome dos atributos do model que serão irão aparecer no relatório

 $ list_report = ('atributo1', 'atributo2', )

-Ainda na classe de administração do modelo adicione a action "report_generic" na lista de actions

 $ actions = [report_generic, ]