============
Resource API
============

.. _resource:

Resource
--------

Bundle resource management.

ExternalPath(itemname) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns an externally accessible URL for a bundled resource.

SharedExternalPath(itemname) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a shared externally accessible URL. Deprecated.

Load(itemname, binary=True) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads a resource file's contents.

GuessMimeType(path) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~

Guesses MIME type from extension.

AddMimeType(mimetype, extension)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registers a custom MIME type. Legacy only.

ContentsOfURLWithFallback(url, fallback=None, hosted_fallback=None) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a callback URL that fetches content with fallback.

Hosted(type, group, identifier=None) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a hosted resource URL.

.. _r-func:

R
-

.. code-block:: text

   R(itemname) → str

Alias for ``Resource.ExternalPath``. Returns an externally accessible URL for a bundled resource.

.. code-block:: python

   # Use a bundled image as a thumbnail
   thumb = R('icon-default.png')

   # Load a resource file
   data = Resource.Load('data.json', binary=False)

Resources are stored in ``Contents/Resources/`` within the bundle.
