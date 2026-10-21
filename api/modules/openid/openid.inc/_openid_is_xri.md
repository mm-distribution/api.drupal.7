# _openid_is_xri()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 263–276 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L263-L276)
- **Module/theme:** openid

## Signature

```php
function _openid_is_xri($identifier)
```

## Documentation

```text
Determine if the given identifier is an XRI ID.
```

## Code

```php
function _openid_is_xri($identifier) {
  // Strip the xri:// scheme from the identifier if present.
  if (stripos($identifier, 'xri://') === 0) {
    $identifier = substr($identifier, 6);
  }

  // Test whether the identifier starts with an XRI global context symbol or (.
  $firstchar = substr($identifier, 0, 1);
  if (strpos("=@+$!(", $firstchar) !== FALSE) {
    return TRUE;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
