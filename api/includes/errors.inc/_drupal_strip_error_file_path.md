# _drupal_strip_error_file_path()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 306–318 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L306-L318)

## Signature

```php
function _drupal_strip_error_file_path($error)
```

## Documentation

```text
Strip full path information from error details.

@param $error
  An array with the following keys: %type, !message, %function, %file, %line
  and severity_level.

@return
  An array with the same keys as the $error param but with full paths
  stripped from the %file element
```

## Code

```php
function _drupal_strip_error_file_path($error) {
  if (!empty($error['%file'])) {
    if (($drupal_root_position = strpos($error['%file'], DRUPAL_ROOT)) === 0) {
      $root_length = strlen(DRUPAL_ROOT);
      $error['%file'] = substr($error['%file'], $root_length + 1);
    }
    elseif ($drupal_root_position !== FALSE) {
      // As a fallback, make sure DRUPAL_ROOT's value is not in the path.
      $error['%file'] = str_replace(DRUPAL_ROOT, 'DRUPAL_ROOT', $error['%file']);
    }
  }
  return $error;
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
