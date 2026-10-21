# drupal_load()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1430–1449 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1430-L1449)

## Signature

```php
function drupal_load($type, $name)
```

## Documentation

```text
Includes a file with the provided type and name.

This prevents including a theme, engine, module, etc., more than once.

@param $type
  The type of item to load (i.e. theme, theme_engine, module).
@param $name
  The name of the item to load.

@return
  TRUE if the item is loaded or has already been loaded.
```

## Code

```php
function drupal_load($type, $name) {
  // Once a file is included this can't be reversed during a request so do not
  // use drupal_static() here.
  static $files = array();

  if (isset($files[$type][$name])) {
    return TRUE;
  }

  $filename = drupal_get_filename($type, $name);

  if ($filename) {
    include_once DRUPAL_ROOT . '/' . $filename;
    $files[$type][$name] = TRUE;

    return TRUE;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
