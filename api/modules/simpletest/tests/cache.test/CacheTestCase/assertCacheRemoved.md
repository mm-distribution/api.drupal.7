# CacheTestCase::assertCacheRemoved()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 66–76 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L66-L76)
- **Class:** [CacheTestCase](../CacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertCacheRemoved($message, $cid = NULL, $bin = NULL)
```

## Documentation

```text
Assert or a cache entry has been removed.

@param $message
  Message to display.
@param $cid
  The cache id.
@param $bin
  The bin the cache item was stored in.
```

## Code

```php
  function assertCacheRemoved($message, $cid = NULL, $bin = NULL) {
    if ($bin == NULL) {
      $bin = $this->default_bin;
    }
    if ($cid == NULL) {
      $cid = $this->default_cid;
    }

    $cache = cache_get($cid, $bin);
    $this->assertFalse($cache, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
