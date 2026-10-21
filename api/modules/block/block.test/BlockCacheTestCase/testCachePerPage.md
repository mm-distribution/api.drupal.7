# BlockCacheTestCase::testCachePerPage()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 641–657 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L641-L657)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCachePerPage()
```

## Documentation

```text
Test DRUPAL_CACHE_PER_PAGE.
```

## Code

```php
  function testCachePerPage() {
    $this->setCacheMode(DRUPAL_CACHE_PER_PAGE);
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    $this->drupalGet('node');
    $this->assertText($current_content, 'Block content displays on the node page.');

    $old_content = $current_content;
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    $this->drupalGet('user');
    $this->assertNoText($old_content, 'Block content cached for the node page does not show up for the user page.');
    $this->drupalGet('node');
    $this->assertText($old_content, 'Block content cached for the node page.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
