.. _preferences:

===========
Preferences
===========

Preferences are defined in ``Contents/DefaultPrefs.json`` as a JSON array of preference items.
Access preference values in code via the global :ref:`Prefs <prefs>` object.
To validate user input when preferences are saved, implement the :ref:`ValidatePrefs <validateprefs>` lifecycle callback.

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
     - Return type
   * - text
     - Free-text input. Use ``"option": "hidden"`` for passwords.
     - ``str``
   * - bool
     - Boolean toggle. Stored as ``"true"`` / ``"false"`` on disk, but decoded
       before being returned to plug-in code.
     - ``bool`` (Python ``True`` / ``False``)
   * - enum
     - Dropdown selection.
     - ``str`` (the selected value)

.. _prefs:

Accessing Preferences
---------------------

The global ``Prefs`` object provides read-only access to user preferences defined
in ``Contents/DefaultPrefs.json``.

.. code-block:: python

   username = Prefs['username']
   quality = Prefs['quality']

   # Boolean prefs return actual Python bools — use directly in conditions
   if Prefs['subtitles']:
       load_subtitles()

.. note::

   **Text** and **enum** preference values are returned as strings.
   **Boolean** preference values are returned as Python ``bool`` (``True`` / ``False``),
   **not** strings.
   The framework decodes ``"true"`` / ``"false"`` strings internally via
   ``BooleanPref.decode_value()`` before returning to plug-in code.

.. warning::

   ``Prefs`` is a read-only accessor — you cannot set preference values from
   code. Preferences are managed by the server UI and stored in a per-user
   preferences file.
