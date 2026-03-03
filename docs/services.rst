.. _services:

===========
Service API
===========

Services are a set of well-defined functions that allow plug-ins to interact
with web content in a standardised way. Because service behaviour is consistent
across plug-ins, Plex can leverage services for features like universal search,
URL resolution, and related content discovery.

Three types of service are available:

- **URL Services** — convert a website URL into standardised Plex metadata
  objects and playable media.
- **Search Services** — accept a search query and return a container of matching
  results. All installed search services contribute to Plex's universal search.
- **Related Content Services** — accept a metadata object and return related
  items.

.. _service-directory-structure:

Directory Structure
-------------------

There are two ways to organise service files: *old-style* (declared in
``Info.plist``) and *new-style* (using a separate ``ServiceInfo.plist``).

Old-style (plist-declared)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Declare services via ``PlexURLServices``, ``PlexSearchServices``, or
``PlexRelatedContentServices`` in ``Info.plist`` (see :ref:`plist-services`).
Source files go directly under ``Contents/``:

.. code-block:: text

   MyPlugin.bundle/
   └── Contents/
       ├── Info.plist              # Contains PlexURLServices etc.
       ├── URL Services/
       │   └── YouTube/
       │       └── ServiceCode.pys
       ├── Search Services/
       │   └── VideoSurf/
       │       └── ServiceCode.pys
       └── Related Content Services/
           └── YouTube/
               └── ServiceCode.pys

New-style (ServiceInfo.plist)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Declare services in a ``ServiceInfo.plist`` file inside a ``Contents/Services/``
directory. The plist uses top-level ``URL``, ``Search``, and ``RelatedContent``
keys with the same dictionary structure as the old-style plist keys.

.. code-block:: text

   MyPlugin.bundle/
   └── Contents/
       └── Services/
           ├── ServiceInfo.plist   # Defines URL, Search, RelatedContent
           ├── URL/
           │   └── MyService/
           │       └── ServiceCode.pys
           ├── Search/
           │   └── MySearch/
           │       └── ServiceCode.pys
           ├── Related Content/
           │   └── MyRelated/
           │       └── ServiceCode.pys
           ├── Shared Code/        # Shared .pys modules (optional)
           │   └── utils.pys
           └── Resources/          # Service-specific resources (optional)

**ServiceInfo.plist example:**

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>URL</key>
     <dict>
       <key>IVA</key>
       <dict>
         <key>URLPatterns</key>
         <array>
           <string>^(iva?:)?//(api.)?internetvideoarchive.com</string>
         </array>
       </dict>
     </dict>
   </dict>
   </plist>

Shared Code
~~~~~~~~~~~

Shared ``.pys`` modules placed in the ``Shared Code/`` directory (two levels up
from the service source file) are automatically loaded and importable from
service code. This allows URL, Search, and Related Content services to reuse
common logic.

----

.. _urlservice:

URL Services
------------

URL services convert a website URL into Plex metadata objects. A URL service
source file (``ServiceCode.pys``) should define the following functions:

.. _normalizeurl:

NormalizeURL(url) → str
~~~~~~~~~~~~~~~~~~~~~~~~

*Optional.* Returns a normalised version of the given URL. Plex uses the URL as
a unique identifier, so different URLs pointing to the same content should be
normalised to a single canonical form. This function is called automatically
before ``MetadataObjectForURL`` and ``MediaObjectsForURL``.

.. note::

   This function should execute quickly — avoid HTTP requests.

:param url: The URL to normalise.
:type url: str
:returns: The normalised URL, or ``None`` to use the original.
:rtype: str

.. _metadataobjectforurl:

MetadataObjectForURL(url) → MetadataObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates and returns a metadata object (e.g. :ref:`VideoClipObject <videoclipobject>`,
:ref:`TrackObject <trackobject>`) populated with metadata from the given URL.
Only metadata should be set here — the ``key`` and ``rating_key`` properties are
synthesised automatically based on the URL.

