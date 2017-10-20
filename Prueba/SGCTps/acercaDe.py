'''
Informacion
======================

Estaba pensando que esto podriamos implementarlo en la parte de [b]informacion[/b].

Podriamos usarlo como una guia para los usuarios

Video
----------------

.. video:: softboy.mpg


Inline Markup
-------------

- *emphasis*
- **strong emphasis**
- `interpreted text`
- ``inline literal``
- reference_
- `phrase reference`_
- anonymous__
- _`inline internal target`

.. _top:

Internal crossreferences, like example_, or bottom_.

Imagen
-----

.. image:: images/boton_normal.png
Grilla
----

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | column 2   | column 3  |
+------------+------------+-----------+
| body row 3 | column 2   | column 3  |
+------------+------------+-----------+




Admonitions
-----------

.. warning::

    This is just a Test.

.. note::

    And this is just a note. Let's test some literal::

        $ echo 'Hello world'
        Hello world



Usage with Text
---------------

::

    text = """
    .. _top:

    Hello world
    ===========

    This is an **emphased text**, some ``interpreted text``.
    And this is a reference to top_::

        $ print("Hello world")

    """



Go to top_'''

from kivy.uix.rst import RstDocument
from kivy.app import App


class RstApp(App):

    def build(self):
        return RstDocument(text=__doc__)

if __name__ == '__main__':
    RstApp().run()
