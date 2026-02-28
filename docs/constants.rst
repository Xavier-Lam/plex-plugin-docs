=========
Constants
=========

.. _cache-time-constants:

Cache Time Constants
--------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Constant
     - Value
     - Description
   * - CACHE_1MINUTE
     - 60
     - 1 minute in seconds.
   * - CACHE_1HOUR
     - 3600
     - 1 hour.
   * - CACHE_1DAY
     - 86400
     - 1 day.
   * - CACHE_1WEEK
     - 604800
     - 1 week.
   * - CACHE_1MONTH
     - 2592000
     - 30 days.

.. _clientplatform:

ClientPlatform
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - ClientPlatform.MacOSX
     - MacOSX
   * - ClientPlatform.Linux
     - Linux
   * - ClientPlatform.Windows
     - Windows
   * - ClientPlatform.iOS
     - iOS
   * - ClientPlatform.Android
     - Android
   * - ClientPlatform.LGTV
     - LGTV
   * - ClientPlatform.Roku
     - Roku

.. _protocol:

Protocol
--------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - Protocol.DASH
     - dash
   * - Protocol.HTTP
     - http
   * - Protocol.HLS
     - hls
   * - Protocol.RTMP
     - rtmp
   * - Protocol.Shoutcast
     - shoutcast (legacy)
   * - Protocol.WebKit
     - webkit (legacy)
   * - Protocol.HTTPLiveStreaming
     - http-live-streaming (legacy)

.. _audiocodec:

AudioCodec
----------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - AudioCodec.AAC
     - aac
   * - AudioCodec.DCA
     - dca
   * - AudioCodec.MP3
     - mp3
   * - AudioCodec.WMA
     - wma
   * - AudioCodec.WMAP
     - wmap
   * - AudioCodec.VORBIS
     - vorbis
   * - AudioCodec.FLAC
     - flac

.. _videocodec:

VideoCodec
----------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - VideoCodec.H263
     - h263
   * - VideoCodec.H264
     - h264
   * - VideoCodec.VP6
     - vp6
   * - VideoCodec.WVC1
     - wvc1
   * - VideoCodec.DIVX
     - divx
   * - VideoCodec.DIV4
     - div4
   * - VideoCodec.XVID
     - xvid
   * - VideoCodec.THEORA
     - theora

.. _container-constant:

Container (Constant)
--------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - Container.MKV
     - mkv
   * - Container.MP4
     - mp4
   * - Container.MPEGTS
     - mpegts
   * - Container.MOV
     - mov
   * - Container.AVI
     - avi
   * - Container.MP3
     - mp3
   * - Container.OGG
     - ogg
   * - Container.FLAC
     - flac
   * - Container.FLV
     - flv

.. _containercontent:

ContainerContent
----------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Constant
     - Value
     - Description
   * - ContainerContent.Secondary
     - secondary
     - Secondary content.
   * - ContainerContent.Mixed
     - mixed
     - Mixed content types.
   * - ContainerContent.Genres
     - genre
     - Genre listing.
   * - ContainerContent.Playlists
     - playlist
     - Playlist listing.
   * - ContainerContent.Albums
     - album
     - Album listing.
   * - ContainerContent.Tracks
     - track
     - Track listing.
   * - ContainerContent.GenericVideos
     - video
     - Video listing.
   * - ContainerContent.Episodes
     - episode
     - Episode listing.
   * - ContainerContent.Movies
     - movie
     - Movie listing.
   * - ContainerContent.Seasons
     - season
     - Season listing.
   * - ContainerContent.Shows
     - show
     - Show listing.
   * - ContainerContent.Artists
     - artist
     - Artist listing.

.. _viewtype:

ViewType
--------

Legacy view type constants.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - ViewType.Grid
     - grid
   * - ViewType.List
     - list

.. _summarytexttype:

SummaryTextType
---------------

Legacy summary text constants.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - SummaryTextType.NoSummary
     - 0
   * - SummaryTextType.Short
     - 1
   * - SummaryTextType.Long
     - 2

.. _streamtype:

StreamType
----------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Value
   * - StreamType.Video
     - 1
   * - StreamType.Audio
     - 2
   * - StreamType.Subtitle
     - 3
