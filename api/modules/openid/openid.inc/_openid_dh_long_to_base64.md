# _openid_dh_long_to_base64()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 474–476 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L474-L476)
- **Module/theme:** openid

## Signature

```php
function _openid_dh_long_to_base64($str)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_dh_long_to_base64($str) {
  return base64_encode(_openid_dh_long_to_binary($str));
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
