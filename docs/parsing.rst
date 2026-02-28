===========
Parsing API
===========

All parsing APIs support both parsing from strings and directly from URLs (with built-in HTTP caching).

All ``*FromURL`` methods accept the following common HTTP parameters in addition to their specific ones:

.. list-table::
   :header-rows: 1
   :widths: 18 15 15 52

   * - Parameter
     - Type
     - Default
     - Description
   * - url
     - str
     - *(required)*
     - URL to fetch.
   * - values
     - dict
     - None
     - POST form data.
   * - headers
     - dict
     - {}
     - Additional headers.
   * - cacheTime
     - float
     - None
     - Cache time in seconds.
   * - encoding
     - str
     - None
     - Character encoding.
   * - errors
     - str
     - None
     - Error handling mode.
   * - timeout
     - float
     - GLOBAL_DEFAULT_TIMEOUT
     - Timeout in seconds.
   * - sleep
     - float
     - 0
     - Post-request sleep time.
   * - follow_redirects
     - bool
     - True
     - Follow redirects.
   * - method
     - str
     - None
     - HTTP method override.

.. _json:

JSON
----

JSON parser.

ObjectFromString(string, encoding=None) → dict or list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses a JSON string.

ObjectFromURL(url, ...) → dict or list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as JSON. Accepts all common HTTP parameters.

StringFromObject(obj) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts an object to a JSON string.

.. _xml:

XML
---

XML parser (powered by lxml).

Element(name, text=None, \*\*kwargs) → \_Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a new XML element.

StringFromElement(el, encoding='utf8') → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Serializes an element to a string.

ElementFromString(string, encoding=None) → \_Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses XML string to an element.

ElementFromURL(url, ...) → \_Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as XML. Accepts all common HTTP parameters.

ObjectFromString(string) → ObjectifiedElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses XML into an objectified element (``lxml.objectify``).

ObjectFromURL(url, ...) → ObjectifiedElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and objectifies XML. Accepts all common HTTP parameters.

StringFromObject(obj, encoding='utf-8') → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Serializes objectified XML to string.

.. _html:

HTML
----

HTML parser (powered by lxml.html).

Element(name, text=None, \*\*kwargs) → HtmlElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a new HTML element.

StringFromElement(el, encoding='utf8') → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Serializes element to string.

ElementFromString(string) → HtmlElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses HTML to element.

ElementFromURL(url, ...) → HtmlElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as HTML. Accepts all common HTTP parameters.

.. _plist:

Plist
-----

Property List parser.

ObjectFromString(string) → dict or list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses a Plist string.

ObjectFromURL(url, ...) → dict or list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as Plist. Accepts all common HTTP parameters.

StringFromObject(obj) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts object to Plist string.

.. _rss:

RSS
---

Feed parser (RSS / Atom / RDF).

FeedFromString(string) → feedparser dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses a feed string.

FeedFromURL(url, ...) → feedparser dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as feed. Accepts all common HTTP parameters.

.. _yaml:

YAML
----

YAML parser.

ObjectFromString(string) → object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses YAML string.

ObjectFromURL(url, ...) → object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetches URL and parses as YAML. Accepts all common HTTP parameters.
