# _theme_build_registry()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 678–727 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L678-L727)

## Signature

```php
function _theme_build_registry($theme, $base_theme, $theme_engine)
```

## Documentation

```text
Builds the theme registry cache.

@param $theme
  The loaded $theme object as returned by list_themes().
@param $base_theme
  An array of loaded $theme objects representing the ancestor themes in
  oldest first order.
@param $theme_engine
  The name of the theme engine.
```

## Code

```php
function _theme_build_registry($theme, $base_theme, $theme_engine) {
  $cache = array();
  // First, process the theme hooks advertised by modules. This will
  // serve as the basic registry. Since the list of enabled modules is the same
  // regardless of the theme used, this is cached in its own entry to save
  // building it for every theme.
  if ($cached = cache_get('theme_registry:build:modules')) {
    $cache = $cached->data;
  }
  else {
    foreach (module_implements('theme') as $module) {
      _theme_process_registry($cache, $module, 'module', $module, drupal_get_path('module', $module));
    }
    // Only cache this registry if all modules are loaded.
    if (module_load_all(NULL)) {
      cache_set('theme_registry:build:modules', $cache);
    }
  }

  // Process each base theme.
  foreach ($base_theme as $base) {
    // If the base theme uses a theme engine, process its hooks.
    $base_path = dirname($base->filename);
    if ($theme_engine) {
      _theme_process_registry($cache, $theme_engine, 'base_theme_engine', $base->name, $base_path);
    }
    _theme_process_registry($cache, $base->name, 'base_theme', $base->name, $base_path);
  }

  // And then the same thing, but for the theme.
  if ($theme_engine) {
    _theme_process_registry($cache, $theme_engine, 'theme_engine', $theme->name, dirname($theme->filename));
  }

  // Finally, hooks provided by the theme itself.
  _theme_process_registry($cache, $theme->name, 'theme', $theme->name, dirname($theme->filename));

  // Let modules alter the registry.
  drupal_alter('theme_registry', $cache);

  // Optimize the registry to not have empty arrays for functions.
  foreach ($cache as $hook => $info) {
    foreach (array('preprocess functions', 'process functions') as $phase) {
      if (empty($info[$phase])) {
        unset($cache[$hook][$phase]);
      }
    }
  }
  return $cache;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
