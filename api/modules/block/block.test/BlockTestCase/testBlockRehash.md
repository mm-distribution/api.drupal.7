# BlockTestCase::testBlockRehash()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 362–380 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L362-L380)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockRehash()
```

## Documentation

```text
Test _block_rehash().
```

## Code

```php
  function testBlockRehash() {
    module_enable(array('block_test'));
    $this->assertTrue(module_exists('block_test'), 'Test block module enabled.');

    // Our new block should be inserted in the database when we visit the
    // block management page.
    $this->drupalGet('admin/structure/block');
    // Our test block's caching should default to DRUPAL_CACHE_PER_ROLE.
    $current_caching = db_query("SELECT cache FROM {block} WHERE module = 'block_test' AND delta = 'test_cache'")->fetchField();
    $this->assertEqual($current_caching, DRUPAL_CACHE_PER_ROLE, 'Test block cache mode defaults to DRUPAL_CACHE_PER_ROLE.');

    // Disable caching for this block.
    variable_set('block_test_caching', DRUPAL_NO_CACHE);
    // Flushing all caches should call _block_rehash().
    drupal_flush_all_caches();
    // Verify that the database is updated with the new caching mode.
    $current_caching = db_query("SELECT cache FROM {block} WHERE module = 'block_test' AND delta = 'test_cache'")->fetchField();
    $this->assertEqual($current_caching, DRUPAL_NO_CACHE, "Test block's database entry updated to DRUPAL_NO_CACHE.");
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
