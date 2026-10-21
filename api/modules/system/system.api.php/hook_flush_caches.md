# hook_flush_caches()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2652–2654 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2652-L2654)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_flush_caches()
```

## Documentation

```text
Add a list of cache tables to be cleared.

This hook allows your module to add cache table names to the list of cache
tables that will be cleared by the Clear button on the Performance page or
whenever drupal_flush_all_caches is invoked.

@return
  An array of cache table names.

@see drupal_flush_all_caches()
```

## Code

```php
function hook_flush_caches() {
  return array('cache_example');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_flush_caches()".

- [update_script_test_flush_caches()](../../simpletest/tests/update_script_test.module/update_script_test_flush_caches.md) — `modules/simpletest/tests/update_script_test.module`
- [block_flush_caches()](../../block/block.module/block_flush_caches.md) — `modules/block/block.module`
- [system_cron_test_flush_caches()](../tests/system_cron_test.module/system_cron_test_flush_caches.md) — `modules/system/tests/system_cron_test.module`
- [field_flush_caches()](../../field/field.module/field_flush_caches.md) — `modules/field/field.module`
- [image_flush_caches()](../../image/image.module/image_flush_caches.md) — `modules/image/image.module`
- [system_flush_caches()](../system.module/system_flush_caches.md) — `modules/system/system.module`
- [update_flush_caches()](../../update/update.module/update_flush_caches.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
