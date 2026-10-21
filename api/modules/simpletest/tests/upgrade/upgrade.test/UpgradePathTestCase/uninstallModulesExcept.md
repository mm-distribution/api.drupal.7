# UpgradePathTestCase::uninstallModulesExcept()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 302–311 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L302-L311)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function uninstallModulesExcept(array $modules)
```

## Documentation

```text
Force uninstall all modules from a test database, except those listed.

@param $modules
  The list of modules to keep installed. Required core modules will
  always be kept.
```

## Code

```php
  protected function uninstallModulesExcept(array $modules) {
    $required_modules = array('block', 'dblog', 'filter', 'node', 'system', 'update', 'user');

    $modules = array_merge($required_modules, $modules);

    db_delete('system')
      ->condition('type', 'module')
      ->condition('name', $modules, 'NOT IN')
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
