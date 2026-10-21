# ModuleTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 11–127 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L11-L127)
- **Module/theme:** system

## Signature

```php
class ModuleTestCase extends DrupalWebTestCase
```

## Documentation

```text
Helper class for module test cases.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [setUp()](ModuleTestCase/setUp.md)
- [assertTableCount()](ModuleTestCase/assertTableCount.md) — Assert there are tables that begin with the specified base table name.
- [assertModuleTablesExist()](ModuleTestCase/assertModuleTablesExist.md) — Assert that all tables defined in a module's hook_schema() exist.
- [assertModuleTablesDoNotExist()](ModuleTestCase/assertModuleTablesDoNotExist.md) — Assert that none of the tables defined in a module's hook_schema() exist.
- [assertModules()](ModuleTestCase/assertModules.md) — Assert the list of modules are enabled or disabled.
- [assertLogMessage()](ModuleTestCase/assertLogMessage.md) — Verify a log entry was entered for a module's status change. Called in the same way of the expected original watchdog() execution.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
