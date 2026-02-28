==========================================
Container & Object Types (Legacy API)
==========================================

These are available for older-style plugins. Modern plugins should use the types in :doc:`modern_api`.

.. _mediacontainer:

MediaContainer
--------------

.. code-block:: python

   MediaContainer(art=None, viewGroup=None, title1=None, title2=None, noHistory=False, replaceParent=False, disabledViewModes=None, **kwargs)

Legacy XML container.

Append(obj)
~~~~~~~~~~~

Adds a child object.

Count(x) → int
~~~~~~~~~~~~~~~

Counts occurrences.

Index(x) → int
~~~~~~~~~~~~~~~

Returns index of item.

Extend(x)
~~~~~~~~~~

Extends with a list.

Insert(i, x)
~~~~~~~~~~~~~

Inserts at index.

Pop(i) → item
~~~~~~~~~~~~~~

Removes and returns item at index.

Remove(x)
~~~~~~~~~~

Removes first occurrence.

Reverse()
~~~~~~~~~~

Reverses in place.

Sort(attr, descending=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sorts by attribute.

Clear()
~~~~~~~

Removes all items.

.. _directoryitem:

DirectoryItem
-------------

.. code-block:: python

   DirectoryItem(key, title, subtitle=None, summary=None, thumb=None, art=None)

Navigable directory.

.. _popupdirectoryitem:

PopupDirectoryItem
------------------

.. code-block:: python

   PopupDirectoryItem(key, title, subtitle=None, summary=None, thumb=None, art=None)

Popup directory.

.. _inputdirectoryitem:

InputDirectoryItem
------------------

.. code-block:: python

   InputDirectoryItem(key, title, prompt, subtitle=None, summary=None, thumb=None, art=None)

Input / search directory.

.. _videoitem:

VideoItem
---------

.. code-block:: python

   VideoItem(key=None, title=None, subtitle=None, summary=None, duration=None, thumb=None, art=None, items=[])

Video item.

.. _webvideoitem:

WebVideoItem
-------------

.. code-block:: python

   WebVideoItem(url, title=None, subtitle=None, summary=None, duration=None, thumb=None)

Web video item (WebKit playback).

.. _rtmpvideoitem:

RTMPVideoItem
-------------

.. code-block:: python

   RTMPVideoItem(url, clip=None, clips=None, width=None, height=None, live=False, title=None, subtitle=None, summary=None, duration=None, thumb=None)

RTMP video item.

.. _photoitem:

PhotoItem
---------

.. code-block:: python

   PhotoItem(key, title, subtitle=None, summary=None, thumb=None)

Photo item.

.. _trackitem:

TrackItem
---------

.. code-block:: python

   TrackItem(key, title, artist=None, album=None, index=None, rating=None, duration=None, size=None)

Audio track item.

.. _prefsitem:

PrefsItem
---------

.. code-block:: python

   PrefsItem(title=None, subtitle=None, thumb=None)

Preferences link.

.. _function:

Function
--------

.. code-block:: python

   Function(obj, ext=None, **kwargs)

Wraps an object so its key attribute calls a function with the provided arguments.

.. _indirectfunction:

IndirectFunction
----------------

.. code-block:: python

   IndirectFunction(obj, ext=None, **kwargs)

Same as :ref:`Function <function>` but marks the response as indirect.

.. _messagecontainer:

MessageContainer
----------------

.. code-block:: python

   MessageContainer(header, message, title1=None, title2=None)

Displays a simple message to the user.

.. _redirect:

Redirect
--------

.. code-block:: python

   Redirect(url, temporary=True)

Returns an HTTP redirect response.

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Parameter
     - Type
     - Description
   * - url
     - str
     - The URL to redirect to.
   * - temporary
     - bool
     - If True, uses HTTP 302; if False, uses HTTP 301.

.. _dataobject:

DataObject
----------

.. code-block:: python

   DataObject(data, contentType)

Returns raw binary data with a specified MIME type.

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Parameter
     - Type
     - Description
   * - data
     - str
     - The binary data.
   * - contentType
     - str
     - MIME type (e.g. ``'image/jpeg'``).
