======================
Metadata Model Types
======================

Metadata models define the structure of metadata that agents populate. Each model type has typed attributes defined using Template.\* types.

.. _movie:

Movie
-----

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Movie title.
   * - year
     - int
     - Release year.
   * - originally_available_at
     - datetime.date
     - Release date.
   * - studio
     - str
     - Production studio.
   * - tagline
     - str
     - Tagline.
   * - summary
     - str
     - Plot summary.
   * - trivia
     - str
     - Trivia text.
   * - quotes
     - str
     - Notable quotes.
   * - content_rating
     - str
     - Content rating (e.g. PG-13).
   * - content_rating_age
     - int
     - Content rating minimum age.
   * - duration
     - int
     - Duration in milliseconds.
   * - rating
     - float
     - Critic rating.
   * - audience_rating
     - float
     - Audience rating.
   * - rating_image
     - str
     - Rating image identifier.
   * - audience_rating_image
     - str
     - Audience rating image identifier.
   * - original_title
     - str
     - Original title (foreign language).
   * - title_sort
     - str
     - Sort title.
   * - genres
     - :ref:`Set <set>`\[str]
     - Genre tags.
   * - tags
     - Set[str]
     - Tag strings. Serialized as ``<Tag>`` elements.
   * - collections
     - Set[str]
     - Collection names.
   * - similar
     - Set[str]
     - Similar item names.
   * - writers
     - Set[:ref:`Person <person>`]
     - Writers.
   * - directors
     - Set[Person]
     - Directors.
   * - producers
     - Set[Person]
     - Producers.
   * - roles
     - Set[Person]
     - Cast members (actors).
   * - countries
     - Set[str]
     - Country names.
   * - reviews
     - Set[:ref:`Review <review>`]
     - Reviews.
   * - chapters
     - Set[:ref:`Chapter <chapter>`]
     - Chapter markers.
   * - posters
     - :ref:`ProxyContainer <proxycontainer>`
     - Poster images.
   * - art
     - ProxyContainer
     - Background art images.
   * - banners
     - ProxyContainer
     - Banner images.
   * - themes
     - ProxyContainer
     - Theme music files.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Video extras (Trailer, BehindTheScenes, etc.).

.. _tv-show:

TV_Show
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Show title.
   * - summary
     - str
     - Show summary.
   * - originally_available_at
     - datetime.date
     - First air date.
   * - content_rating
     - str
     - Content rating.
   * - studio
     - str
     - Network / studio.
   * - duration
     - int
     - Default episode duration (ms).
   * - rating
     - float
     - Rating.
   * - genres
     - :ref:`Set <set>`\[str]
     - Genres.
   * - tags
     - Set[str]
     - Tag strings. Serialized as ``<Tag>`` elements.
   * - collections
     - Set[str]
     - Collections.
   * - similar
     - Set[str]
     - Similar item names.
   * - roles
     - Set[:ref:`Person <person>`]
     - Cast members.
   * - countries
     - Set[str]
     - Countries.
   * - posters
     - :ref:`ProxyContainer <proxycontainer>`
     - Poster images.
   * - banners
     - ProxyContainer
     - Banner images.
   * - art
     - ProxyContainer
     - Background art.
   * - themes
     - ProxyContainer
     - Theme music.
   * - seasons
     - :ref:`Map <map>`\[:ref:`Season <season>`]
     - Seasons keyed by season number.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Video extras.

.. _season:

Season
------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Attribute
     - Type
     - Description
   * - summary
     - str
     - Season summary.
   * - posters
     - :ref:`ProxyContainer <proxycontainer>`
     - Season posters.
   * - banners
     - ProxyContainer
     - Season banners.
   * - art
     - ProxyContainer
     - Season art.
   * - episodes
     - :ref:`Map <map>`\[:ref:`Episode <episode>`]
     - Episodes keyed by episode number.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Video extras.

.. _episode:

Episode
-------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Episode title.
   * - summary
     - str
     - Episode summary.
   * - originally_available_at
     - datetime.date
     - Air date.
   * - rating
     - float
     - Rating.
   * - duration
     - int
     - Duration (ms).
   * - content_rating
     - str
     - Content rating.
   * - content_rating_age
     - int
     - Content rating minimum age.
   * - absolute_index
     - int
     - Absolute episode index (for absolute numbering).
   * - writers
     - :ref:`Set <set>`\[:ref:`Person <person>`]
     - Writers.
   * - directors
     - Set[Person]
     - Directors.
   * - producers
     - Set[Person]
     - Producers.
   * - guest_stars
     - Set[Person]
     - Guest stars.
   * - tags
     - Set[str]
     - Tag strings. Serialized as ``<Tag>`` elements.
   * - thumbs
     - :ref:`ProxyContainer <proxycontainer>`
     - Episode thumbnails.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Video extras.

.. _artist:

