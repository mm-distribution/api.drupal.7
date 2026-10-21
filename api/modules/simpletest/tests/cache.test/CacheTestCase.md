# CacheTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/cache.test`](_file.md), lines 3–101 · [local source](../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L3-L101)
- **Module/theme:** batch_test

## Signature

```php
class CacheTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $default_bin

```php
protected $default_bin = 'cache';
```

### $default_cid

```php
protected $default_cid = 'test_temporary';
```

### $default_value

```php
protected $default_value = 'CacheTest';
```

## Methods (derived index)

- [checkCacheExists()](CacheTestCase/checkCacheExists.md) — Check whether or not a cache entry exists.
- [assertCacheExists()](CacheTestCase/assertCacheExists.md) — Assert or a cache entry exists.
- [assertCacheRemoved()](CacheTestCase/assertCacheRemoved.md) — Assert or a cache entry has been removed.
- [generalWipe()](CacheTestCase/generalWipe.md) — Perform the general wipe.
- [setupLifetime()](CacheTestCase/setupLifetime.md) — Setup the lifetime settings for caching.

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
