========================
Data & Persistence API
========================

.. _data:

Data
----

Binary data storage.

Load(item) → str
~~~~~~~~~~~~~~~~~

Loads a stored binary data item by name.

Save(item, data)
~~~~~~~~~~~~~~~~~

Stores binary data under the given name.

LoadObject(item) → object
~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads a stored Python object by name.

SaveObject(item, obj)
~~~~~~~~~~~~~~~~~~~~~~

Stores a Python object under the given name.

Exists(item) → bool
~~~~~~~~~~~~~~~~~~~~

Checks if a data item exists.

Remove(item)
~~~~~~~~~~~~~

Removes a stored data item.

.. code-block:: python

   # Store and load binary data
   Data.Save('my_cache', some_data)
   loaded = Data.Load('my_cache')

   # Store and load Python objects
   Data.SaveObject('settings', {'key': 'value'})
   obj = Data.LoadObject('settings')

.. _dict:

Dict
----

A dictionary-like object that is automatically persisted to disk. Changes are auto-saved after a short delay.

**Supported operators:**

- ``Dict[key]`` — gets a value by key
- ``Dict[key] = value`` — sets a value
- ``del Dict[key]`` — deletes a key
- ``len(Dict)`` — number of keys
- ``for key in Dict`` — iterates over keys

Save()
~~~~~~

Forces immediate save to disk.

Reset()
~~~~~~~

Resets to defaults (from ``DefaultDict.json``).

.. code-block:: python

   Dict['last_update'] = Datetime.Now()
   if 'favorites' not in Dict:
       Dict['favorites'] = []
   Dict['favorites'].append('item_id')
   Dict.Save()
