# CacheTestCase::assertCacheExists()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 42–54 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L42-L54)
- **Class:** [CacheTestCase](../CacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertCacheExists($message, $var = NULL, $cid = NULL, $bin = NULL)
```

## Documentation

```text
Assert or a cache entry exists.

@param $message
  Message to display.
@param $var
  The variable the cache should contain.
@param $cid
  The cache id.
@param $bin
  The bin the cache item was stored in.
```

## Code

```php
  protected function assertCacheExists($message, $var = NULL, $cid = NULL, $bin = NULL) {
    if ($bin == NULL) {
      $bin = $this->default_bin;
    }
    if ($cid == NULL) {
      $cid = $this->default_cid;
    }
    if ($var == NULL) {
      $var = $this->default_value;
    }

    $this->assertTrue($this->checkCacheExists($cid, $var, $bin), $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
