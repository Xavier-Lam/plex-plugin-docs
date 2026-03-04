========================
Overview
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
   │   ├── Info.plist            # Plugin metadata & configuration
   │   ├── DefaultPrefs.json     # Default preferences (see Preferences)
   │   ├── Code/
   │   │   └── __init__.py       # Plugin entry point
   │   ├── Resources/            # Images, strings, etc.
   │   ├── Helpers/              # External binaries (optional)
   │   │   ├── MacOSX/i386/
   │   │   ├── Windows/
   │   │   └── Linux/i386/
   │   ├── Libraries/
   │   │   └── Shared/           # Third-party Python libraries
   │   ├── Strings/              # Locale string files (optional)
   │   │
   │   │  # Old-style service directories (declared in Info.plist):
   │   ├── URL Services/         # URL service modules
   │   │   └── MyService/
   │   │       └── ServiceCode.pys
   │   ├── Search Services/      # Search service modules (optional)
   │   ├── Related Content Services/  # Related content modules (optional)
   │   │
   │   │  # New-style service directories (with ServiceInfo.plist):
   │   └── Services/
   │       ├── ServiceInfo.plist # Service declarations
   │       ├── URL/
   │       │   └── MyService/
   │       │       └── ServiceCode.pys
   │       ├── Search/
   │       ├── Related Content/
   │       ├── Shared Code/      # Shared .pys modules
   │       └── Resources/        # Service-specific resources

See :ref:`Service API <services>` for full details on how services are organised and configured.

.. _how-the-api-is-exposed:

How the API is Exposed
----------------------

The framework "publishes" API objects into the plug-in sandbox so they appear as global names. For example, ``HTTP``, ``JSON``, ``Log``, ``Dict``, ``ObjectContainer``, etc. are all globally available in plugin code without explicit imports. This document lists each API under its **global name** as seen from plugin code.
