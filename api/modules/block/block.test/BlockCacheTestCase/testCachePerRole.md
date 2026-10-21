# BlockCacheTestCase::testCachePerRole()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 527–569 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L527-L569)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function testCachePerRole()
```

## Documentation

```text
Test DRUPAL_CACHE_PER_ROLE.
```

## Code

```php
  function testCachePerRole() {
    $this->setCacheMode(DRUPAL_CACHE_PER_ROLE);

    // Enable our test block. Set some content for it to display.
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
    $this->drupalLogin($this->normal_user);
    $this->drupalGet('');
    $this->assertText($current_content, 'Block content displays.');

    // Change the content, but the cached copy should still be served.
    $old_content = $current_content;
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
    $this->drupalGet('');
    $this->assertText($old_content, 'Block is served from the cache.');

    // Clear the cache and verify that the stale data is no longer there.
    cache_clear_all();
    $this->drupalGet('');
    $this->assertNoText($old_content, 'Block cache clear removes stale cache data.');
    $this->assertText($current_content, 'Fresh block content is displayed after clearing the cache.');

    // Test whether the cached data is served for the correct users.
    $old_content = $current_content;
    $current_content = $this->randomName();
    variable_set('block_test_content', $current_content);
    $this->drupalLogout();
    $this->drupalGet('');
    $this->assertNoText($old_content, 'Anonymous user does not see content cached per-role for normal user.');

    $this->drupalLogin($this->normal_user_alt);
    $this->drupalGet('');
    $this->assertText($old_content, 'User with the same roles sees per-role cached content.');

    $this->drupalLogin($this->admin_user);
    $this->drupalGet('');
    $this->assertNoText($old_content, 'Admin user does not see content cached per-role for normal user.');

    $this->drupalLogin($this->normal_user);
    $this->drupalGet('');
    $this->assertText($old_content, 'Block is served from the per-role cache.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
