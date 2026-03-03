==========================================
Container & Object Types (Modern API)
==========================================

The modern API uses typed objects instead of generic XML containers.

.. _objectcontainer:

ObjectContainer
---------------

The top-level container for returning content to the client.

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Attribute
     - Type
     - Description
   * - title1
     - str
     - Primary title (displayed in header).
   * - title2
     - str
     - Secondary title.
   * - art
     - str
     - Background art URL / resource path.
   * - view_group
     - str
     - Name of a registered view group.
   * - content
     - str
     - Content type hint (use :ref:`ContainerContent <containercontent>` constants).
   * - no_history
     - bool
     - Don't add to navigation history.
   * - replace_parent
     - bool
     - Replace the parent container in navigation.
   * - no_cache
     - bool
     - Disable caching of this container.
   * - mixed_parents
     - bool
     - Contains items from multiple parent containers.
   * - header
     - str
     - Header message text.
   * - message
     - str
     - Message body text.
   * - http_headers
     - dict
     - HTTP headers for requests.
   * - identifier
     - str
     - Plugin identifier override.
   * - source_title
     - str
     - Source title override.

Supported child types: :ref:`DirectoryObject <directoryobject>`, :ref:`NextPageObject <nextpageobject>`, :ref:`InputDirectoryObject <inputdirectoryobject>`, :ref:`PopupDirectoryObject <popupdirectoryobject>`, :ref:`PrefsObject <prefsobject>`, :ref:`SearchDirectoryObject <searchdirectoryobject>`, :ref:`PlaylistObject <playlistobject>`, :ref:`MovieObject <movieobject>`, :ref:`VideoClipObject <videoclipobject>`, :ref:`EpisodeObject <episodeobject>`, :ref:`SeasonObject <seasonobject>`, :ref:`TVShowObject <tvshowobject>`, :ref:`ArtistObject / AlbumObject / PhotoObject / PhotoAlbumObject <artistobject-albumobject>`, :ref:`TrackObject <trackobject>`, :ref:`MetadataItem <metadataitem>`, :ref:`SearchResult <searchresult>`, and all :ref:`Video Extra Types <video-extra-types>`.

add(obj)
~~~~~~~~

Adds an object to the container.

extend(obj_list)
~~~~~~~~~~~~~~~~

Adds all objects from a list or another container.

.. _directoryobject:

DirectoryObject
---------------

A navigable directory item.

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Attribute
     - Type
     - Description
   * - key
     - str or :ref:`Callback <callback>`
     - URL or callback to load contents.
   * - title
     - str
     - Display title.
   * - tagline
     - str
     - Subtitle / tagline.
   * - summary
     - str
     - Description.
   * - thumb
     - str
     - Thumbnail URL / resource path.
   * - art
     - str
     - Background art URL / resource path.
   * - duration
     - int
     - Duration (ms).

.. _nextpageobject:

NextPageObject
--------------

Represents a "More..." pagination link. Same attributes as :ref:`DirectoryObject <directoryobject>`. Only one instance can exist per container. If title is omitted, defaults to "More...".

.. _inputdirectoryobject:

InputDirectoryObject
--------------------

A directory that takes text input from the user.

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Attribute
     - Type
     - Description
   * - key
     - str or :ref:`Callback <callback>`
     - URL / callback, receives ``query`` parameter.
   * - title
     - str
     - Display title.
   * - prompt
     - str
     - Prompt text displayed to the user.
   * - summary
     - str
     - Description.
   * - thumb
     - str
     - Thumbnail.
   * - art
     - str
     - Background art.

.. _searchdirectoryobject:

SearchDirectoryObject
---------------------

A specialized search object that uses URL Services.

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - identifier
     - str
     - Plugin identifier (defaults to current plugin).
   * - name
     - str
     - Service name (defaults to first available).
   * - title
     - str
     - Display title.
   * - prompt
     - str
     - Prompt text.
   * - summary
     - str
     - Description.
   * - thumb
     - str
     - Thumbnail.
   * - art
     - str
     - Background art.
   * - term
     - str
     - Pre-filled search term.

.. _popupdirectoryobject:

PopupDirectoryObject
--------------------

A directory displayed as a popup overlay. Same attributes as :ref:`DirectoryObject <directoryobject>` (minus http_headers).

.. _prefsobject:

PrefsObject
-----------

Displays the plug-in's preferences dialog.

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Display title.
   * - summary
     - str
     - Description.
   * - thumb
     - str
     - Thumbnail.

.. _playlistobject:

PlaylistObject
--------------