:param url: The normalised URL.
:type url: str
:returns: A metadata object, or ``None`` if the URL cannot be handled.

.. note::

   Media items can be created here, but it is not required. If no items are
   provided, they will be populated by ``MediaObjectsForURL`` automatically.

.. _mediaobjectsforurl:

MediaObjectsForURL(url) → list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates and returns a list of :ref:`MediaObject <mediaobject>` and
:ref:`PartObject <partobject>` instances representing the playable media at the
given URL. Callbacks may be used if obtaining the final media location requires
additional computation.

.. note::

   This function should execute quickly — avoid HTTP requests. It may be called
   many times when building a container.

:param url: The normalised URL.
:type url: str
:returns: A list of media objects.
:rtype: list

URL Service API (consumer side)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following functions are published as global names and can be called from
plug-in code to interact with URL services:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Function
     - Description
   * - ``URLService.MetadataObjectForURL(url)``
     - Calls the appropriate URL service and returns the metadata object.
   * - ``URLService.MediaObjectsForURL(url)``
     - Returns the list of media objects for a URL.
   * - ``URLService.NormalizeURL(url)``
     - Returns the normalised URL.
   * - ``URLService.ServiceIdentifierForURL(url)``
     - Returns the service identifier matching the URL, or ``None``.
   * - ``URLService.AllPatterns``
     - Returns all registered URL patterns (list of str).

Testing a URL service
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ"

Using URL services from plug-in code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than calling ``URLService.MetadataObjectForURL()`` (which can be slow),
you can set the ``url`` property on a metadata object. The framework will
automatically invoke the service to populate media items and set ``key`` /
``rating_key``:

.. code-block:: python

   video = VideoClipObject(
       title = 'My Video',
       summary = 'A great video.',
       url = 'http://www.youtube.com/watch?v=dQw4w9WgXcQ'
   )

----

.. _searchservice:

Search Services
---------------

Search services accept a user query and return a container of results. They
contribute to Plex's universal search. A Search service ``ServiceCode.pys``
should define:

.. _searchfunction:

Search(query) → ObjectContainer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accepts a search query string and returns an :ref:`ObjectContainer <objectcontainer>`
of matching metadata objects. Mixed object types can be in a single container.

The ``source_title`` property can be set on returned objects to indicate the
result source. If omitted, the service name is used.

If the items can be handled by a URL service, set the ``url`` property on each
object to enable automatic service invocation.

:param query: The user's search query.
:type query: str
:returns: A container of matching results.
:rtype: :ref:`ObjectContainer <objectcontainer>`

Search Service API (consumer side)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Function
     - Description
   * - ``SearchService.Query(query, identifier, name=None)``
     - Executes a search using the specified service.
   * - ``SearchService.List(identifier)``
     - Lists available search service names for an identifier.

Testing a search service
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://localhost:32400/system/services/search?identifier=com.plexapp.search.videosurf&query=dog"

----

.. _relatedcontentservice:

Related Content Services
------------------------

Related content services accept a metadata object and return related items. A
Related Content service ``ServiceCode.pys`` should define:

.. _relatedcontentfunction:

RelatedContentForMetadata(metadata) → ObjectContainer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accepts a metadata object and returns an :ref:`ObjectContainer <objectcontainer>`
of related items. As with search services, ``source_title`` can be set and
``url`` can be used to invoke URL services.

:param metadata: The metadata object to find related content for.
:returns: A container of related items.
:rtype: :ref:`ObjectContainer <objectcontainer>`

.. note::

   Each related content service must share an ``Identifier`` with its associated
   URL service so Plex can link them.

Testing a related content service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://localhost:32400/system/services/relatedcontent/lookup?url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ"

----

.. _sharedcodeservice:

SharedCodeService
-----------------

Access shared code modules (from the ``Shared Code/`` directory) by name:

.. code-block:: python

   result = SharedCodeService.MyModule.my_function()
