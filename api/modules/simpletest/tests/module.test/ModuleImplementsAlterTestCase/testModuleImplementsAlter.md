# ModuleImplementsAlterTestCase::testModuleImplementsAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 359–385 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L359-L385)
- **Class:** [ModuleImplementsAlterTestCase](../ModuleImplementsAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleImplementsAlter()
```

## Documentation

```text
Tests hook_module_implements_alter() adding an implementation.
```

## Code

```php
  function testModuleImplementsAlter() {
    module_enable(array('module_test'), FALSE);
    $this->assertTrue(module_exists('module_test'), 'Test module is enabled.');

    // Assert that module_test.module is now included.
    $this->assertTrue(function_exists('module_test_permission'),
      'The file module_test.module was successfully included.');

    $modules = module_implements('permission');
    $this->assertTrue(in_array('module_test', $modules), 'module_test implements hook_permission.');

    $modules = module_implements('module_implements_alter');
    $this->assertTrue(in_array('module_test', $modules), 'module_test implements hook_module_implements_alter().');

    // Assert that module_test.implementations.inc is not included yet.
    $this->assertFalse(function_exists('module_test_altered_test_hook'),
      'The file module_test.implementations.inc is not included yet.');

    // Assert that module_test_module_implements_alter(*, 'altered_test_hook')
    // has added an implementation
    $this->assertTrue(in_array('module_test', module_implements('altered_test_hook')),
      'module_test implements hook_altered_test_hook().');

    // Assert that module_test.implementations.inc was included as part of the process.
    $this->assertTrue(function_exists('module_test_altered_test_hook'),
      'The file module_test.implementations.inc was included.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
