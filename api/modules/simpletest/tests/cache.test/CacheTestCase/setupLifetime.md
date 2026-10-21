# CacheTestCase::setupLifetime()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 97–100 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L97-L100)
- **Class:** [CacheTestCase](../CacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function setupLifetime($time)
```

## Documentation

```text
Setup the lifetime settings for caching.

@param $time
  The time in seconds the cache should minimal live.
```

## Code

```php
  protected function setupLifetime($time) {
    variable_set('cache_lifetime', $time);
    variable_set('cache_flush', 0);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
