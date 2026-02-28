================================
Appendix: Info.plist Structure
================================

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>CFBundleIdentifier</key>
     <string>com.example.myplugin</string>
     <key>PlexPluginClass</key>
     <string>Agent</string>           <!-- Agent, Channel, Resource -->
     <key>PlexClientPlatforms</key>
     <string>*</string>
     <key>PlexMediaTypes</key>
     <string>1</string>               <!-- 1=Movie, 2=TV, 8=Artist, 9=Album, 13=Photo -->
     <key>PlexFrameworkVersion</key>
     <string>2</string>
     <key>PlexPluginCodePolicy</key>
     <string>Elevated</string>        <!-- Standard, Elevated -->
   </dict>
   </plist>


*This reference was generated from the Plex Plugin Framework v2 source code. All classes, methods and attributes are documented as they exist in the codebase. Some internal/private APIs are omitted for clarity.*
