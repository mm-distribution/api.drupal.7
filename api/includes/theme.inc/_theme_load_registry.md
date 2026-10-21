# _theme_load_registry()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 316–337 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L316-L337)

## Signature

```php
function _theme_load_registry($theme, $base_theme = NULL, $theme_engine = NULL, $complete = TRUE)
```

## Documentation

```text
Gets the theme_registry cache; if it doesn't exist, builds it.

@param $theme
  The loaded $theme object as returned by list_themes().
@param $base_theme
  An array of loaded $theme objects representing the ancestor themes in
  oldest first order.
@param $theme_engine
  The name of the theme engine.
@param $complete
  Whether to load the complete theme registry or an instance of the
  ThemeRegistry class.

@return
  The theme registry array, or an instance of the ThemeRegistry class.
```

## Code

```php
function _theme_load_registry($theme, $base_theme = NULL, $theme_engine = NULL, $complete = TRUE) {
  if ($complete) {
    // Check the theme registry cache; if it exists, use it.
    $cached = cache_get("theme_registry:$theme->name");
    if (isset($cached->data)) {
      $registry = $cached->data;
    }
    else {
      // If not, build one and cache it.
      $registry = _theme_build_registry($theme, $base_theme, $theme_engine);
      // Only persist this registry if all modules are loaded. This assures a
      // complete set of theme hooks.
      if (module_load_all(NULL)) {
        _theme_save_registry($theme, $registry);
      }
    }
    return $registry;
  }
  else {
    return new ThemeRegistry('theme_registry:runtime:' . $theme->name, 'cache');
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
