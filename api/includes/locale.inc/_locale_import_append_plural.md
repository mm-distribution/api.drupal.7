# _locale_import_append_plural()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1452–1461 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1452-L1461)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_append_plural($entry, $key)
```

## Documentation

```text
Modify a string to contain proper count indices

This is a callback function used via array_map()

@param $entry
  An array element.
@param $key
  Index of the array element.
```

## Code

```php
function _locale_import_append_plural($entry, $key) {
  // No modifications for 0, 1
  if ($key == 0 || $key == 1) {
    return $entry;
  }

  // First remove any possibly false indices, then add new ones
  $entry = preg_replace('/(@count)\[[0-9]\]/', '\\1', $entry);
  return preg_replace('/(@count)/', "\\1[$key]", $entry);
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
