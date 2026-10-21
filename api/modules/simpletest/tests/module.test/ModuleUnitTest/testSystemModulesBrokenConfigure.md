# ModuleUnitTest::testSystemModulesBrokenConfigure()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 144–152 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L144-L152)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSystemModulesBrokenConfigure()
```

## Documentation

```text
Test system_modules() with a module with a broken configure path.
```

## Code

```php
  function testSystemModulesBrokenConfigure() {
    module_enable(array('system_admin_test'));
    $this->resetAll();
    $admin = $this->drupalCreateUser(array('administer modules'));
    $this->drupalLogin($admin);
    $this->drupalGet('admin/modules');
    $module_log = db_query_range('SELECT message FROM {watchdog} WHERE type = :type ORDER BY wid DESC', 0, 1, array(':type' => 'system'))->fetchField();
    $this->assertEqual('Module %module specifies an invalid path for configuration: %configure', $module_log, 'An error was logged for the module\'s broken configure path.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