Artist
------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Artist name.
   * - title_sort
     - str
     - Sort name.
   * - summary
     - str
     - Biography.
   * - genres
     - :ref:`Set <set>`\[str]
     - Genres.
   * - moods
     - Set[str]
     - Moods.
   * - styles
     - Set[str]
     - Styles.
   * - similar
     - Set[str]
     - Similar item names.
   * - concerts
     - Set[:ref:`Concert <concert>`]
     - Concert info.
   * - countries
     - Set[str]
     - Countries.
   * - posters
     - :ref:`ProxyContainer <proxycontainer>`
     - Artist images.
   * - art
     - ProxyContainer
     - Background art.
   * - themes
     - ProxyContainer
     - Theme music.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Music videos, interviews, etc.

.. _album:

Album
-----

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Album title.
   * - title_sort
     - str
     - Sort title.
   * - summary
     - str
     - Album summary / review.
   * - studio
     - str
     - Record label.
   * - originally_available_at
     - datetime.date
     - Release date.
   * - available_at
     - datetime.date
     - Availability date.
   * - genres
     - :ref:`Set <set>`\[str]
     - Genres.
   * - styles
     - Set[str]
     - Styles.
   * - moods
     - Set[str]
     - Moods.
   * - album_format
     - Set[str]
     - Album format.
   * - album_type
     - Set[str]
     - Album type.
   * - producers
     - Set[:ref:`Person <person>`]
     - Producers.
   * - countries
     - Set[str]
     - Countries.
   * - posters
     - :ref:`ProxyContainer <proxycontainer>`
     - Album cover images.
   * - art
     - ProxyContainer
     - Background art.
   * - tracks
     - :ref:`Map <map>`\[:ref:`Track <track>`]
     - Tracks keyed by track index.

.. _track:

Track
-----

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Track title.
   * - title_sort
     - str
     - Sort title.
   * - original_title
     - str
     - Original title.
   * - rating
     - float
     - Rating.
   * - rating_count
     - int
     - Number of ratings.
   * - index
     - int
     - Track number.
   * - disc_index
     - int
     - Disc number.
   * - track_index
     - int
     - Track index.
   * - tempo
     - int
     - BPM / tempo.
   * - moods
     - :ref:`Set <set>`\[str]
     - Moods.
   * - tags
     - Set[str]
     - Tag strings. Serialized as ``<Tag>`` elements.
   * - extras
     - :ref:`extras container <video-extra-types>`
     - Music video extras.
   * - lyrics
     - :ref:`ProxyContainer <proxycontainer>`
     - Lyrics (supports Media, Remote, LocalFile proxies).

.. _photo:

Photo
-----

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Photo title.
   * - year
     - int
     - Year taken.
   * - originally_available_at
     - datetime.date
     - Date taken.
   * - studio
     - str
     - Studio / camera.
   * - tagline
     - str
     - Tagline.
   * - summary
     - str
     - Description.
   * - content_rating
     - str
     - Content rating.
   * - writers
     - :ref:`Set <set>`\[:ref:`Person <person>`]
     - Photographers.
   * - directors
     - Set[Person]
     - Directors.
   * - producers
     - Set[Person]
     - Producers.
   * - roles
     - Set[Person]
     - People in the photo.
   * - countries
     - Set[str]
     - Countries.

.. _photoalbum:

PhotoAlbum
----------

Same attributes as :ref:`Photo <photo>`.

.. _person:

Person
------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - name
     - str
     - Person's name.
   * - role
     - str
     - Role name (for cast).
   * - photo
     - str
     - URL to a photo.

.. _review:

Review
------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - author
     - str
     - Reviewer name.
   * - source
     - str
     - Review source.
   * - image
     - str
     - Image URL.
   * - link
     - str
     - Review URL.
   * - text
     - str
     - Review text.

.. _chapter:

Chapter
-------

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Chapter title.
   * - start_time_offset
     - int
     - Start time in milliseconds.
   * - end_time_offset
     - int
     - End time in milliseconds.

.. _concert:

Concert
-------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Concert title.
   * - venue
     - str
     - Venue name.
   * - city
     - str
     - City.
   * - country
     - str
     - Country.
   * - date
     - str
     - Date string.
   * - url
     - str
     - URL for more info.

.. _video-extra-types:

Video Extra Types
-----------------

The ``extras`` attribute on metadata models is an
:ref:`ObjectContainer <objectcontainer>`-based container that accepts extra
video objects. Each extra type is a class published as a global name in the
sandbox (e.g. ``TrailerObject``). All extras inherit from ``VideoExtra`` (a
``MetadataModel`` subclass).

.. note::

   The extras container is **not** a :ref:`Set <set>` or :ref:`Map <map>`.
   It is an ``ObjectContainerObject`` that wraps an :ref:`ObjectContainer <objectcontainer>`.
   Use ``metadata.extras.add(...)`` to add items.

.. warning::

   **Extras cannot be deserialized.** The framework's
   ``ObjectContainerObject._deserialize()`` is a no-op. This means that each
   time ``update()`` is called, the extras container starts **empty** — the
   agent must re-populate all extras on every update. Extras saved by one agent
   cannot be read back by the same or another agent in a subsequent call.

