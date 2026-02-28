=============
Threading API
=============

.. _thread:

Thread
------

Thread management.

Create(f, globalize=True, \*args, \*\*kwargs) → Thread
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates and starts a new thread.

CreateTimer(interval, f, globalize=True, \*args, \*\*kwargs) → Timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a delayed execution timer.

Sleep(interval)
~~~~~~~~~~~~~~~

Pauses the current thread for the given number of seconds.

Lock(key=None) → Lock
~~~~~~~~~~~~~~~~~~~~~~

Returns a named or anonymous lock.

AcquireLock(key)
~~~~~~~~~~~~~~~~

Acquires a named lock.

ReleaseLock(key)
~~~~~~~~~~~~~~~~

Releases a named lock.

Block(key)
~~~~~~~~~~

Clears a named event (blocks waiters).

Unblock(key)
~~~~~~~~~~~~

Sets a named event (unblocks waiters).

Wait(key, timeout=None) → bool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Waits for a named event. Returns True if event was set.

Event(key=None) → Event
~~~~~~~~~~~~~~~~~~~~~~~~

Returns a named or anonymous event.

Semaphore(key=None, limit=1) → Semaphore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a named or anonymous semaphore.

Queue
~~~~~

Reference to Python's ``Queue.Queue`` class.

Decorator Examples
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @thread
   def background_task():
       # This runs in a new thread
       ...

   background_task()  # Returns immediately, function runs in background

.. code-block:: python

   @spawn
   def init_task():
       # Runs immediately in a new thread when the module loads
       ...

.. code-block:: python

   @lock('my_operation')
   def safe_operation():
       # Runs with 'my_operation' lock held
       ...

.. code-block:: python

   @parallelize
   def fetch_all():
       for url in urls:

           @task
           def fetch(url=url):
               results.append(HTTP.Request(url).content)
