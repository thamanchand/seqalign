.. image:: header1.png

=======
Modules
=======

Applications contains modules, classes and functions. For different processes and subprocess
class and functions are used at modules. The Seq-alignment contains two modules which are described
below with their functionality.

The :mod:`index` Module
-----------------------

.. module:: index

:class:`HtmlTemplate`

.. class:: HtmlTemplate

The :class:`HtmlTemplate` is responsible for following methods


    .. method:: HtmlTemplate.Header(self)

    .. method:: HtmlTemplate.Body(self)

    .. method:: HtmlTemplate.Form(self)

    .. method:: HtmlTemplate.Footer(self)

    .. method:: HtmlTemplate.CloseHtml(self)

The :mod:`display` Module
-------------------------

.. module:: display

:class:`MainDisplay`

.. class:: MainDisplay

The :class:`MainDisplay` is responsible for following methods


    .. method:: MainDisplay.execute(self)

    .. method:: MainDisplay.display(self)

    .. method:: MainDisplay.tree(self)


Code Block
----------

1. Index.py
###########

.. literalinclude:: c:\wamp\www\project\index.py
    :linenos:
    :language: python
    :lines: 1-28, 116-153

2. Display.py
#############

.. literalinclude:: c:\wamp\www\project\display.py
    :linenos:
    :language: python
    :lines: 1-6, 7-9, 32-34, 44-52, 55-56

