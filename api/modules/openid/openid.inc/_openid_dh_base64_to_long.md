# _openid_dh_base64_to_long()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 468–472 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L468-L472)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_base64_to_long($str)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_base64_to_long($str) {
  $b64 = base64_decode($str);

  return _openid_dh_binary_to_long($b64);
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
