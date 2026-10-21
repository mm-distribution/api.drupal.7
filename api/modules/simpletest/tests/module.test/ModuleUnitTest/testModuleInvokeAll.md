# ModuleUnitTest::testModuleInvokeAll()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 167–172 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L167-L172)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleInvokeAll()
```

## Documentation

```text
Test that module_invoke_all() can load a hook defined in hook_hook_info().
```

## Code

```php
  function testModuleInvokeAll() {
    module_enable(array('module_test'), FALSE);
    $this->resetAll();
    $this->drupalGet('module-test/hook-dynamic-loading-invoke-all');
    $this->assertText('success!', 'module_invoke_all() dynamically loads a hook defined in hook_hook_info().');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
