# BlockCacheTestCase::testCacheGlobal()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 574–589 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L574-L589)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCacheGlobal()
```

## Documentation

```text
Test DRUPAL_CACHE_GLOBAL.
```

## Code

```php
  function testCacheGlobal() {
    $this->setCacheMode(DRUPAL_CACHE_GLOBAL);
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    $this->drupalGet('');
    $this->assertText($current_content, 'Block content displays.');

    $old_content = $current_content;
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    $this->drupalLogout();
    $this->drupalGet('user');
    $this->assertText($old_content, 'Block content served from global cache.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