A playlist directory object.

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Attribute
     - Type
     - Description
   * - key
     - str or :ref:`Callback <callback>`
     - URL / callback for playlist contents.
   * - title
     - str
     - Playlist title.
   * - summary
     - str
     - Description.
   * - thumb
     - str
     - Thumbnail.
   * - radio
     - bool
     - Whether this is a radio-style playlist.

.. _movieobject:

MovieObject
-----------

A browsable movie metadata item.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - url
     - str
     - URL for URL Service resolution.
   * - key
     - str
     - Metadata URL.
   * - rating_key
     - str
     - Unique rating key.
   * - title
     - str
     - Movie title.
   * - year
     - int
     - Year.
   * - originally_available_at
     - datetime.date
     - Release date.
   * - studio
     - str
     - Studio.
   * - tagline
     - str
     - Tagline.
   * - summary
     - str
     - Summary.
   * - content_rating
     - str
     - Content rating.
   * - duration
     - int
     - Duration (ms).
   * - rating
     - float
     - Rating.
   * - genres
     - list[str]
     - Genres.
   * - directors
     - list[:ref:`Person <person>`] or list[dict]
     - Directors.
   * - writers
     - list[Person] or list[dict]
     - Writers.
   * - roles
     - list[Person] or list[dict]
     - Cast.
   * - thumb
     - str
     - Thumbnail URL.
   * - source_icon
     - str
     - Source icon URL.
   * - items
     - list[:ref:`MediaObject <mediaobject>`]
     - Media objects (for direct play).

.. _videoclipobject:

VideoClipObject
---------------

Same as :ref:`MovieObject <movieobject>` but with type = clip.

.. _episodeobject:

EpisodeObject
-------------

Same as :ref:`MovieObject <movieobject>` plus the following additional attributes:

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Attribute
     - Type
     - Description
   * - show
     - str
     - Show title.
   * - season
     - int
     - Season number.
   * - index
     - int
     - Episode number.
   * - absolute_index
     - int
     - Absolute episode number.

.. _seasonobject:

SeasonObject
------------

Non-media container for a season hierarchy.

.. _tvshowobject:

TVShowObject
------------

Non-media container for a show hierarchy.

.. _trackobject:

TrackObject
-----------

A browsable audio track metadata item.

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Attribute
     - Type
     - Description
   * - url
     - str
     - URL for URL Service resolution.
   * - title
     - str
     - Track title.
   * - index
     - int
     - Track number.
   * - artist
     - str
     - Artist name.
   * - album
     - str
     - Album name.
   * - duration
     - int
     - Duration (ms).
   * - rating
     - float
     - Rating.
   * - items
     - list[:ref:`MediaObject <mediaobject>`]
     - Media objects.

.. _artistobject-albumobject:

ArtistObject / AlbumObject / PhotoObject / PhotoAlbumObject
-----------------------------------------------------------

Non-media containers corresponding to their model types.

.. _metadataitem:

MetadataItem
------------

A container representing a node in a hierarchical metadata tree. Used in agent version 1+
object trees returned from PMS; not typically constructed directly in plugin code.
``MetadataItem`` children can be nested recursively.

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Attribute
     - Type
     - Description
   * - type
     - str
     - Media type identifier (e.g. ``"movie"``, ``"show"``, ``"season"``, ``"episode"``).
   * - id
     - str
     - Unique identifier of the metadata item.
   * - title
     - str
     - Display title.
   * - guid
     - str
     - Plex GUID string (e.g. ``"com.plexapp.agents.imdb://tt1234567"``).
   * - index
     - str
     - Positional index (season number, episode number, etc.).
   * - originally_available_at
     - str
     - Original air / release date (ISO 8601 string).
   * - score
     - str
     - Match confidence score (0–100).
   * - thumb
     - str
     - Thumbnail URL.
   * - matched
     - str
     - ``"1"`` if the item has been matched to a metadata source, ``"0"`` otherwise.

.. _searchresult:

SearchResult
------------

Represents a single candidate returned by an agent ``search()`` in version 1+. Append
``SearchResult`` objects to the :ref:`ObjectContainer <objectcontainer>` passed as
``results``. ``SearchResult`` children can be nested to represent hierarchical results
(e.g. episodes within a show).

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Attribute
     - Type
     - Description
   * - type
     - str
     - Media type identifier.
   * - id
     - str
     - Source-specific identifier used to retrieve metadata in ``update()``.
   * - name
     - str
     - Display name of the result.
   * - guid
     - str
     - Plex GUID string.
   * - index
     - str
     - Positional index.
   * - year
     - str
     - Release year.
   * - score
     - str
     - Match confidence score (0–100).
   * - thumb
     - str
     - Thumbnail URL.
   * - matched
     - str
     - ``"1"`` if already matched.
   * - parentName
     - str
     - Name of the parent item (e.g. show title for an episode result).
   * - parentID
     - str
     - Identifier of the parent item.
   * - parentGUID
     - str
     - Plex GUID of the parent item.
   * - parentIndex
     - str
     - Index of the parent item (e.g. season number).

