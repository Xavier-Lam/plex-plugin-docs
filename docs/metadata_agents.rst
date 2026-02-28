==================
Metadata Agent API
==================

Metadata agents are classes that inherit from media type base classes and provide ``search()`` and ``update()`` methods.

.. _agent-movies:

Agent.Movies
------------

Base class for movie metadata agents.

.. _agent-tv-shows:

Agent.TV_Shows
--------------

Base class for TV show metadata agents.

.. _agent-artist:

Agent.Artist
------------

Base class for music artist metadata agents.

.. _agent-album:

Agent.Album
-----------

Base class for music album metadata agents.

.. _agent-photos:

Agent.Photos
-------------

Base class for photo metadata agents.

All agent base classes share the following class attributes:

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Attribute
     - Type
     - Default
     - Description
   * - name
     - str
     - 'Unnamed Agent'
     - Display name of the agent.
   * - languages
     - list[str]
     - []
     - List of supported :ref:`language codes <language>` (e.g. ``[Locale.Language.English]``).
   * - primary_provider
     - bool
     - True
     - Whether this agent is a primary metadata provider.
   * - contributes_to
     - list[str] or None
     - None
     - List of agent identifiers this agent contributes to.
   * - accepts_from
     - list[str] or None
     - None
     - List of agent identifiers this agent accepts contributions from.
   * - fallback_agent
     - str or None
     - None
     - Identifier of the agent to fall back to.
   * - persist_stored_files
     - bool
     - True
     - Whether to persist stored media files on disk.
   * - version
     - int
     - 0
     - Agent version (0 = legacy, 1+ = modern).

