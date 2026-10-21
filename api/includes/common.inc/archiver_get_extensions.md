# archiver_get_extensions()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8588–8600 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8588-L8600)

## Signature

```php
function archiver_get_extensions()
```

## Documentation

```text
Returns a string of supported archive extensions.

@return
  A space-separated string of extensions suitable for use by the file
  validation system.
```

## Code

```php
function archiver_get_extensions() {
  $valid_extensions = array();
  foreach (archiver_get_info() as $archive) {
    foreach ($archive['extensions'] as $extension) {
      foreach (explode('.', $extension) as $part) {
        if (!in_array($part, $valid_extensions)) {
          $valid_extensions[] = $part;
        }
      }
    }
  }
  return implode(' ', $valid_extensions);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
