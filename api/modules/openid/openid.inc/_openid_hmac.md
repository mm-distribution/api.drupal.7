# _openid_hmac()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 454–466 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L454-L466)
- **Module/theme:** openid

## Signature

```php
function _openid_hmac($key, $text)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_hmac($key, $text) {
  if (strlen($key) > OPENID_SHA1_BLOCKSIZE) {
    $key = sha1($key, TRUE);
  }

  $key = str_pad($key, OPENID_SHA1_BLOCKSIZE, chr(0x00));
  $ipad = str_repeat(chr(0x36), OPENID_SHA1_BLOCKSIZE);
  $opad = str_repeat(chr(0x5c), OPENID_SHA1_BLOCKSIZE);
  $hash1 = sha1(($key ^ $ipad) . $text, TRUE);
  $hmac = sha1(($key ^ $opad) . $hash1, TRUE);

  return $hmac;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
