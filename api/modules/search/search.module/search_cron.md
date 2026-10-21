# search_cron()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 356–365 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L356-L365)
- **Module/theme:** search
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function search_cron()
```

## Documentation

```text
Implements hook_cron().

Fires hook_update_index() in all modules and cleans up dirty words.

@see search_dirty()
```

## Code

```php
function search_cron() {
  // We register a shutdown function to ensure that search_total is always up
  // to date.
  drupal_register_shutdown_function('search_update_totals');

  foreach (variable_get('search_active_modules', array('node', 'user')) as $module) {
    // Update word index
    module_invoke($module, 'update_index');
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
