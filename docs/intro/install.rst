.. _intro-install:

==================
Installation guide
==================

.. _faq-python-versions:

Supported Python versions
=========================

PyGoChook requires Python 3.7+ (only tested on 3.7)


Installing PyGoChook
====================

You can install PyGoChook and its dependencies from PyPI with::

    pip install pygochook


We strongly recommend that you install PyGoChook in :ref:`a dedicated virtualenv <intro-using-virtualenv>`,
to avoid conflicting with your system packages.

For more detailed and platform specifics instructions, as well as
troubleshooting information, read on.


Things that are good to know
----------------------------

PyGoChook is written in pure Python and depends on a few key Python packages:

* `aiohttp`_, a request library with asyncio support

.. _aiohttp: https://docs.aiohttp.org/en/stable


.. _intro-using-virtualenv:

Using a virtual environment (recommended)
-----------------------------------------

TL;DR: We recommend installing PyGoChook inside a virtual environment
on all platforms.

Python packages can be installed either globally (a.k.a system wide),
or in user-space. We do not recommend installing PyGoChook system wide.

Instead, we recommend that you install PyGoChook within a so-called
"virtual environment" (:mod:`venv`).
Virtual environments allow you to not conflict with already-installed Python
system packages (which could break some of your system tools and scripts),
and still install packages normally with ``pip`` (without ``sudo`` and the likes).

Once you have created a virtual environment, you can install PyGoChook inside it with ``pip``,
just like any other Python package.


.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/en/latest/installing/