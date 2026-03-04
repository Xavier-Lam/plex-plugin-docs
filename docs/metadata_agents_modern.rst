.. _modern-metadata-agents:

=============================
Modern Metadata Agent (V1+)
=============================

Modern metadata agents set ``version = 1`` (or higher) on the agent class. This
changes the search and update API compared to :ref:`legacy agents <legacy-metadata-agents>`.

Key differences from legacy agents:

- ``search()`` receives **four** positional parameters instead of three:
  ``(results, tree, hints, lang)``.
- The ``results`` container is an :ref:`ObjectContainer <objectcontainer>`
  instead of a :ref:`MediaContainer <mediacontainer>`.
- Search results use :ref:`SearchResult <searchresult>` objects (with more
  attributes) instead of :ref:`MetadataSearchResult <metadatasearchresult>`.
- ``update()`` is called at the **parent level** for hierarchical media
  (TV shows with seasons/episodes), with optional ``child_guid`` and 
  ``child_id`` parameters.

Agent class attributes are identical to legacy agents — see
:ref:`Agent Class Attributes <agent-class-attributes>` — except ``version``
must be set to ``1`` or higher.

.. _modern-search:

search(self, results, tree, hints, lang)
-----------------------------------------

Called when the server needs search results for a media item.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - results
     - :ref:`ObjectContainer <objectcontainer>`
     - Container for search results. Use ``results.add(SearchResult(...))``.
   * - tree
     - :ref:`MediaTree <mediatree>`
     - Full media tree built from the database, providing file/stream info.
   * - hints
     - :ref:`Media.Movie <media-movie>`, :ref:`Media.TV_Show <media-tv-show>`, :ref:`Media.Artist <media-artist>`, :ref:`Media.Album <media-album>`, etc.
     - Media hints object carrying scanner-detected information (name, year,
       etc.). The concrete type depends on the agent base class.
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
     - ``True`` if this is a partial/child match (i.e. a ``parentID`` was
       provided in the search request).
   * - primary
     - bool
     - ``True`` if this is the primary agent for the library.

Results are automatically sorted by ``score`` (descending) after the call.

**Example:**

.. code-block:: python

   def search(self, results, tree, hints, lang, manual=False):
       results.add(SearchResult(
           id='12345',
           name=hints.name,
           year=hints.year,
           score=100,
           thumb='https://example.com/thumb.jpg'
       ))

.. _modern-update:

update(self, metadata, media, lang, force=False)
--------------------------------------------------

Called when the server needs metadata for a matched item.

For hierarchical media types (TV shows), ``update()`` is called at the
**parent level** instead of once per individual item. For flat media types
(movies, tracks), the behaviour is the same as legacy agents.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - metadata
     - :ref:`Movie <movie>`, :ref:`TV_Show <tv-show>`, :ref:`Artist <artist>`, :ref:`Album <album>`, etc.
     - The metadata model instance to populate. The concrete type depends on
       the agent base class.
   * - media
     - :ref:`MediaTree <mediatree>`
     - The media tree with file info, parts, and streams.
   * - lang
     - str
     - Preferred :ref:`language code <language>`.
   * - force
     - bool
     - True if the user forced a metadata refresh.

Optional parameters (passed if the function signature accepts them):

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Type
     - Description
   * - child_guid
     - str
     - GUID of the specific child item that triggered this update. ``None``
       if the update was triggered for the top-level item itself. Only present
       for V1+ agents when PMS provides a parent GUID.
   * - child_id
     - str
     - Database ID of the specific child item. ``None`` if the update was
       triggered for the top-level item itself.
   * - periodic
     - bool
     - ``True`` if this update was triggered by a periodic refresh.
   * - prefs
     - dict
     - Library section preferences (music agents). Keys include:
       ``artistBio``, ``albumReviews``, ``popularTracks``, ``concerts``,
       ``genres``, ``albumPosters``; values are integers (0 or 1).

.. note::

   ``child_guid`` and ``child_id`` are only injected when PMS actually provides
   a parent GUID (i.e. when a child item triggers the update). If ``update()``
   is called for the top-level item itself (e.g. the show refresh button),
   these parameters may not be present. Always make them optional:
   ``def update(self, metadata, media, lang, force=False, child_guid=None, child_id=None)``.

.. _modern-parent-update:

Parent-Level Update
~~~~~~~~~~~~~~~~~~~~

When a child item (e.g. an episode) triggers an update on a V1+ agent, the
framework swaps the GUID and ID to the **parent** (e.g. the show) and passes
the original child values as ``child_guid`` and ``child_id``. This means:

- ``metadata`` is the parent model (e.g. ``TV_Show``), not the child.
- The agent is responsible for navigating to the child via
  ``metadata.seasons[...].episodes[...]``.

.. _modern-versioned-models:

Versioned Model Names
~~~~~~~~~~~~~~~~~~~~~~

Some agent types use different metadata models depending on the agent version:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25

   * - Agent Type
     - V0 Model
     - V2 Model
   * - :ref:`Agent.Artist <agent-artist>`
     - ``LegacyArtist``
     - ``ModernArtist``

Other agent types (Movies, TV_Shows, Album, Photos) use the same model name
regardless of version.

.. _modern-example:

Example Agent
--------------

.. code-block:: python

   class MyModernMovieAgent(Agent.Movies):
       name = 'My Modern Movie Agent'
       languages = [Locale.Language.English]
       primary_provider = True
       version = 1

       def search(self, results, tree, hints, lang, manual=False):
           results.add(SearchResult(
               id='12345',
               name=hints.name,
               year=hints.year,
               score=100,
               thumb='https://example.com/thumb.jpg'
           ))

       def update(self, metadata, media, lang, force=False):
           metadata.title = "Movie Title"
           metadata.year = 2020
           metadata.summary = "A great movie."
           metadata.genres.add("Action")

.. code-block:: python

   class MyModernTVAgent(Agent.TV_Shows):
       name = 'My Modern TV Agent'
       languages = [Locale.Language.English]
       primary_provider = True
       version = 1

       def search(self, results, tree, hints, lang, manual=False):
           results.add(SearchResult(
               id='tt1234567',
               name=hints.show,
               year=hints.year,
               score=95,
               thumb='https://example.com/show_thumb.jpg'
           ))

       def update(self, metadata, media, lang, force=False,
                  child_guid=None, child_id=None):
           metadata.title = "TV Show Title"
           metadata.summary = "A great show."

           # Navigate to seasons and episodes
           for season_index in media.seasons:
               season = metadata.seasons[season_index]
               season_media = media.seasons[season_index]
               for episode_index in season_media.episodes:
                   episode = season.episodes[episode_index]
                   episode.title = "Episode Title"
