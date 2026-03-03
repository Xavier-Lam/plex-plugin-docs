================================
Appendix: Info.plist Structure
================================

Every plug-in bundle must contain a ``Contents/Info.plist`` file using Apple's
property-list XML format. This file tells Plex Media Server how to load and
classify the plug-in.

Minimal Example
---------------

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>CFBundleIdentifier</key>
     <string>com.example.myplugin</string>
     <key>PlexPluginClass</key>
     <string>Agent</string>
     <key>PlexFrameworkVersion</key>
     <string>2</string>
   </dict>
   </plist>

.. _plist-keys:

Info.plist Keys Reference
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Key
     - Type
     - Description
   * - ``CFBundleIdentifier``
     - string
     - **Required.** A globally unique reverse-DNS identifier for the plug-in
       (e.g. ``com.plexapp.agents.imdb``). Used by the server to identify the
       bundle and for inter-plug-in messaging.
   * - ``PlexPluginClass``
     - string
     - The plug-in's class. Determines what the plug-in can do. See
       :ref:`PlexPluginClass values <plist-pluginclass>` below.
       Common values: ``Agent``, ``Resource``. Channel plug-ins typically
       omit this key or use ``Resource``.
   * - ``PlexFrameworkVersion``
     - string
     - The framework bootstrap version to use. Should always be ``"2"`` for
       modern plug-ins. This selects which ``Versions/`` sub-directory inside
       ``Framework.bundle`` is loaded — **it is not the same as the agent
       version attribute** (see :ref:`Agent version <agent-version-note>`).
   * - ``PlexClientPlatforms``
     - string
     - Comma-separated list of client platforms that can access this plug-in,
       or ``"*"`` for all platforms.
   * - ``PlexMediaTypes``
     - string
     - Comma-separated media type IDs this plug-in supports. See
       :ref:`Media type IDs <plist-mediatypes>` below.
   * - ``PlexPluginCodePolicy``
     - string
     - Security policy for the plug-in sandbox. ``Standard`` (default) —
       general purpose with normal restrictions. ``Elevated`` — relaxed
       restrictions, access to additional APIs (e.g. raw ``os`` path
       operations). Most plug-ins use ``Standard``.
   * - ``PlexPluginAPIExclusions``
     - array
     - List of API kit names to exclude from the sandbox. For example,
       ``["Agent"]`` prevents the plug-in from registering agents.
   * - ``PlexBundleVersion``
     - string
     - Version number of the plug-in bundle.

.. _plist-pluginclass:

PlexPluginClass Values
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Value
     - Description
   * - ``Agent``
     - A metadata agent plug-in. Provides :ref:`search() <agent-movies>`
       and :ref:`update() <agent-movies>` methods to fetch metadata for library
       items.
   * - ``Resource``
     - A resource plug-in that provides :ref:`services <services>` (URL
       Services, Search Services, Related Content Services) or shared code.
       Does not appear in the user interface directly.

.. note::

   The official documentation listed ``Content`` as a valid value for channel
   plug-ins, but in practice most channel plug-ins omit ``PlexPluginClass``
   entirely or use ``Resource``.

.. _plist-mediatypes:

PlexMediaTypes
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - ID
     - Media Type
   * - 1
     - Movie
   * - 2
     - TV Show
   * - 8
     - Artist (Music)
   * - 9
     - Album (Music)
   * - 13
     - Photo

.. _plist-services:

Service Keys
~~~~~~~~~~~~

Services can be declared in ``Info.plist`` using the *old-style* plist keys
below, or in a separate ``ServiceInfo.plist`` file using the *new-style*
format. See :ref:`services` for full details on both approaches.

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Key
     - Description
   * - ``PlexURLServices``
     - Dict of URL services. Each entry maps a service name to a dict with
       ``Identifier`` (str), ``URLPatterns`` (array of regex strings),
       and optionally ``TestURLs`` (array of test URL strings),
       ``Fallback`` (bool), ``SourceTitle`` (str), ``Priority`` (int).
   * - ``PlexSearchServices``
     - Dict of search services. Each entry maps a service name to a dict
       with ``Identifier`` (str) and optionally ``TestQueries`` (array),
       ``SourceTitle`` (str).
   * - ``PlexRelatedContentServices``
     - Dict of related content services. Each entry maps a service name to a
       dict with ``Identifier`` (str) and optionally ``SourceTitle`` (str).
       Must share an ``Identifier`` with the associated URL service.

**Old-style URL service example:**

.. code-block:: xml

   <key>PlexURLServices</key>
   <dict>
     <key>YouTube</key>
     <dict>
       <key>Identifier</key>
       <string>com.plexapp.plugins.youtube</string>
       <key>URLPatterns</key>
       <array>
         <string>http://.*youtube\.com/(watch)?\?v=</string>
       </array>
       <key>TestURLs</key>
       <array>
         <string>http://youtube.com/watch?v=vzKbhxY1eQU</string>
       </array>
     </dict>
   </dict>

Full Agent Example
------------------

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>CFBundleIdentifier</key>
     <string>com.plexapp.agents.mymovieagent</string>
     <key>PlexPluginClass</key>
     <string>Agent</string>
     <key>PlexClientPlatforms</key>
     <string>*</string>
     <key>PlexMediaTypes</key>
     <string>1</string>
     <key>PlexFrameworkVersion</key>
     <string>2</string>
     <key>PlexBundleVersion</key>
     <string>1.0.0</string>
   </dict>
   </plist>

Full Service Bundle Example
----------------------------

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>CFBundleIdentifier</key>
     <string>com.plexapp.plugins.myservice</string>
     <key>PlexPluginClass</key>
     <string>Resource</string>
     <key>PlexFrameworkVersion</key>
     <string>2</string>
     <key>PlexURLServices</key>
     <dict>
       <key>MyService</key>
       <dict>
         <key>Identifier</key>
         <string>com.plexapp.plugins.myservice</string>
         <key>URLPatterns</key>
         <array>
           <string>https?://.*example\.com/video/</string>
         </array>
       </dict>
     </dict>
     <key>PlexSearchServices</key>
     <dict>
       <key>MySearch</key>
       <dict>
         <key>Identifier</key>
         <string>com.plexapp.plugins.myservice</string>
       </dict>
     </dict>
   </dict>
   </plist>
