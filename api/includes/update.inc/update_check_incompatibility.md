# update_check_incompatibility()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 43–68 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L43-L68)

## Signature

```php
function update_check_incompatibility($name, $type = 'module')
```

## Documentation

```text
Tests the compatibility of a module or theme.
```

## Code

```php
function update_check_incompatibility($name, $type = 'module') {
  static $themes, $modules;

  // Store values of expensive functions for future use.
  if (empty($themes) || empty($modules)) {
    // We need to do a full rebuild here to make sure the database reflects any
    // code changes that were made in the filesystem before the update script
    // was initiated.
    $themes = system_rebuild_theme_data();
    $modules = system_rebuild_module_data();
  }

  if ($type == 'module' && isset($modules[$name])) {
    $file = $modules[$name];
  }
  elseif ($type == 'theme' && isset($themes[$name])) {
    $file = $themes[$name];
  }
  if (!isset($file)
      || !isset($file->info['core'])
      || $file->info['core'] != DRUPAL_CORE_COMPATIBILITY
      || version_compare(phpversion(), $file->info['php']) < 0) {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
