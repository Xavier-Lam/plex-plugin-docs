.. _proxy-objects:

=============
Proxy Objects
=============

Proxy objects are used to store media assets (images, audio) in metadata models. Available as the global ``Proxy`` object.

.. _proxymedia:

Proxy.Media
-----------

.. code-block:: text

   Proxy.Media(data, sort_order=None, ext=None, index=None, **kwargs) → ProxyObject

Creates a proxy for media data to be stored on disk.

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - data
     - str
     - Binary image / audio data.
   * - sort_order
     - int or None
     - Sort priority (lower = higher priority).
   * - ext
     - str or None
     - File extension hint.
   * - index
     - str or None
     - Stream index.
   * - \*\*kwargs
     -
     - Extra named data (stored as additional files with the extension as key).

.. _proxypreview:

Proxy.Preview
-------------

.. code-block:: text

   Proxy.Preview(data, sort_order=None, ext=None, index=None, **kwargs) → ProxyObject

Creates a proxy for preview / thumbnail data. Same parameters as :ref:`Proxy.Media <proxymedia>`.

.. _proxylocalfile:

Proxy.LocalFile
---------------

.. code-block:: text

   Proxy.LocalFile(file_path, sort_order=None, ext=None, index=None, **kwargs) → ProxyObject

Creates a proxy that references a local file by path (data is not copied, just referenced).

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Parameter
     - Type
     - Description
   * - file_path
     - str
     - Absolute path to the file on disk.

.. _proxyremote:

Proxy.Remote
------------

.. code-block:: text

   Proxy.Remote(url, sort_order=None, ext=None, index=None, **kwargs) → ProxyObject

Creates a proxy that references a remote URL.

Usage Examples
~~~~~~~~~~~~~~

.. code-block:: python

   # Store a poster from HTTP
   poster_data = HTTP.Request('https://example.com/poster.jpg').content
   metadata.posters['poster_url'] = Proxy.Media(poster_data, sort_order=1)

   # Store a preview thumbnail
   metadata.posters['poster_url'] = Proxy.Preview(thumb_data, sort_order=1)

   # Reference a local file directly
   metadata.posters['local_poster'] = Proxy.LocalFile('/path/to/poster.jpg')

   # Store a subtitle from a local file
   part.subtitles['en']['subtitle_name'] = Proxy.LocalFile('/path/to/subs.srt', ext='srt')

   # Store a subtitle from remote data
   part.subtitles['en']['subtitle_name'] = Proxy.Media(sub_data, ext='srt')
