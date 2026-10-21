# DrupalDatabaseCache

- **Type:** Class
- **File:** [`includes/cache.inc`](_file.md), lines 322–590 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L322-L590)

## Signature

```php
class DrupalDatabaseCache implements DrupalCacheInterface
```

## Documentation

```text
Defines a default cache implementation.

This is Drupal's default cache implementation. It uses the database to store
cached data. Each cache bin corresponds to a database table by the same name.
```

## Properties

### $bin

```php
protected $bin;
```

## Methods (derived index)

- [__construct()](DrupalDatabaseCache/__construct.md) — Constructs a DrupalDatabaseCache object.
- [get()](DrupalDatabaseCache/get.md) — Implements DrupalCacheInterface::get().
- [getMultiple()](DrupalDatabaseCache/getMultiple.md) — Implements DrupalCacheInterface::getMultiple().
- [garbageCollection()](DrupalDatabaseCache/garbageCollection.md) — Garbage collection for get() and getMultiple().
- [prepareItem()](DrupalDatabaseCache/prepareItem.md) — Prepares a cached item.
- [set()](DrupalDatabaseCache/set.md) — Implements DrupalCacheInterface::set().
- [clear()](DrupalDatabaseCache/clear.md) — Implements DrupalCacheInterface::clear().
- [isEmpty()](DrupalDatabaseCache/isEmpty.md) — Implements DrupalCacheInterface::isEmpty().
- [isValidBin()](DrupalDatabaseCache/isValidBin.md) — Checks if $this->bin represents a valid cache table.

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
