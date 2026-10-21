# ModuleUnitTest::testModuleInvoke()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 157–162 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L157-L162)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleInvoke()
```

## Documentation

```text
Test that module_invoke() can load a hook defined in hook_hook_info().
```

## Code

```php
  function testModuleInvoke() {
    module_enable(array('module_test'), FALSE);
    $this->resetAll();
    $this->drupalGet('module-test/hook-dynamic-loading-invoke');
    $this->assertText('success!', 'module_invoke() dynamically loads a hook defined in hook_hook_info().');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
