# image_get_toolkit()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 63–78 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L63-L78)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_get_toolkit()
```

## Documentation

```text
Gets the name of the currently used toolkit.

@return
  String containing the name of the selected toolkit, or FALSE on error.
```

## Code

```php
function image_get_toolkit() {
  static $toolkit;

  if (!isset($toolkit)) {
    $toolkits = image_get_available_toolkits();
    $toolkit = variable_get('image_toolkit', 'gd');
    if (!isset($toolkits[$toolkit]) || !function_exists('image_' . $toolkit . '_load')) {
      // The selected toolkit isn't available so return the first one found. If
      // none are available this will return FALSE.
      reset($toolkits);
      $toolkit = key($toolkits);
    }
  }

  return $toolkit;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
