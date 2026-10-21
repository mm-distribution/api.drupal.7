# BlockCacheTestCase::testNoCache()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 594–608 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L594-L608)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function testNoCache()
```

## Documentation

```text
Test DRUPAL_NO_CACHE.
```

## Code

```php
  function testNoCache() {
    $this->setCacheMode(DRUPAL_NO_CACHE);
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    // If DRUPAL_NO_CACHE has no effect, the next request would be cached.
    $this->drupalGet('');
    $this->assertText($current_content, 'Block content displays.');

    // A cached copy should not be served.
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
    $this->drupalGet('');
    $this->assertText($current_content, 'DRUPAL_NO_CACHE prevents blocks from being cached.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
