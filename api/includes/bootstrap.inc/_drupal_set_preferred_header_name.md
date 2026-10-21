# _drupal_set_preferred_header_name()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1515–1522 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1515-L1522)

## Signature

```php
function _drupal_set_preferred_header_name($name = NULL)
```

## Documentation

```text
Sets the preferred name for the HTTP header.

Header names are case-insensitive, but for maximum compatibility they should
follow "common form" (see RFC 2617, section 4.2).
```

## Code

```php
function _drupal_set_preferred_header_name($name = NULL) {
  static $header_names = array();

  if (!isset($name)) {
    return $header_names;
  }
  $header_names[strtolower($name)] = $name;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
