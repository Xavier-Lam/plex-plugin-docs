==============================
Global Functions & Decorators
==============================

.. _handler:

@handler
--------

Registers a function as a top-level menu handler with a URL prefix.

.. code-block:: python

   @handler('/video/myplugin', 'My Plugin', thumb='icon-default.png')
   def Main():
       oc = ObjectContainer()
       oc.add(DirectoryObject(key=Callback(SubMenu), title="Browse"))
       return oc

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Parameter
     - Type
     - Description
   * - prefix
     - str
     - The URL prefix for this handler (e.g. ``'/video/myplugin'``).
   * - name
     - str
     - Display name shown to users.
   * - thumb
     - str
     - Resource name for icon image.
   * - art
     - str
     - Resource name for background art.
   * - titleBar
     - str
     - Resource name for title bar image.
   * - share
     - bool
     - Whether to share this handler across plugins.
   * - allow_sync
     - bool
     - Whether to allow sync for this handler.

.. _route:

@route
------

Registers a function to handle a specific URL path pattern.

.. code-block:: python

   @route('/video/myplugin/item/{id}')
   def GetItem(id):
       ...

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - path
     - str
     - URL path pattern. Can contain ``{param}`` placeholders.
   * - method
     - str or list
     - HTTP method(s) (``'GET'``, ``'POST'``, ``['GET','POST']``).
   * - allow_sync
     - bool
     - Whether to allow sync for this route.

.. _callback:

Callback
--------

Generates a callback URL path for the given function with optional keyword arguments.

.. code-block:: python

   DirectoryObject(key=Callback(SubMenu, title="Action"), title="Go")

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - func
     - function
     - The function to call back.
   * - \*\*kwargs
     - any
     - Arguments to pass to the function. Values are URL-encoded.

Returns str — a URL path string.

.. _indirect:

@indirect
---------

Marks a function as returning indirect content (content that requires a secondary lookup).

.. _deferred:

@deferred
---------

Marks a function as deferred (content resolved lazily on demand).

.. _expose:

@expose
-------

Marks a function as callable from other plug-ins or from the server itself.

.. _thread-decorator:

@thread (decorator)
-------------------

Decorator that makes a function execute in a new background thread when called.

.. _spawn:

@spawn
------

Immediately executes the decorated function in a new thread.

.. _lock-decorator:

@lock (decorator)
-----------------

Decorator that acquires the named lock(s) before executing the function, releasing them afterward.

.. _parallelize-parallel-task:

@parallelize / @parallel / @task
---------------------------------

Decorators for parallel task execution (see :ref:`Thread <thread>`).
