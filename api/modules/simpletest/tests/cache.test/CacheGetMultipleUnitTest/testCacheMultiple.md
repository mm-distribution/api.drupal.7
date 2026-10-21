# CacheGetMultipleUnitTest::testCacheMultiple()

- **Type:** Method
- **File:** [`modules/simpletest/tests/cache.test`](../_file.md), lines 193–216 · [local source](../../../../../../source/modules/simpletest/tests/cache.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test#L193-L216)
- **Class:** [CacheGetMultipleUnitTest](../CacheGetMultipleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testCacheMultiple()
```

## Documentation

```text
Test cache_get_multiple().
```

## Code

```php
  function testCacheMultiple() {
    $item1 = $this->randomName(10);
    $item2 = $this->randomName(10);
    cache_set('item1', $item1, $this->default_bin);
    cache_set('item2', $item2, $this->default_bin);
    $this->assertTrue($this->checkCacheExists('item1', $item1), 'Item 1 is cached.');
    $this->assertTrue($this->checkCacheExists('item2', $item2), 'Item 2 is cached.');

    // Fetch both records from the database with cache_get_multiple().
    $item_ids = array('item1', 'item2');
    $items = cache_get_multiple($item_ids, $this->default_bin);
    $this->assertEqual($items['item1']->data, $item1, 'Item was returned from cache successfully.');
    $this->assertEqual($items['item2']->data, $item2, 'Item was returned from cache successfully.');

    // Remove one item from the cache.
    cache_clear_all('item2', $this->default_bin);

    // Confirm that only one item is returned by cache_get_multiple().
    $item_ids = array('item1', 'item2');
    $items = cache_get_multiple($item_ids, $this->default_bin);
    $this->assertEqual($items['item1']->data, $item1, 'Item was returned from cache successfully.');
    $this->assertFalse(isset($items['item2']), 'Item was not returned from the cache.');
    $this->assertTrue(count($items) == 1, 'Only valid cache entries returned.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/cache.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/cache.test) · Licensed GPL-2.0-or-later (see LICENSE)._