search(self, results, media, lang, manual=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Called when the server needs search results for a media item.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - results
     - :ref:`ObjectContainer <objectcontainer>` or :ref:`MediaContainer <mediacontainer>`
     - Container to append results to.
   * - media
     - :ref:`Media.Movie <media-movie>`, :ref:`Media.TV_Show <media-tv-show>`, :ref:`Media.Artist <media-artist>`, :ref:`Media.Album <media-album>`, etc.
     - Media object with hints from the scanner (name, year, etc.). The concrete type depends on the agent base class.
   * - lang
     - str
     - :ref:`Language code <language>` for the search.
   * - manual
     - bool
     - True if the user initiated the search manually.

For version 0 agents, append :ref:`MetadataSearchResult <metadatasearchresult>` objects:

.. code-block:: python

   results.Append(MetadataSearchResult(id='123', name='Movie Title', year=2020, score=95, lang=lang))

For version 1+ agents, append SearchResult objects to the :ref:`ObjectContainer <objectcontainer>`.

update(self, metadata, media, lang, force=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Called when the server needs metadata for a matched item.

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Parameter
     - Type
     - Description
   * - metadata
     - :ref:`Movie <movie>`, :ref:`TV_Show <tv-show>`, :ref:`Artist <artist>`, :ref:`Album <album>`, etc.
     - The metadata model instance to populate. The concrete type depends on the agent base class.
   * - media
     - :ref:`Media.Movie <media-movie>`, :ref:`Media.TV_Show <media-tv-show>`, :ref:`Media.Artist <media-artist>`, :ref:`Media.Album <media-album>`, etc.
     - The media object with file info, parts, and streams. Attributes from the underlying :ref:`MediaTree <mediatree>` (such as ``items``, ``seasons``, ``episodes``) are accessible directly on this object.
   * - lang
     - str
     - Preferred :ref:`language code <language>`.
   * - force
     - bool
     - True if the user forced a metadata refresh.

Example Agent
~~~~~~~~~~~~~

.. code-block:: python

   class MyMovieAgent(Agent.Movies):
       name = 'My Movie Agent'
       languages = [Locale.Language.English]
       primary_provider = True
       contributes_to = ['com.plexapp.agents.imdb']

       def search(self, results, media, lang):
           results.Append(MetadataSearchResult(
               id='12345', name=media.name, year=media.year, score=100, lang=lang
           ))

       def update(self, metadata, media, lang):
           metadata.title = "Movie Title"
           metadata.year = 2020
           metadata.summary = "A great movie."
           metadata.genres.add("Action")
           metadata.directors.new().name = "John Director"

           role = metadata.roles.new()
           role.name = "Jane Actor"
           role.role = "Lead"
           role.photo = "https://example.com/photo.jpg"

           metadata.posters['poster_url'] = Proxy.Media(
               HTTP.Request('https://example.com/poster.jpg').content
           )

.. _media-movie:

Media.Movie
-----------

Information provided by the scanner for a movie item.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - name
     - str
     - The detected movie name.
   * - year
     - str
     - The detected year.
   * - openSubtitlesHash
     - str
     - Hash for OpenSubtitles lookups.
   * - duration
     - str
     - Duration in milliseconds.
   * - id
     - str
     - Database ID.
   * - primary_metadata
     - :ref:`Movie <movie>` or None
     - Primary agent's existing metadata (if contributing to another agent).
   * - items
     - list[:ref:`MediaItem <mediaitem>`]
     - Media items with parts/streams.

.. _media-tv-show:

Media.TV_Show
-------------

Information provided by the scanner for a TV show item.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - show
     - str
     - The show name.
   * - season
     - str
     - Season number.
   * - episode
     - str
     - Episode number.
   * - name
     - str
     - Episode name.
   * - year
     - str
     - Year.
   * - duration
     - str
     - Duration.
   * - episodic
     - bool
     - Whether it's episodic (default True).
   * - seasons
     - dict[str, :ref:`MediaTree <mediatree>`]
     - Dict of season indices → season :ref:`MediaTree <mediatree>` objects.

Each season :ref:`MediaTree <mediatree>` has an ``episodes`` dict of episode indices → episode :ref:`MediaTree <mediatree>` objects. Each episode :ref:`MediaTree <mediatree>` has an ``items`` list of :ref:`MediaItem <mediaitem>`.

.. _media-artist:

Media.Artist
-------------

Information provided by the scanner for a music artist.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - artist
     - str
     - Artist name.
   * - album
     - str
     - Album name.
   * - track
     - str
     - Track name.
   * - index
     - str
     - Track index.
   * - albums
     - dict[str, :ref:`MediaTree <mediatree>`]
     - Dict of album GUIDs → album :ref:`MediaTree <mediatree>` objects.

.. _media-album:

Media.Album
------------

Information provided by the scanner for a music album.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - name
     - str
     - Album name.
   * - artist
     - str
     - Artist name.
   * - album
     - str
     - Album name.
   * - track
     - str
     - Track name.
   * - index
     - str
     - Track index.
   * - parentGUID
     - str
     - GUID of the parent artist.
   * - parent_metadata
     - :ref:`Artist <artist>` or None
     - Parent artist's metadata (loaded from ``parentGUID``).
   * - tracks
     - dict[str, :ref:`MediaTree <mediatree>`]
     - Dict of track indices → track :ref:`MediaTree <mediatree>` objects.

.. _mediatree:

MediaTree
---------

A tree structure representing the hierarchical media structure for a library item. Media objects (e.g. :ref:`Media.Movie <media-movie>`, :ref:`Media.TV_Show <media-tv-show>`) delegate attribute access to the underlying :ref:`MediaTree <mediatree>`, so properties like ``items``, ``seasons``, and ``episodes`` are accessible directly on the media object.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - items
     - list[:ref:`MediaItem <mediaitem>`]
     - Media items at this level of the tree.
   * - settings
     - dict
     - Settings associated with this item.
   * - children
     - list[:ref:`MediaTree <mediatree>`]
     - Child :ref:`MediaTree <mediatree>` nodes.

Additional attributes vary by level. For a TV show tree, season-level nodes have an ``episodes`` dict, and episode-level nodes have ``items``. All XML attributes from the server are also set as properties (e.g. ``title``, ``year``, ``originally_available_at``).

all_parts() → list[MediaPart]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a flat list of all :ref:`MediaPart <mediapart>` objects owned by this node and all its descendants.

.. _mediaitem:

MediaItem
---------

Represents a single media file grouping.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Attribute
     - Type
     - Description
   * - parts
     - list[:ref:`MediaPart <mediapart>`]
     - List of media parts.

.. _mediapart:

MediaPart
---------

Represents a single file of a media item.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Attribute
     - Type
     - Description
   * - file
     - str
     - Absolute path to the media file.
   * - hash
     - str
     - SHA1 hash of the file.
   * - size
     - long
     - File size in bytes.
   * - streams
     - list[:ref:`MediaStream <mediastream>`]
     - List of media streams.
   * - thumbs
     - dict-like
     - Directory for thumbnail images. Supports ``item in thumbs``, ``thumbs[item]`` (read bytes), ``thumbs[item] = data`` (write bytes).
   * - art
     - dict-like
     - Directory for art images. Same interface as thumbs.
   * - subtitles
     - dict-like
     - Directory for subtitles, keyed by :ref:`language code <language>`. Access: ``subtitles[lang_code][name] = Proxy.*``.
   * - openSubtitlesHash
     - str
     - OpenSubtitles hash (if available).

.. _mediastream:

MediaStream
-----------

Represents a single audio, video, or subtitle stream within a part.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Attribute
     - Type
     - Description
   * - type
     - long
     - Stream type: 1 = Video, 2 = Audio, 3 = Subtitle.
   * - index
     - long
     - Stream index.
   * - id
     - long
     - Stream ID.
   * - codec
     - str
     - Codec name.
   * - language
     - str
     - Language name.
   * - languageCode
     - str
     - ISO 639 :ref:`language code <language>`.

.. _metadatasearchresult:

MetadataSearchResult
--------------------

A search result returned during an agent ``search()`` call.

.. code-block:: python

   MetadataSearchResult(id, name=None, year=None, score=0, lang=None, thumb=None)

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Parameter
     - Type
     - Description
   * - id
     - str
     - Unique ID for this result.
   * - name
     - str
     - Display name.
   * - year
     - int
     - Release year.
   * - score
     - int
     - Match score (0–100).
   * - lang
     - str
     - :ref:`Language code <language>`.
   * - thumb
     - str
     - Thumbnail URL.
