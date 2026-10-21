# _fix_gpc_magic()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1217–1224 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1217-L1224)

## Signature

```php
function _fix_gpc_magic(&$item)
```

## Documentation

```text
Strips slashes from a string or array of strings.

Callback for array_walk() within fix_gpx_magic().

@param $item
  An individual string or array of strings from superglobals.
```

## Code

```php
function _fix_gpc_magic(&$item) {
  if (is_array($item)) {
    array_walk($item, '_fix_gpc_magic');
  }
  else {
    $item = stripslashes($item);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
