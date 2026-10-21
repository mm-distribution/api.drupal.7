# BlockCacheTestCase::testCachePerUser()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 613–636 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L613-L636)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCachePerUser()
```

## Documentation

```text
Test DRUPAL_CACHE_PER_USER.
```

## Code

```php
  function testCachePerUser() {
    $this->setCacheMode(DRUPAL_CACHE_PER_USER);
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
    $this->drupalLogin($this->normal_user);

    $this->drupalGet('');
    $this->assertText($current_content, 'Block content displays.');

    $old_content = $current_content;
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);

    $this->drupalGet('');
    $this->assertText($old_content, 'Block is served from per-user cache.');

    $this->drupalLogin($this->normal_user_alt);
    $this->drupalGet('');
    $this->assertText($current_content, 'Per-user block cache is not served for other users.');

    $this->drupalLogin($this->normal_user);
    $this->drupalGet('');
    $this->assertText($old_content, 'Per-user block cache is persistent.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
