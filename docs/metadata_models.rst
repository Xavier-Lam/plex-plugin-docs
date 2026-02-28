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
     - General tags.
   * - collections
     - Set[str]
     - Collection names.
   * - similar
     - Set[str]
     - Similar movie titles.
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
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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
     - Tags.
   * - collections
     - Set[str]
     - Collections.
   * - similar
     - Set[str]
     - Similar shows.
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
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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
     - Tags.
   * - thumbs
     - :ref:`ProxyContainer <proxycontainer>`
     - Episode thumbnails.
   * - extras
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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
     - Similar artists.
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
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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
     - Tags.
   * - extras
     - :ref:`Template.ObjectContainer <templateobjectcontainer>`
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

All extras inherit from VideoExtra and can be added to the ``extras`` :ref:`Template.ObjectContainer <templateobjectcontainer>` on metadata models.

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

Each extra type has the following attributes:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

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
   * - url
     - str
     - URL for the video (required for URL service resolution).
