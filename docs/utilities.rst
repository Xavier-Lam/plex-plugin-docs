===========
Utility API
===========

.. _string:

String
------

String utilities. Aliases: ``E(s)`` = ``String.Encode(s)``, ``D(s)`` = ``String.Decode(s)``.

Encode(s) → str
~~~~~~~~~~~~~~~~

URL-safe Base64 encoding.

Decode(s) → str
~~~~~~~~~~~~~~~~

Decodes URL-safe Base64.

Base64Encode(s, with_newlines=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Standard Base64 encoding.

Base64Decode(s) → str
~~~~~~~~~~~~~~~~~~~~~

Standard Base64 decoding.

Quote(s, usePlus=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

URL-encodes a string.

Unquote(s, usePlus=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

URL-decodes a string.

URLEncode(s) → str
~~~~~~~~~~~~~~~~~~~

URL-encodes a string (alias for ``Quote``).

StripTags(s) → str
~~~~~~~~~~~~~~~~~~~

Removes HTML tags.

DecodeHTMLEntities(s) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts HTML entities to characters.

UUID() → str
~~~~~~~~~~~~~

Generates a UUID string.

StripDiacritics(s) → str
~~~~~~~~~~~~~~~~~~~~~~~~~

Removes diacritics / accents.

Pluralize(s) → str
~~~~~~~~~~~~~~~~~~~

Returns plural form.

LevenshteinDistance(a, b) → int
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Computes edit distance between two strings.

LevenshteinRatio(a, b) → float
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Computes similarity ratio (0.0–1.0).

LongestCommonSubstring(a, b) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Longest common substring.

CapitalizeWords(s) → str
~~~~~~~~~~~~~~~~~~~~~~~~~

Capitalizes each word.

ParseQueryString(s) → dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses URL query string.

ParseQueryStringAsList(s) → list[tuple]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses URL query string as list of tuples.

SplitExtension(s) → tuple
~~~~~~~~~~~~~~~~~~~~~~~~~~

Splits filename and extension.

Dedent(s) → str
~~~~~~~~~~~~~~~~

Removes common leading whitespace.

Join(words, sep=None) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Joins words with separator.

JoinURL(base, url) → str
~~~~~~~~~~~~~~~~~~~~~~~~~

Joins a base URL and relative URL.

Clean(s, form='NFKD', lang=None, strip_diacritics=False, strip_punctuation=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normalizes and cleans a string.

String Constants
~~~~~~~~~~~~~~~~

- ``String.LETTERS``, ``String.LOWERCASE``, ``String.UPPERCASE``, ``String.DIGITS``
- ``String.HEX_DIGITS``, ``String.OCT_DIGITS``, ``String.PUNCTUATION``
- ``String.PRINTABLE``, ``String.WHITESPACE``

.. _hash:

Hash
----

Cryptographic hashing. All methods accept a ``digest`` parameter (default False); when True they return raw binary digest instead of hex string.

MD5(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MD5 hash.

SHA1(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHA-1 hash.

SHA224(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHA-224 hash.

SHA256(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHA-256 hash.

SHA384(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHA-384 hash.

SHA512(data, digest=False) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHA-512 hash.

CRC32(data) → int
~~~~~~~~~~~~~~~~~~

CRC32 checksum.

.. _regex:

Regex
-----

Regular expression compiler. ``Regex`` is callable — it compiles a regular expression pattern.

.. code-block:: python

   pattern = Regex(r'<title>(.*?)</title>', Regex.IGNORECASE | Regex.DOTALL)
   match = pattern.search(html)
   if match:
       title = match.group(1)

Regex Constants
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Constant
     - Description
   * - Regex.IGNORECASE
     - Case-insensitive matching.
   * - Regex.MULTILINE
     - ``^`` / ``$`` match at line boundaries.
   * - Regex.DOTALL
     - ``.`` matches newlines.

.. _datetime:

Datetime
--------

Date and time utilities.

Now() → datetime
~~~~~~~~~~~~~~~~~

Current local date/time.

UTCNow() → datetime
~~~~~~~~~~~~~~~~~~~~

Current UTC date/time.

ParseDate(date, fmt=None) → datetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parses a date string. Auto-detects format if fmt is None.

Delta(\*\*kwargs) → timedelta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a timedelta. Accepts ``days``, ``hours``, ``minutes``, ``seconds``, ``weeks``, etc.

TimestampFromDatetime(dt) → int
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts to UNIX timestamp.

FromTimestamp(ts) → datetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts from UNIX timestamp.

MillisecondsFromString(s) → int
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts duration string (e.g. ``"1:23:45"``) to milliseconds.

.. code-block:: python

   date = Datetime.ParseDate("2020-01-15")
   one_week_ago = Datetime.Now() - Datetime.Delta(weeks=1)

.. _archive:

Archive
-------

Compression utilities.

Zip(data=None) → ZipArchive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates or loads a ZIP archive.

ZipFromURL(url, ...) → ZipArchive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Downloads and opens a ZIP. Accepts all common HTTP parameters.

GzipCompress(data) → str
~~~~~~~~~~~~~~~~~~~~~~~~~

Gzip-compresses data.

GzipDecompress(data) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gzip-decompresses data.

.. _amf:

AMF
---

ActionScript Message Format utilities.

RemotingService(\*args, amf_version=3) → RemotingService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a PyAMF remoting service.

RegisterClass
~~~~~~~~~~~~~

Reference to ``pyamf.register_class``.

SOL(\*args) → SOL object
~~~~~~~~~~~~~~~~~~~~~~~~~

Loads / creates a Flash Shared Object.

.. _util:

Util
----

General utilities.

Floor(x) → float
~~~~~~~~~~~~~~~~~

Floor function.

Ceiling(x) → float
~~~~~~~~~~~~~~~~~~~

Ceiling function.

VersionAtLeast(version_string, \*components) → bool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checks if version meets minimum.

ListSortedByKey(l, key) → list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns list sorted by dict key.

ListSortedByAttr(l, attr) → list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns list sorted by attribute.

SortListByKey(l, key)
~~~~~~~~~~~~~~~~~~~~~~

In-place sort by dict key.

SortListByAttr(l, attr)
~~~~~~~~~~~~~~~~~~~~~~~~

In-place sort by attribute.

LevenshteinDistance(a, b) → int
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit distance.

LongestCommonSubstring(a, b) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Longest common substring.

Random() → float
~~~~~~~~~~~~~~~~~

Random float [0, 1).

RandomInt(a, b) → int
~~~~~~~~~~~~~~~~~~~~~~

Random integer [a, b].

RandomItemFromList(l) → any
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Random item from list.

RandomChoice(l) → any
~~~~~~~~~~~~~~~~~~~~~~

Random choice.

RandomSample(l, count) → list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Random sample.