Extras per Media Type
~~~~~~~~~~~~~~~~~~~~~~

Not all metadata models support extras. The allowed extra types differ by
model:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Model
     - Allowed Extra Types
   * - :ref:`Movie <movie>`
     - TrailerObject, DeletedSceneObject, BehindTheScenesObject,
       InterviewObject, SceneOrSampleObject, FeaturetteObject, ShortObject,
       OtherObject
   * - :ref:`TV_Show <tv-show>`
     - *(same as Movie)*
   * - :ref:`Season <season>`
     - *(same as Movie)*
   * - :ref:`Episode <episode>`
     - *(same as Movie)*
   * - :ref:`Artist <artist>`
     - MusicVideoObject, LiveMusicVideoObject, LyricMusicVideoObject,
       InterviewObject, BehindTheScenesObject, ConcertVideoObject
   * - :ref:`Track <track>`
     - MusicVideoObject, LyricMusicVideoObject
   * - :ref:`Album <album>`
     - **No extras** — Album does not have an ``extras`` attribute.
   * - :ref:`Photo <photo>` / :ref:`PhotoAlbum <photoalbum>`
     - **No extras** — Photo and PhotoAlbum do not have an ``extras`` attribute.

**Adding extras:**

.. code-block:: python

   # Online extras — use 'url' to specify a URL (resolved via URL Services)
   trailer = TrailerObject(
       url='https://example.com/trailer.mp4',
       title='Official Trailer',
       year=2020,
       thumb='https://example.com/thumb.jpg'
   )
   metadata.extras.add(trailer)

   # Local file extras — use 'file' to specify a local file path
   # (Agent plug-ins only; LocalMedia.bundle uses this pattern)
   metadata.extras.add(BehindTheScenesObject(
       title='Making Of',
       file='/path/to/behindthescenes.mp4'
   ))

   # Music video extras on an Artist
   metadata.extras.add(MusicVideoObject(
       url='https://example.com/musicvideo.mp4',
       title='Song Title',
       album='Album Name'
   ))

Available extra types
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Type
     - relation_type
     - Description
   * - TrailerObject
     - trailer
     - Movie / show trailer.
   * - DeletedSceneObject
     - deletedScene
     - Deleted scene.
   * - BehindTheScenesObject
     - behindTheScenes
     - Behind-the-scenes footage.
   * - InterviewObject
     - interview
     - Interview clip.
   * - SceneOrSampleObject
     - sceneOrSample
     - Scene or sample clip.
   * - FeaturetteObject
     - featurette
     - Featurette.
   * - ShortObject
     - short
     - Short film.
   * - OtherObject
     - other
     - Other extra.
   * - MusicVideoObject
     - musicVideo
     - Music video.
   * - LiveMusicVideoObject
     - liveMusicVideo
     - Live music video.
   * - LyricMusicVideoObject
     - lyricMusicVideo
     - Lyric music video.
   * - ConcertVideoObject
     - concert
     - Concert video.

Common extra attributes
~~~~~~~~~~~~~~~~~~~~~~~~

All extra types accept these attributes in their constructor and as settable
properties. The first group comes from the ``MetadataObject`` superclass
(added by ``objectkit.py`` when publishing the class); the second group comes
from the ``VideoExtra`` model definition.

**Source attributes (MetadataObject):**

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Attribute
     - Type
     - Description
   * - url
     - str
     - Video URL. PMS resolves this via URL Services to obtain playable media.
       Optional — use either ``url`` or ``file``.
   * - file
     - str
     - Local file path to the video. **Agent plug-ins only** — this attribute
       is not available in channel (Resource) plug-ins. Optional — use either
       ``url`` or ``file``.
   * - http_headers
     - dict
     - HTTP headers to send when fetching the URL.
   * - user_agent
     - str
     - User-Agent header (shorthand).
   * - http_cookies
     - str
     - Cookie header (shorthand).
   * - deferred
     - bool
     - Whether this extra should be lazily resolved.
   * - source_icon
     - str
     - Icon for the source provider.

**Model attributes (VideoExtra):**

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Attribute
     - Type
     - Description
   * - title
     - str
     - Title.
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
   * - writers
     - :ref:`Set <set>`\[:ref:`Person <person>`]
     - Writers.
   * - directors
     - Set[Person]
     - Directors.
   * - producers
     - Set[Person]
     - Producers.
   * - roles
     - Set[Person]
     - Cast.
   * - countries
     - Set[str]
     - Countries.
   * - index
     - int
     - Sort index.
   * - thumb
     - str
     - Thumbnail URL (synthetic — written to XML but not persisted to model).
   * - art_url
     - str
     - Art URL (synthetic, serialized as ``art`` in XML).

Music-video extra attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``MusicVideoObject``, ``LiveMusicVideoObject``, ``LyricMusicVideoObject``, and
``ConcertVideoObject`` also support:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Attribute
     - Type
     - Description
   * - album
     - str
     - Associated album name (serialized as ``parentTitle`` in XML).
