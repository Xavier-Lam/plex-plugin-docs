===========
Service API
===========

.. _urlservice:

URLService
----------

URL service functions.

MetadataObjectForURL(url) → MetadataObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gets metadata for a URL.

MediaObjectsForURL(url) → list[MediaObject]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gets media objects for a URL.

NormalizeURL(url) → str
~~~~~~~~~~~~~~~~~~~~~~~~

Normalizes a URL.

ServiceIdentifierForURL(url) → str or None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gets the service identifier matching a URL.

AllPatterns → list[str]
~~~~~~~~~~~~~~~~~~~~~~~~

All registered URL patterns.

.. _searchservice:

SearchService
-------------

Search service functions.

Query(query, identifier, name) → results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Executes a search.

List(identifier) → list[str]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists available search services.

.. _sharedcodeservice:

SharedCodeService
-----------------

Access shared code modules by name:

.. code-block:: python

   result = SharedCodeService.MyModule.my_function()
