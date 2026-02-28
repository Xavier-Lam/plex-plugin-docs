====================
Runtime & Plugin API
====================

.. _plugin:

Plugin
------

Plugin information (legacy).

Identifier → str
~~~~~~~~~~~~~~~~~

The plug-in's identifier string.

Title → str
~~~~~~~~~~~~

The plug-in's display title.

IconResourceName → str
~~~~~~~~~~~~~~~~~~~~~~

Name of the icon resource file.

ArtResourceName → str
~~~~~~~~~~~~~~~~~~~~~

Name of the art resource file.

TitleBarResourceName → str
~~~~~~~~~~~~~~~~~~~~~~~~~~

Name of the title bar resource file.

Prefixes → list
~~~~~~~~~~~~~~~~

Currently registered URL prefixes.

ViewGroups → dict
~~~~~~~~~~~~~~~~~

Currently registered view groups.

Traceback(msg='Traceback')
~~~~~~~~~~~~~~~~~~~~~~~~~~

Logs a traceback.

Nice(value) → int
~~~~~~~~~~~~~~~~~~

Sets process niceness (0–20).

AddPrefixHandler(prefix, handler, name, thumb=None, art=None, titleBar=None, share=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registers a URL prefix handler. Legacy.

AddViewGroup(name, viewMode="List", mediaType="items", type=None, menu=None, cols=None, rows=None, thumb=None, summary=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registers a view group. Legacy.

.. _client:

Client
------

Client information for the current request.

Platform → str
~~~~~~~~~~~~~~~

Client platform (e.g. ``'iOS'``, ``'Android'``, ``'MacOSX'``).

Product → str
~~~~~~~~~~~~~

Client product name (e.g. ``'Plex/iOS'``).

Version → str
~~~~~~~~~~~~~~

Client version string.

.. _platform:

Platform
--------

Server platform information.

OS → str
~~~~~~~~~

Server OS (``'MacOSX'``, ``'Windows'``, ``'Linux'``).

OSVersion → str
~~~~~~~~~~~~~~~~

OS version string.

CPU → str
~~~~~~~~~~

CPU architecture (``'i386'``, ``'x86_64'``, etc.).

HasWebKit → bool
~~~~~~~~~~~~~~~~~

Whether WebKit is available.

HasFlash → bool
~~~~~~~~~~~~~~~~

*Deprecated*. Always False.

HasSilverlight → bool
~~~~~~~~~~~~~~~~~~~~~~

*Deprecated*. Always False.

MachineIdentifier → str
~~~~~~~~~~~~~~~~~~~~~~~~

Unique server identifier.

ServerVersion → str
~~~~~~~~~~~~~~~~~~~

Plex Media Server version.

.. _prefs:

Prefs
-----

Access user preferences defined in ``Contents/DefaultPrefs.json``.

.. code-block:: python

   username = Prefs['username']
   quality = Prefs['quality']

.. _request:

Request
-------

Current HTTP request context.

Headers → dict
~~~~~~~~~~~~~~~

HTTP headers of the current request.

Body → str
~~~~~~~~~~~

POST body of the current request.

Method → str
~~~~~~~~~~~~~

HTTP method (``'GET'``, ``'POST'``, etc.).

.. _response:

Response
--------

Current HTTP response context.

Headers → dict
~~~~~~~~~~~~~~~

Response headers to send. Get / set.

Status → int
~~~~~~~~~~~~~

HTTP response status code. Get / set.

.. _route-1:

Route
-----

Route management.

Connect(path, f, method=['GET'], allow_sync=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programmatically connects a route.
