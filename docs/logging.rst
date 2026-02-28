===========
Logging API
===========

.. _log:

Log
---

Logging facility. ``Log`` is callable directly (equivalent to ``Log.Info``).

Log(fmt, \*args)
~~~~~~~~~~~~~~~~

Logs at INFO level.

.. code-block:: python

   Log("Found %d results for '%s'", len(results), query)

Debug(fmt, \*args)
~~~~~~~~~~~~~~~~~~

Logs at DEBUG level.

Info(fmt, \*args)
~~~~~~~~~~~~~~~~~

Logs at INFO level.

Warn(fmt, \*args)
~~~~~~~~~~~~~~~~~

Logs at WARNING level.

Error(fmt, \*args)
~~~~~~~~~~~~~~~~~~

Logs at ERROR level.

Critical(fmt, \*args)
~~~~~~~~~~~~~~~~~~~~~

Logs at CRITICAL level.

Exception(fmt, \*args)
~~~~~~~~~~~~~~~~~~~~~~

Logs CRITICAL + traceback. Only use in ``except`` blocks.

.. code-block:: python

   try:
       ...
   except:
       Log.Exception("Error processing item")

Stack()
~~~~~~~

Logs the current stack trace.
