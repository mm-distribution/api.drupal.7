# system_list_reset()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 225–235 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L225-L235)

## Signature

```php
function system_list_reset()
```

## Documentation

```text
Resets all system_list() caches.
```

## Code

```php
function system_list_reset() {
  drupal_static_reset('system_list');
  drupal_static_reset('system_rebuild_module_data');
  drupal_static_reset('list_themes');
  cache_clear_all('bootstrap_modules', 'cache_bootstrap');
  cache_clear_all('system_list', 'cache_bootstrap');

  // Clean up the bootstrap file scan cache.
  drupal_static_reset('_drupal_file_scan_cache');
  cache_clear_all('_drupal_file_scan_cache', 'cache_bootstrap');
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
