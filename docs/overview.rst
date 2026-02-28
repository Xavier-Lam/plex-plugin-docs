========================
Overview & Architecture
========================

The Plex Plugin Framework (v2) is a Python 2.7 framework that provides a sandboxed environment for plug-in code. Plug-ins run inside Plex Media Server and can serve as:

- **Channels** — provide browsable content via :ref:`ObjectContainer <objectcontainer>` / :ref:`DirectoryObject <directoryobject>` hierarchies.
- **Metadata Agents** — fetch and store metadata (posters, summaries, cast, etc.) for media items.
- **URL Services** — resolve playable media URLs from website links.

.. _bundle-structure:

Bundle Structure
----------------

.. code-block:: text

   MyPlugin.bundle/
   ├── Contents/
   │   ├── Info.plist            # Plugin metadata (identifier, title, etc.)
   │   ├── DefaultPrefs.json     # Default preferences
   │   ├── Code/
   │   │   └── __init__.py       # Plugin entry point
   │   ├── Resources/            # Images, strings, etc.
   │   ├── Helpers/              # External binaries (optional)
   │   │   ├── MacOSX/i386/
   │   │   ├── Windows/
   │   │   └── Linux/i386/
   │   ├── Libraries/
   │   │   └── Shared/           # Third-party Python libraries
   │   └── Services/             # URL Services (optional)
   │       └── MyService/
   │           └── ServiceCode.pys

.. _how-the-api-is-exposed:

How the API is Exposed
----------------------

The framework "publishes" API objects into the plug-in sandbox so they appear as global names. For example, ``HTTP``, ``JSON``, ``Log``, ``Dict``, ``ObjectContainer``, etc. are all globally available in plugin code without explicit imports. This document lists each API under its **global name** as seen from plugin code.
