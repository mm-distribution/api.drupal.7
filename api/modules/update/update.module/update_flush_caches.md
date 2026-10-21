# update_flush_caches()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 886–891 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L886-L891)
- **Module/theme:** update
- **Topics:** [update_status_cache](../../../topics/update_status_cache.md)
- **Implements:** [hook_flush_caches()](../../system/system.api.php/hook_flush_caches.md)

## Signature

```php
function update_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().

Called from update.php (among others) to flush the caches. Since we're
running update.php, we are likely to install a new version of something, in
which case, we want to check for available update data again. However,
because we have our own caching system, we need to directly clear the
database table ourselves at this point and return nothing, for example, on
sites that use memcache where cache_clear_all() won't know how to purge this
data.

However, we only want to do this from update.php, since otherwise, we'd lose
all the available update data on every cron run. So, we specifically check if
the site is in MAINTENANCE_MODE == 'update' (which indicates update.php is
running, not update module... alas for overloaded names).
```

## Code

```php
function update_flush_caches() {
  if (defined('MAINTENANCE_MODE') && MAINTENANCE_MODE == 'update') {
    _update_cache_clear();
  }
  return array();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
