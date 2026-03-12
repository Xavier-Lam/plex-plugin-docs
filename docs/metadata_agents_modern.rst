.. _modern-metadata-agents:

============================
Modern Metadata Agent (V2)
============================

Setting ``version = 2`` on an :ref:`Agent.Artist <agent-artist>` class activates the
modern (V2) agent path. The V2 path changes the ``search()`` signature and switches
the metadata model from ``LegacyArtist`` to ``ModernArtist``.

.. warning:: **This only works for** :ref:`Agent.Artist <agent-artist>`.

   Using ``version = 2`` (or any ``version > 0``) with ``Agent.Movies``,
   ``Agent.TV_Shows``, ``Agent.Album``, or ``Agent.Photos`` causes a ``KeyError``
   inside the framework when ``update()`` is dispatched. Search results will appear
   in the Plex UI, but ``update()`` is never called and no metadata is written.

   For all non-Artist agent types, keep ``version = 0``. You can still use modern
   search objects by adding a ``tree`` keyword argument to ``search()`` — see
   :ref:`Using the tree Parameter <search-with-tree>`.

.. note::

   V2 Artist agents only run ``search()`` for **manual** searches initiated by the
   user in the Plex UI. Automatic matching when media is first added to the library
   is not supported — the framework skips the search entirely and no results are
   returned.

.. _modern-agent-setup:

Agent Setup
-----------

A V2 Artist agent has the same :ref:`class attributes <agent-class-attributes>` as a
legacy agent, but sets ``version = 2``:

.. code-block:: python

   class MyArtistAgent(Agent.Artist):
       name = 'My Modern Artist Agent'
       languages = [Locale.Language.English]
       primary_provider = False
       contributes_to = ['com.plexapp.agents.plexmusic']
       version = 2

.. _modern-search:

search(self, results, tree, hints, lang)
-----------------------------------------

The V2 ``search()`` takes four positional parameters. The key difference from the
legacy ``(results, media, lang)`` pattern is that ``tree`` is the second positional
argument and the media hints object is called ``hints``.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - results
     - :ref:`ObjectContainer <objectcontainer>`
     - Container for search results. Add items with
       ``results.add(SearchResult(...))``.
   * - tree
     - :ref:`MediaTree <mediatree>`
     - Full media tree from the database, providing file and stream info.
   * - hints
     - :ref:`Media.Artist <media-artist>`
     - Scanner-detected information (artist name, album, track, etc.).
   * - lang
     - str
     - :ref:`Language code <language>` for the search.

Optional parameters (passed if the function signature accepts them):

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - manual
     - bool
     - ``True`` if the user initiated the search manually.
   * - partial
     - bool
     - ``True`` if this is a partial/child match (a ``parentID`` was provided
       in the search request).
   * - primary
     - bool
     - ``True`` if this is the primary agent for the library.

.. _modern-update:

update(self, metadata, media, lang)
-------------------------------------

Called when the server needs metadata for a matched item. For V2 Artist agents,
``update()`` is always called at the **artist level**. When a child item (an album
or track) triggers an update, the framework promotes the call to the parent artist
and passes the child's identifiers as keyword arguments.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - metadata
     - ``ModernArtist``
     - The artist metadata model to populate. V2 uses ``ModernArtist``
       instead of the ``LegacyArtist`` model used by V0 agents.
   * - media
     - :ref:`MediaTree <mediatree>`
     - The media tree with file and stream info.
   * - lang
     - str
     - Preferred :ref:`language code <language>`.

Optional parameters (passed if the function signature accepts them):

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - force
     - bool
     - ``True`` if the user forced a metadata refresh.
   * - child_guid
     - str
     - GUID of the child item that triggered this update, or ``None`` if the
       update was for the artist directly.
   * - child_id
     - str
     - Database ID of the child item, or ``None``.
   * - periodic
     - bool
     - ``True`` if this update was triggered by a periodic refresh.
   * - prefs
     - dict
     - Library section preferences. Keys: ``artistBios``, ``albumReviews``,
       ``popularTracks``, ``concerts``, ``genres``, ``albumPosters``;
       values are integers (0 or 1).

Always declare ``child_guid`` and ``child_id`` as optional with a default of
``None``:

.. code-block:: python

   def update(self, metadata, media, lang, child_guid=None, child_id=None):
       ...

When a child item triggers the update, ``metadata`` is still the top-level artist
model. To update a specific album or track, navigate via
``metadata.albums[child_guid]`` or ``metadata.albums[...].tracks[...]``.

.. _modern-example:

Example Agent
--------------

.. code-block:: python

   class MyArtistAgent(Agent.Artist):
       name = 'My Modern Artist Agent'
       languages = [Locale.Language.English]
       primary_provider = False
       contributes_to = ['com.plexapp.agents.plexmusic']
       version = 2

       def search(self, results, tree, hints, lang, manual=False):
           results.add(SearchResult(
               id='null',
               type='artist',
               parentName=hints.artist,
               score=100,
           ))

       def update(self, metadata, media, lang, child_guid=None, child_id=None):
           data = JSON.ObjectFromURL('https://api.example.com/artist/' + metadata.id)
           metadata.title = data['name']
           metadata.summary = data['bio']