.. _mediaobject:

MediaObject
-----------

Represents a specific media version of a content item.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Attribute
     - Type
     - Description
   * - parts
     - list[:ref:`PartObject <partobject>`]
     - List of media parts.
   * - bitrate
     - int
     - Overall bitrate (kbps).
   * - aspect_ratio
     - str
     - Aspect ratio (e.g. ``"1.78"``).
   * - audio_channels
     - int
     - Number of audio channels.
   * - audio_codec
     - str
     - Audio codec (use :ref:`AudioCodec <audiocodec>` constants).
   * - video_codec
     - str
     - Video codec (use :ref:`VideoCodec <videocodec>` constants).
   * - video_resolution
     - str
     - Resolution (``"sd"``, ``"720"``, ``"1080"``, etc.).
   * - container
     - str
     - Container format (use :ref:`Container <container-constant>` constants).
   * - video_frame_rate
     - str
     - Frame rate.
   * - duration
     - int
     - Duration (ms).
   * - width
     - int
     - Video width (pixels).
   * - height
     - int
     - Video height (pixels).
   * - protocol
     - str
     - Protocol (``"hls"``, ``"rtmp"``, ``"webkit"``, ``"embed"``, etc.).
   * - optimized_for_streaming
     - bool
     - Whether the file is optimized for streaming.

.. _partobject:

PartObject
----------

Represents a single file/stream of a media object.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - key
     - str or URL type
     - URL to the media stream.
   * - file
     - str
     - Local file path.
   * - duration
     - int
     - Duration (ms).
   * - container
     - str
     - Container format.
   * - streams
     - list[:ref:`AudioStreamObject <audiostreamobject>` or :ref:`VideoStreamObject <videostreamobject>`]
     - Stream metadata.
   * - http_headers
     - dict
     - HTTP headers for the request.
   * - optimized_for_streaming
     - bool
     - Optimized for streaming flag.
   * - protocol
     - str
     - Protocol type.

.. _audiostreamobject:

AudioStreamObject
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Attribute
     - Type
     - Description
   * - codec
     - str
     - Audio codec.
   * - channels
     - int
     - Number of channels.
   * - bitrate
     - int
     - Bitrate (kbps).
   * - duration
     - int
     - Duration (ms).
   * - language_code
     - str
     - ISO :ref:`language code <language>`.
   * - sampling_rate
     - int
     - Sampling rate (Hz).
   * - index
     - str
     - Stream index (default: 1).
   * - selected
     - bool
     - Whether this stream is selected.

.. _videostreamobject:

VideoStreamObject
-----------------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - codec
     - str
     - Video codec.
   * - bitrate
     - int
     - Bitrate (kbps).
   * - width
     - int
     - Width (pixels).
   * - height
     - int
     - Height (pixels).
   * - duration
     - int
     - Duration (ms).
   * - frame_rate
     - str
     - Frame rate.
   * - level
     - str
     - Codec level.
   * - profile
     - str
     - Codec profile.
   * - index
     - str
     - Stream index (default: 0).
   * - selected
     - bool
     - Whether this stream is selected.

.. _webvideourl:

WebVideoURL
-----------

.. code-block:: text

   WebVideoURL(url) → str

Wraps a URL for WebKit playback.

.. _httplivestreamurl:

HTTPLiveStreamURL
-----------------

.. code-block:: text

   HTTPLiveStreamURL(url) → str

Wraps a URL for HLS playback.

.. _rtmpvideourl:

RTMPVideoURL
-------------

.. code-block:: text

   RTMPVideoURL(url, clip=None, live=False, swf_url=None, app=None, args=None, **kwargs) → str

Constructs an RTMP URL with parameters.

.. _windowsmediavideourl:

WindowsMediaVideoURL
---------------------

.. code-block:: text

   WindowsMediaVideoURL(url, width=None, height=None) → str

Wraps a URL for Silverlight / WMV playback.

.. _embedurl:

EmbedURL
--------

.. code-block:: text

   EmbedURL(url) → str

Wraps a URL for embedded player playback.

.. _indirectresponse:

IndirectResponse
----------------

.. code-block:: text

   IndirectResponse(cls, key, url=None, metadata_key=None, rating_key=None, metadata_kwargs={}, **kwargs)

Creates an indirect response container for deferred content resolution.
