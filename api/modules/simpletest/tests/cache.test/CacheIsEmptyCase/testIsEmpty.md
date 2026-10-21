# CacheIsEmptyCase::testIsEmpty()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 410–422 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L410-L422)
- **Class:** [CacheIsEmptyCase](../CacheIsEmptyCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testIsEmpty()
```

## Documentation

```text
Test clearing using a cid.
```

## Code

```php
  function testIsEmpty() {
    // Clear the cache bin.
    cache_clear_all('*', $this->default_bin);
    $this->assertTrue(cache_is_empty($this->default_bin), 'The cache bin is empty');
    // Add some data to the cache bin.
    cache_set($this->default_cid, $this->default_value, $this->default_bin);
    $this->assertCacheExists(t('Cache was set.'), $this->default_value, $this->default_cid);
    $this->assertFalse(cache_is_empty($this->default_bin), 'The cache bin is not empty');
    // Remove the cached data.
    cache_clear_all($this->default_cid, $this->default_bin);
    $this->assertCacheRemoved(t('Cache was removed.'), $this->default_cid);
    $this->assertTrue(cache_is_empty($this->default_bin), 'The cache bin is empty');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
