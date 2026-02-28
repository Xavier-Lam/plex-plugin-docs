================================
Plugin Lifecycle & Entry Points
================================

.. _start:

Start
-----

Called when the plug-in is first loaded by the server. Used for one-time initialization.

.. code-block:: python

   def Start():
       HTTP.CacheTime = CACHE_1HOUR
       HTTP.Headers['User-Agent'] = 'Mozilla/5.0'

.. _validateprefs:

ValidatePrefs
-------------

Called when the user saves preferences. Return a :ref:`MessageContainer <messagecontainer>` to display feedback.

.. code-block:: python

   def ValidatePrefs():
       if Prefs['username'] is None:
           return MessageContainer("Error", "Username is required.")
