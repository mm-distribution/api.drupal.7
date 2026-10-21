# Private update status cache system

- **Topic id:** `update_status_cache`
- **Defined in:** [`modules/update/update.module`](../modules/update/update.module/_file.md), line 736 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L736)

## Documentation

```text
@defgroup update_status_cache Private update status cache system
@{
Functions to manage the update status cache.

We specifically do NOT use the core cache API for saving the fetched data
about available updates. It is vitally important that this cache is only
cleared when we're populating it after successfully fetching new available
update data. Usage of the core cache API results in all sorts of potential
problems that would result in attempting to fetch available update data all
the time, including if a site has a "minimum cache lifetime" (which is both a
minimum and a maximum) defined, or if a site uses memcache or another
pluggable cache system that assumes volatile caches.

The Update Manager module still uses the {cache_update} table, but instead of
using cache_set(), cache_get(), and cache_clear_all(), there are private
helper functions that implement these same basic tasks but ensure that the
cache is not prematurely cleared, and that the data is always stored in the
database, even if memcache or another cache backend is in use.
```

## Members (derived, 5)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_update_cache_clear()](../modules/update/update.module/_update_cache_clear.md) (function) — Invalidates cached data relating to update status.
- [_update_cache_get()](../modules/update/update.module/_update_cache_get.md) (function) — Retrieves data from the private update status cache table.
- [_update_cache_set()](../modules/update/update.module/_update_cache_set.md) (function) — Stores data in the private update status cache table.
- [_update_get_cache_multiple()](../modules/update/update.module/_update_get_cache_multiple.md) (function) — Returns an array of cache items with a given cache ID prefix.
- [update_flush_caches()](../modules/update/update.module/update_flush_caches.md) (function) — Implements hook_flush_caches().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
