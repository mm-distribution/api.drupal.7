# ModuleUninstallTestCase::testUserPermsUninstalled()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 335–344 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L335-L344)
- **Class:** [ModuleUninstallTestCase](../ModuleUninstallTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUserPermsUninstalled()
```

## Documentation

```text
Tests the hook_modules_uninstalled() of the user module.
```

## Code

```php
  function testUserPermsUninstalled() {
    // Uninstalls the module_test module, so hook_modules_uninstalled()
    // is executed.
    module_disable(array('module_test'));
    drupal_uninstall_modules(array('module_test'));

    // Are the perms defined by module_test removed from {role_permission}.
    $count = db_query("SELECT COUNT(rid) FROM {role_permission} WHERE permission = :perm", array(':perm' => 'module_test perm'))->fetchField();
    $this->assertEqual(0, $count, 'Permissions were all removed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
