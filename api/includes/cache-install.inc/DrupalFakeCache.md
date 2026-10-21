# DrupalFakeCache

- **Type:** Class
- **File:** [`includes/cache-install.inc`](_file.md), lines 17–74 · [local source](../../../source/includes/cache-install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc#L17-L74)

## Signature

```php
class DrupalFakeCache extends DrupalDatabaseCache implements DrupalCacheInterface
```

## Documentation

```text
Defines a stub cache implementation to be used during installation.

The stub implementation is needed when database access is not yet available.
Because Drupal's caching system never requires that cached data be present,
these stub functions can short-circuit the process and sidestep the need for
any persistent storage. Obviously, using this cache implementation during
normal operations would have a negative impact on performance.
```

## Methods (derived index)

- [get()](DrupalFakeCache/get.md) — Overrides DrupalDatabaseCache::get().
- [getMultiple()](DrupalFakeCache/getMultiple.md) — Overrides DrupalDatabaseCache::getMultiple().
- [set()](DrupalFakeCache/set.md) — Overrides DrupalDatabaseCache::set().
- [clear()](DrupalFakeCache/clear.md) — Overrides DrupalDatabaseCache::clear().
- [isEmpty()](DrupalFakeCache/isEmpty.md) — Overrides DrupalDatabaseCache::isEmpty().

---
_Drupal 7.103 · [includes/cache-install.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache-install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
