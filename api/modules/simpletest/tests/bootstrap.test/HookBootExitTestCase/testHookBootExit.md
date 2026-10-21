# HookBootExitTestCase::testHookBootExit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 385–413 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L385-L413)
- **Class:** [HookBootExitTestCase](../HookBootExitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHookBootExit()
```

## Documentation

```text
Test calling of hook_boot() and hook_exit().
```

## Code

```php
  function testHookBootExit() {
    // Test with cache disabled. Boot and exit should always fire.
    variable_set('cache', 0);
    $this->drupalGet('');
    $calls = 1;
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_boot'))->fetchField(), $calls, t('hook_boot called with disabled cache.'));
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_exit'))->fetchField(), $calls, t('hook_exit called with disabled cache.'));

    // Test with normal cache. Boot and exit should be called.
    variable_set('cache', 1);
    $this->drupalGet('');
    $calls++;
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_boot'))->fetchField(), $calls, t('hook_boot called with normal cache.'));
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_exit'))->fetchField(), $calls, t('hook_exit called with normal cache.'));

    // Boot and exit should not fire since the page is cached.
    variable_set('page_cache_invoke_hooks', FALSE);
    $this->assertTrue(cache_get(url('', array('absolute' => TRUE)), 'cache_page'), t('Page has been cached.'));
    $this->drupalGet('');
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_boot'))->fetchField(), $calls, t('hook_boot not called with aggressive cache and a cached page.'));
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_exit'))->fetchField(), $calls, t('hook_exit not called with aggressive cache and a cached page.'));

    // Test with page cache cleared, boot and exit should be called.
    $this->assertTrue(db_delete('cache_page')->execute(), t('Page cache cleared.'));
    $this->drupalGet('');
    $calls++;
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_boot'))->fetchField(), $calls, t('hook_boot called with aggressive cache and no cached page.'));
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND message = :message', array(':type' => 'system_test', ':message' => 'hook_exit'))->fetchField(), $calls, t('hook_exit called with aggressive cache and no cached page.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
