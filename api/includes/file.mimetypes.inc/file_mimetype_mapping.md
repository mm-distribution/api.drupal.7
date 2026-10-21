# file_mimetype_mapping()

- **Type:** Function
- **File:** [`includes/file.mimetypes.inc`](_file.md), lines 18–26 · [local source](../../../source/includes/file.mimetypes.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.mimetypes.inc#L18-L26)

## Signature

```php
function file_mimetype_mapping()
```

## Documentation

```text
Return an array of MIME extension mappings.

Returns the mapping after modules have altered the default mapping.

@return
  Array of mimetypes correlated to the extensions that relate to them.

@see file_get_mimetype()
```

## Code

```php
function file_mimetype_mapping() {
  $mapping = &drupal_static(__FUNCTION__);
  if (!isset($mapping)) {
    $mapping = file_default_mimetype_mapping();
    // Allow modules to alter the default mapping.
    drupal_alter('file_mimetype_mapping', $mapping);
  }
  return $mapping;
}
```

---
_Drupal 7.103 · [includes/file.mimetypes.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.mimetypes.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
