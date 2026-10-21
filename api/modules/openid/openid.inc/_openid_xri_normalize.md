# _openid_xri_normalize()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 303–310 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L303-L310)
- **Module/theme:** openid

## Signature

```php
function _openid_xri_normalize($identifier)
```

## Documentation

```text
OpenID normalization method: normalize XRI identifiers.
```

## Code

```php
function _openid_xri_normalize($identifier) {
  if (_openid_is_xri($identifier)) {
    if (stristr($identifier, 'xri://') !== FALSE) {
      $identifier = substr($identifier, 6);
    }
    return $identifier;
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
