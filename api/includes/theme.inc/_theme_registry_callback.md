# _theme_registry_callback()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 291–297 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L291-L297)

## Signature

```php
function _theme_registry_callback($callback = NULL, array $arguments = array())
```

## Documentation

```text
Sets the callback that will be used by theme_get_registry().

@param $callback
  The name of the callback function.
@param $arguments
  The arguments to pass to the function.
```

## Code

```php
function _theme_registry_callback($callback = NULL, array $arguments = array()) {
  static $stored;
  if (isset($callback)) {
    $stored = array($callback, $arguments);
  }
  return $stored;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
