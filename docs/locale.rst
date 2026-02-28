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

Object containing language code constants. All values:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Constant
     - Code
   * - Locale.Language.Unknown
     - xx
   * - Locale.Language.Afar
     - aa
   * - Locale.Language.Abkhazian
     - ab
   * - Locale.Language.Afrikaans
     - af
   * - Locale.Language.Akan
     - ak
   * - Locale.Language.Albanian
     - sq
   * - Locale.Language.Amharic
     - am
   * - Locale.Language.Arabic
     - ar
   * - Locale.Language.Aragonese
     - an
   * - Locale.Language.Armenian
     - hy
   * - Locale.Language.Assamese
     - as
   * - Locale.Language.Avaric
     - av
   * - Locale.Language.Avestan
     - ae
   * - Locale.Language.Aymara
     - ay
   * - Locale.Language.Azerbaijani
     - az
   * - Locale.Language.Bashkir
     - ba
   * - Locale.Language.Bambara
     - bm
   * - Locale.Language.Basque
     - eu
   * - Locale.Language.Belarusian
     - be
   * - Locale.Language.Bengali
     - bn
   * - Locale.Language.Bihari
     - bh
   * - Locale.Language.Bislama
     - bi
   * - Locale.Language.Bosnian
     - bs
   * - Locale.Language.Breton
     - br
   * - Locale.Language.Bulgarian
     - bg
   * - Locale.Language.Burmese
     - my
   * - Locale.Language.Catalan
     - ca
   * - Locale.Language.Chamorro
     - ch
   * - Locale.Language.Chechen
     - ce
   * - Locale.Language.Chinese
     - zh
   * - Locale.Language.ChurchSlavic
     - cu
   * - Locale.Language.Chuvash
     - cv
   * - Locale.Language.Cornish
     - kw
   * - Locale.Language.Corsican
     - co
   * - Locale.Language.Cree
     - cr
   * - Locale.Language.Czech
     - cs
   * - Locale.Language.Danish
     - da
   * - Locale.Language.Divehi
     - dv
   * - Locale.Language.Dutch
     - nl
   * - Locale.Language.Dzongkha
     - dz
   * - Locale.Language.English
     - en
   * - Locale.Language.Esperanto
     - eo
   * - Locale.Language.Estonian
     - et
   * - Locale.Language.Ewe
     - ee
   * - Locale.Language.Faroese
     - fo
   * - Locale.Language.Fijian
     - fj
   * - Locale.Language.Finnish
     - fi
   * - Locale.Language.French
     - fr
   * - Locale.Language.Frisian
     - fy
   * - Locale.Language.Fulah
     - ff
   * - Locale.Language.Georgian
     - ka
   * - Locale.Language.German
     - de
   * - Locale.Language.Gaelic
     - gd
   * - Locale.Language.Irish
     - ga
   * - Locale.Language.Galician
     - gl
   * - Locale.Language.Manx
     - gv
   * - Locale.Language.Greek
     - el
   * - Locale.Language.Guarani
     - gn
   * - Locale.Language.Gujarati
     - gu
   * - Locale.Language.Haitian
     - ht
   * - Locale.Language.Hausa
     - ha
   * - Locale.Language.Hebrew
     - he
   * - Locale.Language.Herero
     - hz
   * - Locale.Language.Hindi
     - hi
   * - Locale.Language.HiriMotu
     - ho
   * - Locale.Language.Croatian
     - hr
   * - Locale.Language.Hungarian
     - hu
   * - Locale.Language.Igbo
     - ig
   * - Locale.Language.Icelandic
     - is
   * - Locale.Language.Ido
     - io
   * - Locale.Language.SichuanYi
     - ii
   * - Locale.Language.Inuktitut
     - iu
   * - Locale.Language.Interlingue
     - ie
   * - Locale.Language.Interlingua
     - ia
   * - Locale.Language.Indonesian
     - id
   * - Locale.Language.Inupiaq
     - ik
   * - Locale.Language.Italian
     - it
   * - Locale.Language.Javanese
     - jv
   * - Locale.Language.Japanese
     - ja
   * - Locale.Language.Kalaallisut
     - kl
   * - Locale.Language.Kannada
     - kn
   * - Locale.Language.Kashmiri
     - ks
   * - Locale.Language.Kanuri
     - kr
   * - Locale.Language.Kazakh
     - kk
   * - Locale.Language.Khmer
     - km
   * - Locale.Language.Kikuyu
     - ki
   * - Locale.Language.Kinyarwanda
     - rw
   * - Locale.Language.Kirghiz
     - ky
   * - Locale.Language.Komi
     - kv
   * - Locale.Language.Kongo
     - kg
   * - Locale.Language.Korean
     - ko
   * - Locale.Language.Kuanyama
     - kj
   * - Locale.Language.Kurdish
     - ku
   * - Locale.Language.Lao
     - lo
   * - Locale.Language.Latin
     - la
   * - Locale.Language.Latvian
     - lv
   * - Locale.Language.Limburgan
     - li
   * - Locale.Language.Lingala
     - ln
   * - Locale.Language.Lithuanian
     - lt
   * - Locale.Language.Luxembourgish
     - lb
   * - Locale.Language.LubaKatanga
     - lu
   * - Locale.Language.Ganda
     - lg
   * - Locale.Language.Macedonian
     - mk
   * - Locale.Language.Marshallese
     - mh
   * - Locale.Language.Malayalam
     - ml
   * - Locale.Language.Maori
     - mi
   * - Locale.Language.Marathi
     - mr
   * - Locale.Language.Malay
     - ms
   * - Locale.Language.Malagasy
     - mg
   * - Locale.Language.Maltese
     - mt
   * - Locale.Language.Moldavian
     - mo
   * - Locale.Language.Mongolian
     - mn
   * - Locale.Language.Nauru
     - na
   * - Locale.Language.Navajo
     - nv
   * - Locale.Language.SouthNdebele
     - nr
   * - Locale.Language.NorthNdebele
     - nd
   * - Locale.Language.Ndonga
     - ng
   * - Locale.Language.Nepali
     - ne
   * - Locale.Language.NorwegianNynorsk
     - nn
   * - Locale.Language.NorwegianBokmal
     - nb
   * - Locale.Language.Norwegian
     - no
   * - Locale.Language.Chichewa
     - ny
   * - Locale.Language.Occitan
     - oc
   * - Locale.Language.Ojibwa
     - oj
   * - Locale.Language.Oriya
     - or
   * - Locale.Language.Oromo
     - om
   * - Locale.Language.Ossetian
     - os
   * - Locale.Language.Panjabi
     - pa
   * - Locale.Language.Persian
     - fa
   * - Locale.Language.Pali
     - pi
   * - Locale.Language.Polish
     - pl
   * - Locale.Language.Portuguese
     - pt
   * - Locale.Language.Pushto
     - ps
   * - Locale.Language.Quechua
     - qu
   * - Locale.Language.RaetoRomance
     - rm
   * - Locale.Language.Romanian
     - ro
   * - Locale.Language.Rundi
     - rn
   * - Locale.Language.Russian
     - ru
   * - Locale.Language.Sango
     - sg
   * - Locale.Language.Sanskrit
     - sa
   * - Locale.Language.Serbian
     - sr
   * - Locale.Language.Sinhalese
     - si
   * - Locale.Language.Slovak
     - sk
   * - Locale.Language.Slovenian
     - sl
   * - Locale.Language.Sami
     - se
   * - Locale.Language.Samoan
     - sm
   * - Locale.Language.Shona
     - sn
   * - Locale.Language.Sindhi
     - sd
   * - Locale.Language.Somali
     - so
   * - Locale.Language.Sotho
     - st
   * - Locale.Language.Spanish
     - es
   * - Locale.Language.Sardinian
     - sc
   * - Locale.Language.Swati
     - ss
   * - Locale.Language.Sundanese
     - su
   * - Locale.Language.Swahili
     - sw
   * - Locale.Language.Swedish
     - sv
   * - Locale.Language.Tahitian
     - ty
   * - Locale.Language.Tamil
     - ta
   * - Locale.Language.Tatar
     - tt
   * - Locale.Language.Telugu
     - te
   * - Locale.Language.Tajik
     - tg
   * - Locale.Language.Tagalog
     - tl
   * - Locale.Language.Thai
     - th
   * - Locale.Language.Tibetan
     - bo
   * - Locale.Language.Tigrinya
     - ti
   * - Locale.Language.Tonga
     - to
   * - Locale.Language.Tswana
     - tn
   * - Locale.Language.Tsonga
     - ts
   * - Locale.Language.Turkmen
     - tk
   * - Locale.Language.Turkish
     - tr
   * - Locale.Language.Twi
     - tw
   * - Locale.Language.Uighur
     - ug
   * - Locale.Language.Ukrainian
     - uk
   * - Locale.Language.Urdu
     - ur
   * - Locale.Language.Uzbek
     - uz
   * - Locale.Language.Venda
     - ve
   * - Locale.Language.Vietnamese
     - vi
   * - Locale.Language.Volapuk
     - vo
   * - Locale.Language.Welsh
     - cy
   * - Locale.Language.Walloon
     - wa
   * - Locale.Language.Wolof
     - wo
   * - Locale.Language.Xhosa
     - xh
   * - Locale.Language.Yiddish
     - yi
   * - Locale.Language.Yoruba
     - yo
   * - Locale.Language.Zhuang
     - za
   * - Locale.Language.Zulu
     - zu
   * - Locale.Language.Brazilian
     - pb
   * - Locale.Language.NoLanguage
     - xn

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
