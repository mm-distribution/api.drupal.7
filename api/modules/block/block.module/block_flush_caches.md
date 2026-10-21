# block_flush_caches()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 987–997 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L987-L997)
- **Module/theme:** block
- **Implements:** [hook_flush_caches()](../../system/system.api.php/hook_flush_caches.md)

## Signature

```php
function block_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().
```

## Code

```php
function block_flush_caches() {
  // Rehash blocks for active themes. We don't use list_themes() here,
  // because if MAINTENANCE_MODE is defined it skips reading the database,
  // and we can't tell which themes are active.
  $themes = db_query("SELECT name FROM {system} WHERE type = 'theme' AND status = 1");
  foreach ($themes as $theme) {
    _block_rehash($theme->name);
  }

  return array('cache_block');
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
