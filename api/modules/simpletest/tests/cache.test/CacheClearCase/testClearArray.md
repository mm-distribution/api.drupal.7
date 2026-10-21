# CacheClearCase::testClearArray()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 288–306 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L288-L306)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testClearArray()
```

## Documentation

```text
Test clearing using an array.
```

## Code

```php
  function testClearArray() {
    // Create three cache entries.
    cache_set('test_cid_clear1', $this->default_value, $this->default_bin);
    cache_set('test_cid_clear2', $this->default_value, $this->default_bin);
    cache_set('test_cid_clear3', $this->default_value, $this->default_bin);
    $this->assertTrue($this->checkCacheExists('test_cid_clear1', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear2', $this->default_value)
                      && $this->checkCacheExists('test_cid_clear3', $this->default_value),
                      'Three cache entries were created.');

    // Clear two entries using an array.
    cache_clear_all(array('test_cid_clear1', 'test_cid_clear2'), $this->default_bin);
    $this->assertFalse($this->checkCacheExists('test_cid_clear1', $this->default_value)
                       || $this->checkCacheExists('test_cid_clear2', $this->default_value),
                       'Two cache entries removed after clearing with an array.');

    $this->assertTrue($this->checkCacheExists('test_cid_clear3', $this->default_value),
                      'Entry was not cleared from the cache');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
