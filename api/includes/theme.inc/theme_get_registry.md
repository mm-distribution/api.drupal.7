# theme_get_registry()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 255–281 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L255-L281)

## Signature

```php
function theme_get_registry($complete = TRUE)
```

## Documentation

```text
Gets the theme registry.

@param $complete
  Optional boolean to indicate whether to return the complete theme registry
  array or an instance of the ThemeRegistry class. If TRUE, the complete
  theme registry array will be returned. This is useful if you want to
  foreach over the whole registry, use array_* functions or inspect it in a
  debugger. If FALSE, an instance of the ThemeRegistry class will be
  returned, this provides an ArrayObject which allows it to be accessed
  with array syntax and  isset(), and should be more lightweight
  than the full registry. Defaults to TRUE.

@return
  The complete theme registry array, or an instance of the ThemeRegistry
  class.
```

## Code

```php
function theme_get_registry($complete = TRUE) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['registry'] = &drupal_static('theme_get_registry');
  }
  $theme_registry = &$drupal_static_fast['registry'];

  // Initialize the theme, if this is called early in the bootstrap, or after
  // static variables have been reset.
  if (!is_array($theme_registry)) {
    drupal_theme_initialize();
    $theme_registry = array();
  }

  $key = (int) $complete;

  if (!isset($theme_registry[$key])) {
    list($callback, $arguments) = _theme_registry_callback();
    if (!$complete) {
      $arguments[] = FALSE;
    }
    $theme_registry[$key] = call_user_func_array($callback, $arguments);
  }

  return $theme_registry[$key];
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
