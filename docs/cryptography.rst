================
Cryptography API
================

.. _cipher:

Cipher
------

Encryption utilities.

CBC
~~~

CBC (Cipher Block Chaining) mode class.

Rijndael
~~~~~~~~

Rijndael (AES) cipher class.

PadWithPadLen
~~~~~~~~~~~~~

PKCS padding function.

Crypt
~~~~~

``fcrypt.crypt`` function.

.. code-block:: python

   cipher = CBC(Rijndael(key, 16), padding=Cipher.PadWithPadLen)
   encrypted = cipher.encrypt(data)
   decrypted = cipher.decrypt(encrypted)
