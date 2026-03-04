===============
Channel Plugins
===============

A **Channel plugin** provides a browsable content hierarchy that Plex clients
display in the Channels section of the Plex interface. Unlike
:doc:`Metadata Agents <metadata_agents_legacy>` (which enrich existing library items)
or :ref:`URL Services <services>` (which resolve media URLs), a Channel plugin
acts as a self-contained content browser: it exposes a tree of menus and
playable items that users navigate just like a streaming app.

Channels were the original way to extend Plex with online video content. They
are *not* integrated into the Plex library — items returned by a Channel appear
only inside that Channel's own navigation hierarchy, not in Movies or TV Shows
sections.

.. note::

   Channel plugins are no longer officially supported in modern versions of Plex
   Media Server (Plex dropped the Channels section in the primary clients around
   2019–2020). However, the framework and some third-party clients (e.g. Plex
   HTPC) still support them, and the underlying routing and container APIs are
   also used internally.

How It Works
------------

A Channel plugin is essentially a lightweight HTTP server embedded inside PMS.
When Plex (or a Plex client) wants to display a Channel's content, it sends an
HTTP request to the plug-in's registered URL prefix. The plug-in returns an
:ref:`ObjectContainer <objectcontainer>` populated with typed objects, which
the client renders as navigable rows or grids.

The lifecycle for each user interaction is:

1. **Client requests a URL** — e.g. ``/video/myplugin``.
2. **PMS routes to the matching handler** — the function decorated with
   ``@handler`` or ``@route``.
3. **Handler returns an ObjectContainer** — containing directory items, media
   items, or both.
4. **Client renders the container** — the user picks an item, which triggers a
   new request to the URL in that item's ``key`` or :ref:`Callback <callback>`.

Info.plist for Channel Plugins
--------------------------------

A Channel plugin typically sets ``PlexPluginClass`` to ``Resource`` (or omits
it entirely). There is no dedicated ``Agent`` or metadata-handling class for
channels.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>CFBundleIdentifier</key>
     <string>com.example.myvideochannel</string>
     <key>PlexPluginClass</key>
     <string>Resource</string>
     <key>PlexFrameworkVersion</key>
     <string>2</string>
     <key>PlexClientPlatforms</key>
     <string>*</string>
     <key>PlexBundleVersion</key>
     <string>1.0.0</string>
   </dict>
   </plist>

See :ref:`Info.plist keys <plist-keys>` for the full key reference.

Bundle Structure
----------------

A minimal Channel plugin bundle looks like this:

.. code-block:: text

   MyChannel.bundle/
   └── Contents/
       ├── Info.plist
       ├── Code/
       │   └── __init__.py      # Plugin entry point — all handlers go here
       └── Resources/
           ├── icon-default.png  # Channel icon (shown in the Channels section)
           └── art-default.jpg   # Background art

Optional directories:

.. code-block:: text

       ├── DefaultPrefs.json     # Default preference values
       ├── Strings/              # Localisation string files
       ├── Libraries/Shared/     # Third-party Python libraries
       └── Services/             # URL Services for media resolution

Entry Point
-----------

The ``Code/__init__.py`` file is the plugin entry point. At minimum it must
register a top-level prefix handler using the :ref:`@handler <handler>` decorator:

.. code-block:: python

   @handler('/video/myvideochannel', 'My Video Channel',
            thumb='icon-default.png', art='art-default.jpg')
   def MainMenu():
       oc = ObjectContainer()
       oc.add(DirectoryObject(
           key=Callback(Browse, category='trending'),
           title='Trending',
           thumb=R('icon-default.png')
       ))
       oc.add(DirectoryObject(
           key=Callback(Browse, category='new'),
           title='New Releases'
       ))
       return oc

The prefix must start with one of the following path roots depending on the
type of content the channel serves:

- ``/video/`` — video channels
- ``/music/`` — music channels
- ``/photos/`` — photo channels
- ``/applications/`` — application/utility channels

The ``name``, ``thumb``, and ``art`` parameters to ``@handler`` are what Plex
clients show for the channel in the Channels browser.

Defining Sub-Pages
------------------

Sub-pages are functions decorated with :ref:`@route <route>`. The path must
start with the same prefix registered by ``@handler``.

.. code-block:: python

   @route('/video/myvideochannel/browse')
   def Browse(category):
       oc = ObjectContainer(title1='My Video Channel', title2=category.capitalize())
       items = FetchItems(category)
       for item in items:
           oc.add(VideoClipObject(
               url=item['page_url'],
               title=item['title'],
               summary=item['description'],
               thumb=item['thumb_url']
           ))
       return oc

Route path parameters use ``{name}`` placeholders and are passed as strings:

.. code-block:: python

   @route('/video/myvideochannel/show/{show_id}')
   def ShowDetail(show_id):
       ...

Linking Pages with Callback
-----------------------------

Use :ref:`Callback <callback>` to generate the ``key`` URL for any object
whose target is another route in your plugin. Callback serialises the function
reference and any keyword arguments into a URL that PMS will route back to
the function.

.. code-block:: python

   DirectoryObject(
       key=Callback(Browse, category='trending'),
       title='Trending'
   )

You can pass any JSON-serialisable values as keyword arguments. They arrive in
your handler as strings, so convert them as needed:

.. code-block:: python

   @route('/video/myvideochannel/episodes')
   def Episodes(show_id, page='1'):
       page = int(page)
       ...

