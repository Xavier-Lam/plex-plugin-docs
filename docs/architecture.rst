==================
Architecture
==================

This chapter describes the internal architecture of the Plex Plugin Framework
v2. Understanding these internals is not required for writing plug-ins, but can
help when debugging or extending framework behaviour.

Framework Bootstrap
-------------------

When Plex Media Server loads a plug-in, it executes the following sequence:

1. **bootstrap.py** — The entry point. Parses command-line arguments (socket
   path, plug-in identifier, log path, etc.) and selects an interface
   (pipe-based or socket-based) for communicating with PMS.
2. **config.py** — Provides default configuration values (root path, bundle
   path, log level, etc.).
3. **FrameworkCore** (``core.py``) — Central orchestrator. Initialises all
   components and API kits in order:

   a. Reads the plug-in's ``Info.plist`` to determine ``CFBundleIdentifier``,
      ``PlexPluginClass``, and other settings.
   b. Creates components: storage, networking, caching, data persistence,
      runtime, messaging, services, etc.
   c. Creates the sandbox and API kits.
   d. Executes the plug-in code (``Contents/Code/__init__.py``) inside the
      sandbox.
   e. Calls ``Start()`` if defined.

Sandbox & Code Execution
--------------------------

Plug-in code runs inside a **RestrictedPython** sandbox. The sandbox:

- Restricts access to dangerous builtins (``open``, ``exec``, ``eval``,
  ``import``, ``__import__`` are replaced with safe wrappers).
- Provides a curated ``environment`` dict of global names that plug-in code
  can use (e.g. ``HTTP``, ``JSON``, ``Log``, ``Dict``, ``ObjectContainer``).
- Enforces a **code policy** that controls which APIs are accessible.

Files with the ``.pys`` extension are compiled with RestrictedPython. The
standard ``.py`` extension is used for the main ``Code/__init__.py`` entry
point, which is also restricted.

API Kit System
--------------

The framework uses an API Kit architecture for publishing globals into
the sandbox:

- **DevKit** — The root kit that contains all child kits.
- Each child kit (e.g. ``AgentKit``, ``ObjectKit``, ``NetworkKit``,
  ``ServiceKit``, ``TemplateKit``, etc.) ``publish()`` es names into the
  sandbox environment.
- For example, ``AgentKit`` publishes ``Agent`` (with sub-attributes
  ``Agent.Movies``, ``Agent.TV_Shows``, etc.) and ``MetadataSearchResult``.
  ``ObjectKit`` publishes ``ObjectContainer``, ``DirectoryObject``,
  ``VideoClipObject``, ``TrailerObject``, etc.

This is why plug-in code can reference ``HTTP.Request()``, ``JSON.ObjectFromString()``,
or ``Agent.Movies`` without any explicit ``import`` statements.

.. _policy-system:

Policy System
--------------

Security policies control what APIs and operations are available in different
contexts:

For plug-in code, the active policy is determined by the ``PlexPluginCodePolicy``
key in the bundle's ``Info.plist``. Services and model files always use their
dedicated policies regardless of this setting.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Policy
     - Description
   * - **Standard**
     - Default for most plug-ins. General-purpose API access.
   * - **Elevated**
     - Relaxed restrictions. Grants access to additional built-ins (``hasattr``,
       ``getattr``, ``setattr``, ``dir``, ``super``, ``type``), allows bundled
       native libraries, enables bundle-provided import whitelist extensions,
       and runs with elevated execution privileges.
       Set via ``PlexPluginCodePolicy = Elevated`` in ``Info.plist``.
   * - **ServicePolicy**
     - Applied to service code (``ServiceCode.pys``). Similar to Standard
       with service-specific additions.
   * - **ModelPolicy**
     - Applied to model template files (``.pym``).

Modelling System
-----------------

Metadata schemas are defined in ``.pym`` (Python Model) template files using a
declarative class-based syntax. The framework compiles these and generates
interface classes that plug-in code interacts with.

Key concepts:

- **ModelTemplate** — Base class for metadata models (e.g. ``Movie``,
  ``TV_Show``, ``Artist``). Templates use ``Template.*`` attribute types
  (:ref:`Template.String <template-types>`, :ref:`Template.Set <set>`,
  :ref:`Template.Map <map>`, etc.) to define their schema.
- **RecordTemplate** — Nested structure types (e.g. ``Person``, ``Review``,
  ``Chapter``).
- **generate_model_interface_class()** — Converts a ``ModelTemplate``
  into a concrete Python class that plug-in code can instantiate and populate.

For example, the ``Movie`` metadata model in ``common_models.pym`` defines
attributes like ``title = Template.String()``,
``genres = Template.Set(Template.String())``, etc. The framework generates a
``Movie`` interface class that agents interact with in ``update()``.

Framework Versions
-------------------

``Framework.bundle`` contains multiple version directories under
``Contents/Resources/Versions/``:

- **Version 0** — Legacy ``PMS.Plugin`` framework. Pipe-based communication.
- **Version 1** — Minor evolution of v0.
- **Version 2** — Complete rewrite. RestrictedPython sandbox, API kit system,
  component architecture, policy-based security. This is the version
  documented here.

The ``PlexFrameworkVersion`` key in ``Info.plist`` selects which version
directory is loaded. Modern plug-ins always use ``"2"``.

Inter-Plugin Communication
--------------------------

Plug-ins communicate with each other and with PMS via a messaging system.
The ``FrameworkCore.messaging`` component handles:

- Sending/receiving messages between plug-ins.
- Calling functions in other bundles (e.g. the System bundle).
- Service discovery — the System bundle provides the list of all available
  services to other plug-ins.

Source Code Layout
------------------

For reference, the framework v2 source code is organised as follows:

.. code-block:: text

   Framework.bundle/Contents/Resources/Versions/2/Python/Framework/
   ├── __init__.py
   ├── core.py              # FrameworkCore — central orchestrator
   ├── bootstrap.py          # Entry point
   ├── config.py             # Default configuration
   ├── code/                 # Sandbox, compiler, policy enforcement
   ├── components/           # Core components
   │   ├── runtime.py        # Plugin, Client, Platform, Prefs, etc.
   │   ├── services.py       # Service loading and invocation
   │   ├── networking.py     # HTTP client
   │   ├── caching.py        # Caching layer
   │   ├── storage.py        # File system abstraction
   │   ├── data.py           # Dict and Data persistence
   │   └── ...
   ├── handlers/             # HTTP request handlers
   │   ├── services.py       # Service API endpoints
   │   └── ...
   ├── api/                  # API kits
   │   ├── agentkit.py       # Agent.*, MediaObject, MediaTree
   │   ├── objectkit.py      # ObjectContainer, metadata objects
   │   ├── servicekit.py     # URLService, SearchService, etc.
   │   ├── templatekit.py    # Template.* types mapping
   │   ├── networkkit.py     # HTTP global
   │   └── ...
   ├── modelling/            # Model system
   │   ├── templates.py      # Template attribute types
   │   ├── objects.py        # Model interface generation
   │   └── ...
   ├── models/               # .pym model definitions
   │   ├── common_models.pym # Movie, TV_Show, Artist, etc.
   │   ├── extra_models.pym  # Video extra types
   │   ├── common_records.pym # Person, Review, Chapter, Concert
   │   └── ...
   └── policies/             # Security policies
       ├── standard.py
       ├── elevated.py
       └── ...
