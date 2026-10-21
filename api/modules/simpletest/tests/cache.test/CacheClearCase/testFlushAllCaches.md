# CacheClearCase::testFlushAllCaches()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 311–327 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L311-L327)
- **Class:** [CacheClearCase](../CacheClearCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFlushAllCaches()
```

## Documentation

```text
Test drupal_flush_all_caches().
```

## Code

```php
  function testFlushAllCaches() {
    // Create cache entries for each flushed cache bin.
    $bins = array('cache', 'cache_filter', 'cache_page', 'cache_boostrap', 'cache_path');
    $bins = array_merge(module_invoke_all('flush_caches'), $bins);
    foreach ($bins as $id => $bin) {
      $id = 'test_cid_clear' . $id;
      cache_set($id, $this->default_value, $bin);
    }

    // Remove all caches then make sure that they are cleared.
    drupal_flush_all_caches();

    foreach ($bins as $id => $bin) {
      $id = 'test_cid_clear' . $id;
      $this->assertFalse($this->checkCacheExists($id, $this->default_value, $bin), format_string('All cache entries removed from @bin.', array('@bin' => $bin)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