Playable Media Items
---------------------

To make an item playable, use one of the media object types and set its ``url``
attribute to the page URL of the media item. PMS (via a matching
:ref:`URL Service <services>`) will resolve this URL to an actual playable
stream at playback time.

Common media object types for channels:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Type
     - When to use
   * - :ref:`VideoClipObject <videoclipobject>`
     - A standalone video clip or web video. Most web videos are ``VideoClipObject``.
   * - :ref:`MovieObject <movieobject>`
     - A feature film with full movie metadata (rating, cast, etc.).
   * - :ref:`EpisodeObject <episodeobject>`
     - A TV episode — use when the item has show/season/episode metadata.
   * - :ref:`TrackObject <trackobject>`
     - An audio track for music channels.

.. code-block:: python

   oc.add(VideoClipObject(
       url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
       title='Never Gonna Give You Up',
       summary='Official music video',
       duration=212000,             # milliseconds
       thumb='https://img.example.com/thumb.jpg'
   ))

The ``url`` is passed to a :ref:`URL Service <services>` whose
``URLPatterns`` matches it. The URL Service returns standardised media info
that PMS uses to play the item.

Indirect Playback
-----------------

When a media item's final URL is not known until the moment of playback (e.g.
it requires a fresh token, or a server selection step), mark the handler as
``@indirect``. This tells PMS to make a second request to the handler
immediately before playback, so it can resolve the live URL on demand.

.. code-block:: python

   @route('/video/myvideochannel/play')
   @indirect
   def PlayItem(item_id):
       stream_url = GetLiveStreamURL(item_id)
       return IndirectResponse(VideoClipObject(), key=stream_url)

Start Function
--------------

If ``Code/__init__.py`` defines a top-level ``Start()`` function, the framework
calls it once when the plugin is first loaded. Use it for one-time
initialisation tasks such as setting default HTTP headers or cache times:

.. code-block:: python

   def Start():
       HTTP.CacheTime = CACHE_1HOUR
       HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (compatible; MyChannel/1.0)'

``Start()`` runs before any handler is invoked. Keep it fast — avoid network
requests here.

User Preferences
----------------

Channels can expose user preferences through a
:ref:`DefaultPrefs.json <preferences>` file. A
:ref:`PrefsObject <prefsobject>` item can be added to any container to give
users a direct link to the preferences dialog:

.. code-block:: python

   oc.add(PrefsObject(title='Settings'))

Read preference values using :ref:`Prefs <prefs>`:

.. code-block:: python

   api_key = Prefs['api_key']

Pagination
----------

For large result sets, add a :ref:`NextPageObject <nextpageobject>` at the
end of the container pointing to the next page of results:

.. code-block:: python

   @route('/video/myvideochannel/browse')
   def Browse(category, page='1'):
       page = int(page)
       items, has_next = FetchPage(category, page)

       oc = ObjectContainer()
       for item in items:
           oc.add(VideoClipObject(url=item['url'], title=item['title']))

       if has_next:
           oc.add(NextPageObject(
               key=Callback(Browse, category=category, page=str(page + 1)),
               title='More...'
           ))
       return oc

Search
------

To support search inside your channel, add a
:ref:`SearchDirectoryObject <searchdirectoryobject>` that delegates to your
search handler:

.. code-block:: python

   oc.add(SearchDirectoryObject(
       key=Callback(SearchResults),
       title='Search',
       prompt='Search My Channel'
   ))

   @route('/video/myvideochannel/search')
   def SearchResults(query):
       oc = ObjectContainer(title2='Results for "%s"' % query)
       for item in SearchAPI(query):
           oc.add(VideoClipObject(url=item['url'], title=item['title']))
       return oc

Complete Example
----------------

.. code-block:: python

   # Code/__init__.py

   BASE_URL = 'https://api.example.com'

   def Start():
       HTTP.CacheTime = CACHE_1HOUR

   @handler('/video/examplechannel', 'Example Channel', thumb='icon-default.png')
   def MainMenu():
       oc = ObjectContainer()
       oc.add(DirectoryObject(
           key=Callback(VideoList, category='latest'),
           title='Latest Videos',
           thumb=R('icon-default.png')
       ))
       oc.add(SearchDirectoryObject(
           key=Callback(Search),
           title='Search',
           prompt='Search Example Channel'
       ))
       oc.add(PrefsObject(title='Settings'))
       return oc

   @route('/video/examplechannel/videos')
   def VideoList(category, page='1'):
       page = int(page)
       data = JSON.ObjectFromURL('%s/videos?cat=%s&page=%d' % (BASE_URL, category, page))
       oc = ObjectContainer(title2=category.capitalize())

       for item in data['items']:
           oc.add(VideoClipObject(
               url=item['page_url'],
               title=item['title'],
               summary=item.get('description', ''),
               thumb=item.get('thumb', ''),
               duration=item.get('duration_ms', 0)
           ))

       if data.get('has_next'):
           oc.add(NextPageObject(
               key=Callback(VideoList, category=category, page=str(page + 1))
           ))

       return oc

   @route('/video/examplechannel/search')
   def Search(query=''):
       oc = ObjectContainer(title2='Results for "%s"' % query)
       data = JSON.ObjectFromURL('%s/search?q=%s' % (BASE_URL, String.Quote(query, usePlus=True)))
       for item in data['results']:
           oc.add(VideoClipObject(
               url=item['page_url'],
               title=item['title']
           ))
       return oc
