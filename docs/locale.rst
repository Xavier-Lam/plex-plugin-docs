==========================
Locale & Localization API
==========================

.. _locale:

Locale
------

Localization support.

DefaultLocale → str
~~~~~~~~~~~~~~~~~~~~

Default locale (get / set), e.g. ``"en-us"``.

CurrentLocale → str or None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Locale of the current request.

Geolocation → str
~~~~~~~~~~~~~~~~~~

Country code via IP geolocation (e.g. ``"US"``).

.. _language:

Language
~~~~~~~~

Object containing language code constants. Common values:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Code
   * - Locale.Language.English
     - en
   * - Locale.Language.French
     - fr
   * - Locale.Language.German
     - de
   * - Locale.Language.Spanish
     - es
   * - Locale.Language.Italian
     - it
   * - Locale.Language.Japanese
     - ja
   * - Locale.Language.Chinese
     - zh
   * - Locale.Language.Korean
     - ko
   * - Locale.Language.Russian
     - ru
   * - Locale.Language.Portuguese
     - pt
   * - Locale.Language.Swedish
     - sv
   * - Locale.Language.Norwegian
     - no
   * - Locale.Language.Danish
     - da
   * - Locale.Language.Dutch
     - nl
   * - Locale.Language.Hungarian
     - hu
   * - Locale.Language.Czech
     - cs
   * - Locale.Language.Polish
     - pl
   * - Locale.Language.Greek
     - el
   * - Locale.Language.Turkish
     - tr
   * - Locale.Language.Finnish
     - fi
   * - Locale.Language.Hebrew
     - he
   * - Locale.Language.Croatian
     - hr
   * - Locale.Language.Slovak
     - sk
   * - Locale.Language.Thai
     - th
   * - Locale.Language.Vietnamese
     - vi
   * - Locale.Language.Latvian
     - lv
   * - Locale.Language.Lithuanian
     - lt
   * - ...
     - *(and many more ISO 639-1 codes)*

CountryCodes
~~~~~~~~~~~~

Object containing country code constants.

.. _l-func:

L
-

.. code-block:: text

   L(key) → str

Retrieves a localized string by key. Alias for ``Locale.LocalString(key)``.

.. _f-func:

F
-

.. code-block:: text

   F(key, *args) → str

Retrieves and formats a localized string. Alias for ``Locale.LocalStringWithFormat(key, *args)``.

Localization String Files
~~~~~~~~~~~~~~~~~~~~~~~~~

Place string files in ``Contents/Strings/<locale>.json``:

.. code-block:: json

   {
     "greeting": "Hello, World!",
     "item_count": "Found %d items"
   }

Usage:

.. code-block:: python

   title = L('greeting')
   subtitle = F('item_count', len(items))
