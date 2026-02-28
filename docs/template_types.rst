=========================
Template Attribute Types
=========================

These are the attribute types used in model definitions. In plugin code, you interact with the instantiated versions.

Value Types
-----------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Template Type
     - Python Type
     - Description
   * - Template.String()
     - unicode
     - Unicode string value.
   * - Template.Integer()
     - int
     - Integer value.
   * - Template.Float()
     - float
     - Floating-point value.
   * - Template.Boolean()
     - bool
     - Boolean value.
   * - Template.Date()
     - datetime.date
     - Date value. Also accepts ``datetime.datetime`` (auto-converts).
   * - Template.Time()
     - datetime.time
     - Time value.
   * - Template.Datetime()
     - datetime.datetime
     - DateTime value.

.. _set:

Set
---

.. code-block:: python

   Template.Set(item_template)

An ordered collection of items. Behaves like a list with extra helper methods.

.. code-block:: python

   # For simple types (strings)
   metadata.genres.add("Action")
   metadata.genres.add("Comedy")
   metadata.genres.clear()

   # For record types (Person, Review, etc.)
   role = metadata.roles.new()
   role.name = "John Actor"
   role.role = "Lead"

   # Find a record in the set
   found = metadata.roles.find(name="John Actor")

   # Iterate
   for genre in metadata.genres:
       Log(genre)

   # Index access
   first = metadata.genres[0]

   # Length
   count = len(metadata.genres)

   # Assign from list (clears and re-adds)
   metadata.genres = ["Action", "Comedy"]

add(value)
~~~~~~~~~~

Adds a new item to the set.

clear()
~~~~~~~

Removes all items.

new() → Record instance
~~~~~~~~~~~~~~~~~~~~~~~~

Creates and returns a new record item. Only available for record-type sets (e.g. :ref:`Person <person>`, :ref:`Review <review>`).

find(\*\*kwargs) → Record or None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finds the first item matching all keyword arguments.

**Supported operators:**

- ``len(set)`` — number of items
- ``set[index]`` — get item at index
- ``set[index] = value`` — set item at index
- ``for item in set`` — iterate

.. _map:

Map
---

.. code-block:: python

   Template.Map(item_template)

A keyed dictionary of items. Used for seasons, episodes, tracks, etc.

.. code-block:: python

   # Access by key
   episode = metadata.seasons['1'].episodes['5']
   episode.title = "Episode Title"

   # Check existence
   if '1' in metadata.seasons:
       ...

   # Iterate over keys
   for season_num in metadata.seasons:
       season = metadata.seasons[season_num]

   # Delete
   del metadata.seasons['1']

   # Validate keys (removes keys not in the valid set)
   metadata.seasons.validate_keys(['1', '2', '3'])

keys() → list
~~~~~~~~~~~~~~

Returns all keys.

validate_keys(valid_keys)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Removes keys not in the provided list.

**Supported operators:**

- ``map[key]`` — get item (auto-creates for record types)
- ``map[key] = value`` — set item
- ``del map[key]`` — delete item
- ``key in map`` — check existence
- ``len(map)`` — number of items
- ``for key in map`` — iterate over keys

.. _proxycontainer:

ProxyContainer
--------------

.. code-block:: python

   Template.ProxyContainer(*proxy_types)

A specialized :ref:`Map <map>` used for media assets (posters, art, banners, themes, thumbnails). Inherits from Map via DirectoryTemplate. Keys are typically URLs. Values must be :ref:`Proxy <proxy-objects>` objects.

.. code-block:: python

   # Set a poster from downloaded data
   metadata.posters['https://example.com/poster.jpg'] = Proxy.Media(
       HTTP.Request('https://example.com/poster.jpg').content,
       sort_order=1
   )

   # Set a poster from a preview (thumbnail) of remote data
   metadata.posters['url'] = Proxy.Preview(thumbnail_data, sort_order=2)

   # Remove outdated posters
   metadata.posters.validate_keys(['url1', 'url2'])

   # Check if a URL is already present
   if 'url' in metadata.posters:
       ...

   # Iterate over URLs
   for url in metadata.posters:
       ...

validate_keys(valid_keys)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Removes keys not in the provided list.

**Supported operators:**

- ``container[key] = Proxy.*`` — set a proxy object at the given key
- ``key in container`` — check existence
- ``for key in container`` — iterate over keys

.. _templateobjectcontainer:

Template.ObjectContainer
------------------------

.. code-block:: python

   Template.ObjectContainer(*classes)

A typed container for model interface objects, used for the ``extras`` attribute on metadata models. Parameterized by the accepted object classes (e.g. Trailer, DeletedScene, BehindTheScenes, etc.).

.. code-block:: python

   # Add a trailer extra
   trailer = TrailerObject(
       url='https://example.com/trailer',
       title='Official Trailer',
       year=2020,
       thumb='https://example.com/thumb.jpg'
   )
   metadata.extras.add(trailer)

add(obj)
~~~~~~~~

Adds an object to the container.

.. _link:

Link
----

.. code-block:: python

   Template.Link(model_class)

A reference to another model instance. Used for parent–child relationships (e.g. :ref:`Album <album>` → :ref:`Artist <artist>`).
