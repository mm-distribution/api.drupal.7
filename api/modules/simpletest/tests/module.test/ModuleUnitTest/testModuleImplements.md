# ModuleUnitTest::testModuleImplements()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 103–127 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L103-L127)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleImplements()
```

## Documentation

```text
Test module_implements() caching.
```

## Code

```php
  function testModuleImplements() {
    // Clear the cache.
    cache_clear_all('module_implements', 'cache_bootstrap');
    $this->assertFalse(cache_get('module_implements', 'cache_bootstrap'), 'The module implements cache is empty.');
    $this->drupalGet('');
    $this->assertTrue(cache_get('module_implements', 'cache_bootstrap'), 'The module implements cache is populated after requesting a page.');

    // Test again with an authenticated user.
    $this->user = $this->drupalCreateUser();
    $this->drupalLogin($this->user);
    cache_clear_all('module_implements', 'cache_bootstrap');
    $this->drupalGet('');
    $this->assertTrue(cache_get('module_implements', 'cache_bootstrap'), 'The module implements cache is populated after requesting a page.');

    // Make sure group include files are detected properly even when the file is
    // already loaded when the cache is rebuilt.
    // For that activate the module_test which provides the file to load.
    module_enable(array('module_test'));

    module_load_include('inc', 'module_test', 'module_test.file');
    $modules = module_implements('test_hook');
    $static = drupal_static('module_implements');
    $this->assertTrue(in_array('module_test', $modules), 'Hook found.');
    $this->assertEqual($static['test_hook']['module_test'], 'file', 'Include file detected.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
