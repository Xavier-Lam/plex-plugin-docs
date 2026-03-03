====================
Runtime & Plugin API
====================

This chapter documents global objects that expose runtime information about the
plug-in, the server, and the current HTTP request. These objects are primarily
used in **route handlers** (registered via ``@route`` or
``Plugin.AddPrefixHandler``), **URL service handlers**, and
**search/related content service handlers** — anywhere plug-in code is invoked
in the context of an HTTP request from a Plex client.

.. _plugin:

Plugin
------

Plugin information (legacy). Used in channel plug-ins for prefix and view group
registration.

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

Client information for the current request. Available in route handlers and
service handlers to identify which Plex client is making the request.

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

.. seealso::

   :ref:`Prefs <prefs>` — Accessing user preferences is documented in the
   :ref:`Preferences <preferences>` chapter.

.. _request:

Request
-------

Current HTTP request context. Available in route handlers and service handlers
to read request data from the Plex client. For example, use ``Request.Headers``
to read custom headers, or ``Request.Body`` to access POST data.

See also: :ref:`HTTP.Request <http>` in the Networking API, which is a
**different** object — it creates *outgoing* HTTP requests to external servers,
while ``Request`` here represents the *incoming* request from a Plex client.

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

Current HTTP response context. Use in route handlers and service handlers to
set response headers or override the status code before returning.

Headers → dict
~~~~~~~~~~~~~~~

Response headers to send. Get / set.

Status → int
~~~~~~~~~~~~~

HTTP response status code. Get / set.

.. _route-1:

Route
-----

Route management. Used by channel plug-ins to programmatically register URL
handlers (as an alternative to the ``@route`` decorator).

Connect(path, f, method=['GET'], allow_sync=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programmatically connects a route.
