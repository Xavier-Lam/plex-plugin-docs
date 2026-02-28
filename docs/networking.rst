==============
Networking API
==============

.. _http:

HTTP
----

HTTP client for making web requests.

Request(url, values=None, headers={}, cacheTime=None, encoding=None, errors=None, timeout=GLOBAL_DEFAULT_TIMEOUT, immediate=False, sleep=0, data=None, follow_redirects=True, method=None) → HTTPRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates and returns an HTTP request object.

.. list-table::
   :header-rows: 1
   :widths: 18 15 12 55

   * - Parameter
     - Type
     - Default
     - Description
   * - url
     - str
     - *(required)*
     - The URL to request.
   * - values
     - dict or None
     - None
     - POST form data (URL-encoded automatically).
   * - headers
     - dict
     - {}
     - Additional HTTP headers.
   * - cacheTime
     - int or None
     - None
     - Max cache age in seconds (None = use default).
   * - encoding
     - str or None
     - None
     - Force a specific character encoding.
   * - errors
     - str or None
     - None
     - Error handling: ``'strict'``, ``'ignore'``, or ``'replace'``.
   * - timeout
     - float
     - GLOBAL_DEFAULT_TIMEOUT
     - Request timeout in seconds.
   * - immediate
     - bool
     - False
     - If True, sends request immediately on creation.
   * - sleep
     - float
     - 0
     - Seconds to sleep after a real (non-cached) request.
   * - data
     - str or None
     - None
     - Raw POST body (mutually exclusive with values).
   * - follow_redirects
     - bool
     - True
     - Whether to follow HTTP redirects.
   * - method
     - str or None
     - None
     - HTTP method override (e.g. ``'PUT'``, ``'DELETE'``).

The returned HTTPRequest object has:

- ``.content`` → str — the response body as a string.
- ``.headers`` → dict — the response HTTP headers.

.. code-block:: python

   # Simple GET
   page = HTTP.Request('https://example.com/api').content

   # POST with form data
   response = HTTP.Request('https://example.com/api', values={'key': 'value'}).content

   # POST with raw JSON
   response = HTTP.Request('https://example.com/api',
       data=JSON.StringFromObject({'key': 'value'}),
       headers={'Content-Type': 'application/json'}
   ).content

   # With caching
   page = HTTP.Request('https://example.com', cacheTime=CACHE_1HOUR).content

CacheTime → float
~~~~~~~~~~~~~~~~~~

Default cache time (in seconds) for all HTTP requests. Get / set.

.. code-block:: python

   HTTP.CacheTime = CACHE_1HOUR

Headers → dict
~~~~~~~~~~~~~~~

A dict of default HTTP headers sent with every request. Get / set.

.. code-block:: python

   HTTP.Headers['User-Agent'] = 'My Plugin/1.0'
   HTTP.Headers['Accept-Language'] = 'en'

CookiesForURL(url) → str
~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the cookie string for a given URL.

SetPassword(url, username, password, realm=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets HTTP Basic Authentication credentials for a URL.

PreCache(url, values=None, headers={}, cacheTime=None, encoding=None, errors=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-caches an HTTP response in a background thread.

Cookies → CookieJar
~~~~~~~~~~~~~~~~~~~~

Returns the cookie jar object.

ClearCookies()
~~~~~~~~~~~~~~

Clears all stored cookies.

ClearCache()
~~~~~~~~~~~~

Clears the HTTP response cache.

.. _network:

Network
-------

Network information and utilities.

Address → str
~~~~~~~~~~~~~

Server's local IP address.

PublicAddress → str
~~~~~~~~~~~~~~~~~~~

Server's public IP address.

Hostname → str
~~~~~~~~~~~~~~~

Server's hostname.

Timeout → float
~~~~~~~~~~~~~~~~

Default network timeout. Get / set.

Socket() → socket
~~~~~~~~~~~~~~~~~~

Creates a new socket object.

.. _xmlrpc:

XMLRPC
------

Proxy(url, encoding=None) → ServerProxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns an ``xmlrpclib.ServerProxy`` object for XML-RPC calls.
