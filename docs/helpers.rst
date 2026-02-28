==========
Helper API
==========

Available only for elevated (bundled) plugins. Helpers are placed in ``Contents/Helpers/<OS>/<CPU>/`` inside the bundle.

.. _helper:

Helper
------

External binary execution.

Run(helper, \*args) → str
~~~~~~~~~~~~~~~~~~~~~~~~~~

Runs a helper binary and returns output.

Process(helper, \*args, stderr=False) → Popen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starts a subprocess with pipe access.

.. code-block:: python

   output = Helper.Run('my_tool', '--input', '/path/to/file')

   proc = Helper.Process('my_tool', '--input', '/path/to/file')
   result = proc.stdout.read()
   proc.stdin.write('data')
