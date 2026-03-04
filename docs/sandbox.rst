.. _sandbox:

===========================
Sandbox & Code Execution
===========================

Plug-in code runs inside a **RestrictedPython** sandbox. The sandbox restricts
access to dangerous builtins, rewrites attribute/item access at compile time,
and enforces naming conventions. Understanding these restrictions is important
for writing working plug-in code.

.. _sandbox-overview:

How It Works
------------

The framework compiles all plug-in source files through
`RestrictedPython <https://pypi.org/project/RestrictedPython/>`_ before
execution. This process:

1. Parses the source code into an AST (Abstract Syntax Tree).
2. Walks the AST with a ``RestrictionMutator`` that rewrites or rejects
   dangerous constructs.
3. Compiles the mutated AST into bytecode.
4. Executes the bytecode in a curated environment dict that contains only
   approved globals (e.g. ``HTTP``, ``JSON``, ``Log``, ``Dict``,
   ``ObjectContainer``).

Files with the ``.pys`` extension (service code) and ``.pym`` extension (model
definitions) are compiled through the same pipeline. The standard ``.py``
extension is used for the main ``Code/__init__.py`` entry point, which is
also restricted.

.. _sandbox-file-types:

File Types
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Extension
     - Policy
     - Description
   * - ``.py``
     - StandardPolicy / ElevatedPolicy
     - Plug-in code (``Contents/Code/*.py``). The active policy depends on the
       ``PlexPluginCodePolicy`` key in ``Info.plist``.
   * - ``.pys``
     - ServicePolicy
     - Service code (``ServiceCode.pys``). Always compiled under
       ServicePolicy regardless of ``PlexPluginCodePolicy``.
   * - ``.pym``
     - ModelPolicy
     - Model template files. Always compiled under ModelPolicy.

.. _sandbox-naming:

Naming Restrictions
-------------------

RestrictedPython enforces strict naming rules at compile time:

- **Variables and attributes starting with** ``_`` **are forbidden.** Any
  variable name, function name, or attribute access that starts with an
  underscore will cause a compile error — for example, ``_my_var``,
  ``self._data``, ``obj.__dict__`` are all **illegal**.
- The bare name ``_`` is allowed (e.g. ``_ = some_value``).
- Names ending with ``__roles__`` are forbidden.
- The name ``printed`` is reserved by the sandbox for print capture.

**Allowed dunder names** (Standard / Cloud policy):

.. code-block:: text

   __init__, __call__, __str__, __repr__

**Additional dunder names** (Elevated policy only):

.. code-block:: text

   __getitem__, __getattr__, __getattribute__, __setitem__, __setattr__,
   __delitem__, __delattr__, __iter__, __len__, __name__,
   __eq__, __ne__, __enter__, __exit__

This means that under the Standard policy, you **cannot** define custom
``__getitem__``, ``__iter__``, ``__len__``, ``__eq__``, etc. on your classes.
Elevated policy allows these.

.. _sandbox-builtins:

Available Builtins
------------------

The sandbox provides a limited subset of Python 2.7 builtins. The following
tables list what is available and what is blocked.

Builtins from RestrictedPython ``safe_builtins``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These Python builtins are available in all policies:

.. code-block:: text

   False, None, True, abs, basestring, bool, callable, chr, cmp, complex,
   divmod, float, hash, hex, id, int, isinstance, issubclass, len, long,
   oct, ord, pow, range, repr, round, str, tuple, unichr, unicode,
   xrange, zip

All standard exception classes (``Exception``, ``ValueError``,
``TypeError``, etc.) are also available.

Additional builtins added by the sandbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sandbox extends ``safe_builtins`` with these names:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - ``object``
     - Python ``object`` base class.
   * - ``set``
     - Python ``set`` type.
   * - ``list``
     - Python ``list`` type.
   * - ``dict``
     - Python ``dict`` type.
   * - ``str``
     - Python ``str`` type.
   * - ``unicode``
     - Python ``unicode`` type.
   * - ``min``
     - Python ``min`` function.
   * - ``max``
     - Python ``max`` function.
   * - ``sorted``
     - Python ``sorted`` function.
   * - ``reversed``
     - Python ``reversed`` function.
   * - ``enumerate``
     - Python ``enumerate`` function.
   * - ``filter``
     - Python ``filter`` function.
   * - ``map``
     - Python ``map`` function.
   * - ``reduce``
     - Python ``reduce`` function.
   * - ``xrange``
     - Python ``xrange`` function.
   * - ``staticmethod``
     - Python ``staticmethod`` decorator.
   * - ``classmethod``
     - Python ``classmethod`` decorator.
   * - ``property``
     - Python ``property`` descriptor.
   * - ``hexlify``
     - ``binascii.hexlify`` for hex encoding.
   * - ``unhexlify``
     - ``binascii.unhexlify`` for hex decoding.
   * - ``Object``
     - Framework base object class.
   * - ``FrameworkException``
     - Framework exception class.

.. _sandbox-blocked-builtins:

Blocked Builtins
~~~~~~~~~~~~~~~~

These standard Python 2.7 builtins are **not available** in the sandbox:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Blocked Builtin
     - Reason
   * - ``any``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``all``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``sum``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``iter``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``frozenset``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``slice``
     - Not included in ``safe_builtins`` or sandbox additions.
   * - ``open``
     - Direct I/O not permitted.
   * - ``file``
     - Direct I/O not permitted.
   * - ``execfile``
     - Direct I/O not permitted.
   * - ``input``
     - Direct I/O not permitted.
   * - ``raw_input``
     - Direct I/O not permitted.
   * - ``compile``
     - Can produce new code objects.
   * - ``eval``
     - Code execution not permitted.
   * - ``globals``
     - Uncontrolled namespace access.
   * - ``locals``
     - Uncontrolled namespace access.
   * - ``vars``
     - Uncontrolled namespace access.
   * - ``dir``
     - Introspection not available (available in Elevated policy).
   * - ``hasattr``
     - Not available (available in Elevated policy).
   * - ``getattr``
     - Not available (available in Elevated policy).
   * - ``setattr``
     - Not available (available in Elevated policy).
   * - ``super``
     - Not available (available in Elevated policy).
   * - ``type``
     - Not available (available in Elevated policy).
   * - ``intern``
     - Low-level, not available.
   * - ``reload``
     - Module manipulation not permitted.
   * - ``buffer``
     - Low-level, not available.
   * - ``coerce``
     - Esoteric, not available.

.. note::

   Functions like ``any()``, ``all()``, ``sum()``, ``iter()``, and
   ``frozenset`` are legitimately useful but are simply not included in the
   sandbox. You can work around some of these — for example, use a ``for``
   loop with a flag instead of ``any()``, or use ``set`` instead of
   ``frozenset``.

.. _sandbox-statements:

Statement Restrictions
-----------------------

RestrictedPython blocks or rewrites several Python statements at compile time:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Statement
     - Restriction
   * - ``exec``
     - **Blocked entirely** — causes a compile error.
   * - ``yield``
     - **Blocked entirely** — generators cannot be used.
   * - ``a.b += c`` (augmented assignment on attributes)
     - **Blocked** — causes a compile error.
   * - ``a[b] += c`` (augmented assignment on subscripts)
     - **Blocked** — causes a compile error.
   * - ``n += 1`` (augmented assignment on names)
     - Allowed, but **only** ``+=`` is supported. All other augmented
       operators (``-=``, ``*=``, ``/=``, ``%=``, ``**=``, etc.) raise
       ``FrameworkException`` at runtime.

.. _sandbox-ast-rewrites:

AST Rewrites
~~~~~~~~~~~~~

RestrictedPython rewrites several constructs at compile time to route them
through guard functions. This is mostly transparent to plug-in code but
explains some unusual error messages:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Source Code
     - Rewritten To
     - Guard
   * - ``foo.bar``
     - ``_getattr_(foo, "bar")``
     - Attribute access proxy
   * - ``foo[bar]``
     - ``_getitem_(foo, bar)``
     - Item access proxy
   * - ``foo[bar] = x``
     - ``_write_(foo)[bar] = x``
     - Write guard
   * - ``a.b = c``
     - ``_write_(a).b = c``
     - Write guard
   * - ``del foo[bar]``
     - ``del _write_(foo)[bar]``
     - Write guard
   * - ``for x in expr:``
     - ``for x in _getiter_(expr):``
     - Iterator guard
   * - List/generator comprehensions
     - ``... for x in _getiter_(expr) ...``
     - Iterator guard
   * - ``print foo``
     - ``print >> _print, foo``
     - Print redirect
   * - ``f(*args, **kw)``
     - ``_apply_(f, *args, **kw)``
     - Apply guard

.. note::

   In the Plex sandbox, the write guard (``_write_``) is a passthrough
   (``lambda x: x``), so attribute/item assignment is not actually guarded
   at runtime — the compile-time restrictions are the primary enforcement.

.. note::

   On Windows, ``print`` output is **silently discarded**. On other platforms,
   it is written to stdout. Use ``Log.Debug()`` etc. for reliable logging.

.. _sandbox-imports:

Import System
--------------

The sandbox provides a custom ``__import__`` that works as follows:

1. Looks for a file matching ``<name>.<policy_ext>`` (e.g. ``mymodule.py``,
   ``mymodule.pys``, ``mymodule.pym``) in the plug-in's code path and any
   custom paths.
2. If found, compiles it through ``compile_restricted()`` as a
   ``RestrictedModule`` — subject to the same sandbox restrictions.
3. If not found, falls back to Python's standard ``__import__``.

The default module whitelist (modules that can be imported from Python's
standard library):

.. code-block:: text

   re, string, datetime, time

Under the **Elevated** policy, plug-ins can extend this whitelist via the
``PlexPluginModuleWhitelist`` key in ``Info.plist``.

Under the **Cloud** policy, only ``RestrictedModule`` imports and the
whitelisted modules above are permitted — all other standard library imports
are blocked.

.. _sandbox-policies:

Policy System
--------------

Security policies control what APIs and operations are available in different
contexts. For plug-in code, the active policy is determined by the
:ref:`PlexPluginCodePolicy <plist-keys>` key in ``Info.plist``. Services and
model files always use their dedicated policies regardless of this setting.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Policy
     - Description
   * - **Standard**
     - Default for most plug-ins. General-purpose API access with full
       RestrictedPython restrictions. Only ``__init__``, ``__call__``,
       ``__str__``, ``__repr__`` dunder names are allowed.
   * - **Elevated**
     - Relaxed restrictions. Grants access to additional built-ins
       (``hasattr``, ``getattr``, ``setattr``, ``dir``, ``super``, ``type``),
       allows bundled native libraries, enables bundle-provided import
       whitelist extensions, and runs with elevated execution privileges
       (more dunder names allowed at compile time).
       Set via ``PlexPluginCodePolicy = Elevated`` in ``Info.plist``.
   * - **ServicePolicy**
     - Applied to service code (``ServiceCode.pys``). Uses the ``.pys`` file
       extension.
   * - **ModelPolicy**
     - Applied to model template files (``.pym``).
   * - **CloudPolicy**
     - Most restrictive bundle policy. Blocks non-whitelisted imports,
       isolates cookies, disables HTTP caching and global HTTP auth.

.. _sandbox-elevated-details:

Elevated Policy Details
~~~~~~~~~~~~~~~~~~~~~~~~

When ``PlexPluginCodePolicy = Elevated`` is set in ``Info.plist``, the
following additional privileges are granted:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Privilege
     - Description
   * - Additional builtins
     - ``hasattr``, ``getattr``, ``setattr``, ``dir``, ``super``, ``type``
       are added to the sandbox environment.
   * - Extended dunder names
     - ``__getitem__``, ``__getattr__``, ``__getattribute__``,
       ``__setitem__``, ``__setattr__``, ``__delitem__``, ``__delattr__``,
       ``__iter__``, ``__len__``, ``__name__``, ``__eq__``, ``__ne__``,
       ``__enter__``, ``__exit__`` are allowed in variable/attribute names.
   * - Import whitelist extension
     - The plug-in can specify additional allowed module names via the
       ``PlexPluginModuleWhitelist`` key in ``Info.plist``.
   * - Bundled native libraries
     - The plug-in can ship native ``.so``/``.dll``/``.dylib`` files in
       ``Contents/Libraries/``.

.. _sandbox-summary-table:

Summary Table
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 15

   * - Restriction
     - Standard
     - Elevated
     - Cloud
   * - ``_``-prefix variables/attrs blocked
     - Yes (4 safe names)
     - Partial (18 safe names)
     - Yes (4 safe names)
   * - ``exec`` statement
     - Blocked
     - Blocked
     - Blocked
   * - ``yield`` statement
     - Blocked
     - Blocked
     - Blocked
   * - ``hasattr``/``getattr``/``setattr``/``dir``/``super``/``type``
     - Not available
     - Available
     - Not available
   * - ``any``/``all``/``sum``/``iter``/``frozenset``
     - Not available
     - Not available
     - Not available
   * - ``open``/``file``/``execfile``/``input``/``raw_input``
     - Not available
     - Not available
     - Not available
   * - ``compile``/``eval``/``globals``/``locals``/``vars``
     - Not available
     - Not available
     - Not available
   * - Only ``+=`` augmented assignment
     - Yes
     - Yes
     - Yes
   * - Augmented assign on attrs/items
     - Blocked
     - Blocked
     - Blocked
   * - Standard library imports
     - Allowed
     - Allowed + custom whitelist
     - Blocked (whitelist only)
   * - Bundled native libraries
     - No
     - Yes
     - No
