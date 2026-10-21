# CacheTestCase::checkCacheExists()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 20–28 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L20-L28)
- **Class:** [CacheTestCase](../CacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function checkCacheExists($cid, $var, $bin = NULL)
```

## Documentation

```text
Check whether or not a cache entry exists.

@param $cid
  The cache id.
@param $var
  The variable the cache should contain.
@param $bin
  The bin the cache item was stored in.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function checkCacheExists($cid, $var, $bin = NULL) {
    if ($bin == NULL) {
      $bin = $this->default_bin;
    }

    $cache = cache_get($cid, $bin);

    return isset($cache->data) && $cache->data == $var;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
