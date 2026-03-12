============
Resource API
============

Resources are files bundled inside a plugin under ``Contents/Resources/``. The
Resource API gives your code two ways to work with them:

* **Reference** a resource file by URL so that PMS or a client can fetch its
  contents — without reading the file yourself.
* **Load** a resource file's raw bytes or text into memory so your code can
  process them at runtime.


.. _resource-externalpath:

ExternalPath(itemname) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a URL that Plex Media Server will use to serve the named resource file
to clients. The file is **not** read by this call; it is only located on disk
to verify existence and obtain its modification time.

The returned path has the form::

   /:/plugins/{identifier}/resources/{itemname}?t={mtime}

The ``?t=`` query parameter is the file's modification time in seconds. It acts
as a cache-buster: when a resource file changes, its mtime changes and therefore
the URL changes, causing clients to re-fetch it instead of serving a stale
cached copy.

Typical use — assigning image resources to object attributes:

.. code-block:: python

   DirectoryObject(
       title='My Channel',
       thumb=Resource.ExternalPath('icon-default.png'),
       art=Resource.ExternalPath('art-default.jpg'),
   )

.. note::

   ``R(itemname)`` is a published alias for this method and is the shorthand
   form used in most plugins. See :ref:`r-func` below.

.. _resource-load:

Load(itemname, binary=True) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Opens the named resource file and returns its contents. The file is read from
disk on every call — there is no caching.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``itemname``
     - ``str``
     - Filename relative to ``Contents/Resources/``.
   * - ``binary``
     - ``bool``
     - If ``True`` (default) the file is opened in binary mode and bytes are
       returned. Pass ``False`` to open in text mode and return a ``str``.

.. code-block:: python

   # Load a JSON config file as text
   raw = Resource.Load('config.json', binary=False)
   config = JSON.ObjectFromString(raw)

   # Load a binary file
   data = Resource.Load('template.dat')

.. _resource-guessmimetype:

GuessMimeType(path) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the MIME type string inferred from the file extension of *path* using
Python's built-in ``mimetypes`` module. No file I/O is performed.

.. code-block:: python

   Resource.GuessMimeType('video.mp4')   # → 'video/mp4'
   Resource.GuessMimeType('thumb.jpg')   # → 'image/jpeg'
   Resource.GuessMimeType('data.json')   # → 'application/json'

.. _resource-addmimetype:

AddMimeType(mimetype, extension)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registers a custom MIME type for the given file extension. This is a one-time
registration that affects the entire process for the rest of its lifetime.

.. note::

   Available in legacy and bundle plugins only. Not available under the modern
   (``ModernPolicy``) sandbox.

.. code-block:: python

   Resource.AddMimeType('application/x-custom', '.myext')

.. _resource-contentsofurlwithfallback:

ContentsOfURLWithFallback(url, fallback=None, hosted_fallback=None) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generates a **callback URL** that, when fetched by PMS, tries to reach a
remote URL and falls back to a bundled or hosted resource if the remote URL is
unavailable. This is useful for remote images that can fall back to a local
placeholder.

This method does **not** make any network request itself. It returns an opaque
callback URL string that PMS evaluates lazily.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Type
     - Description
   * - ``url``
     - ``str`` or ``list[str]``
     - One URL, or a list of URLs to try in order. PMS will redirect to the
       first URL that responds successfully.
   * - ``fallback``
     - ``str`` or ``None``
     - Filename of a bundled resource (inside ``Contents/Resources/``) to use
       if all remote URLs fail.
   * - ``hosted_fallback``
     - ``tuple`` or ``None``
     - A 2- or 3-element tuple ``(type, group)`` or ``(type, group, identifier)``
       pointing to a Plex-hosted resource to use if all remote URLs and
       ``fallback`` fail.

.. code-block:: python

   # Prefer a remote image; fall back to a bundled placeholder
   thumb = Resource.ContentsOfURLWithFallback(
       url='https://example.com/poster.jpg',
       fallback='missing-poster.png',
   )

   # Try multiple remote URLs
   thumb = Resource.ContentsOfURLWithFallback(
       url=['https://cdn1.example.com/img.jpg', 'https://cdn2.example.com/img.jpg'],
       fallback='missing-poster.png',
   )

.. _resource-hosted:

Hosted(type, group, identifier=None) → HostedResource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a ``HostedResource`` object that resolves to a URL on Plex's CDN
(``resources-cdn.plexapp.com``). When coerced to a string (e.g. assigned to
an object attribute), it produces a URL of the form::

   http://resources-cdn.plexapp.com/{type}/{group}/{filename}?h={hash}

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Type
     - Description
   * - ``type``
     - ``str``
     - Resource type, typically ``'image'``.
   * - ``group``
     - ``str``
     - Resource group, e.g. ``'source'``, ``'art'``, ``'thumb'``.
   * - ``identifier``
     - ``str`` or ``None``
     - Plugin bundle identifier. Defaults to the current plugin's identifier.

Used internally by the framework to supply default art and thumbnails from
Plex's hosted resource set when a plugin does not provide its own.

.. _resource-sharedexternalpath:

SharedExternalPath(itemname) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. deprecated:: 2.0

   Identical to :ref:`resource-externalpath`. Use
   ``Resource.ExternalPath()`` or :ref:`r-func` instead.

LoadShared(itemname, binary=True) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. deprecated:: 2.0

   Identical to :ref:`resource-load`. Use ``Resource.Load()`` instead.

.. _r-func:

R
-

.. code-block:: text

   R(itemname) → str

A published alias for ``Resource.ExternalPath()``. This is the idiomatic
shorthand used in most plugins.

``R()`` returns a URL that PMS will serve for the named file inside
``Contents/Resources/``. It does **not** read the file's contents; it only
checks that the file exists and appends its mtime for cache-busting.

.. code-block:: python

   DirectoryObject(
       title='Browse',
       thumb=R('icon-default.png'),
       art=R('art-default.jpg'),
   )

.. note::

   Use ``R()`` (not ``Resource.Load()``) when assigning images to object
   attributes. ``R()`` produces a URL reference; ``Resource.Load()`` reads
   the entire file into memory, which is wasteful for images that will only
   be fetched by a client.

Resources are stored in ``Contents/Resources/`` within the bundle. When a
resource is referenced from a service sandbox, the framework first searches the
service bundle's own ``Contents/Resources/`` and then falls back to the main
plugin's ``Contents/Resources/``.
