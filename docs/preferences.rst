===========
Preferences
===========

Preferences are defined in ``Contents/DefaultPrefs.json`` as a JSON array of preference items.

.. _preference-types:

Preference Types
----------------

.. code-block:: json

   [
     {
       "id": "username",
       "type": "text",
       "label": "Username",
       "default": ""
     },
     {
       "id": "password",
       "type": "text",
       "label": "Password",
       "default": "",
       "option": "hidden"
     },
     {
       "id": "quality",
       "type": "enum",
       "label": "Video Quality",
       "default": "720",
       "values": "360|480|720|1080"
     },
     {
       "id": "subtitles",
       "type": "bool",
       "label": "Enable Subtitles",
       "default": "true"
     }
   ]

.. list-table::
   :header-rows: 1
   :widths: 10 50 40

   * - Type
     - Description
     - Values
   * - text
     - Free-text input. Use ``"option": "hidden"`` for passwords.
     - String.
   * - bool
     - Boolean toggle.
     - ``"true"`` or ``"false"``.
   * - enum
     - Dropdown selection.
     - Pipe-separated values string.

Access preferences in code:

.. code-block:: python

   username = Prefs['username']
   if Prefs['subtitles'] == 'true':
       ...

.. note::

   All preference values are returned as strings. Boolean prefs return ``"true"`` or ``"false"`` (strings, not Python bools).
