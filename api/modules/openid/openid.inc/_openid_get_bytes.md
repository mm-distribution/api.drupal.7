# _openid_get_bytes()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 569–571 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L569-L571)
- **Module/theme:** openid

## Signature

```php
function _openid_get_bytes($num_bytes)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_get_bytes($num_bytes) {
  return drupal_random_bytes($num_bytes);
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
