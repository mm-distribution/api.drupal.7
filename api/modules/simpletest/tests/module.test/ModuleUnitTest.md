# ModuleUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/module.test`](_file.md), lines 11–277 · [local source](../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L11-L277)
- **Module/theme:** batch_test

## Signature

```php
class ModuleUnitTest extends DrupalWebTestCase
```

## Documentation

```text
Unit tests for the module API.
```

## Properties

### $user

```php
protected $user;
```

## Methods (derived index)

- [getInfo()](ModuleUnitTest/getInfo.md)
- [setUp()](ModuleUnitTest/setUp.md) — {@inheritdoc}
- [testModuleList()](ModuleUnitTest/testModuleList.md) — The basic functionality of module_list().
- [assertModuleList()](ModuleUnitTest/assertModuleList.md) — Assert that module_list() return the expected values.
- [testModuleImplements()](ModuleUnitTest/testModuleImplements.md) — Test module_implements() caching.
- [testSystemModulesNullVersion()](ModuleUnitTest/testSystemModulesNullVersion.md) — Test system_modules() with a module with a dependency with a null version.
- [testSystemModulesBrokenConfigure()](ModuleUnitTest/testSystemModulesBrokenConfigure.md) — Test system_modules() with a module with a broken configure path.
- [testModuleInvoke()](ModuleUnitTest/testModuleInvoke.md) — Test that module_invoke() can load a hook defined in hook_hook_info().
- [testModuleInvokeAll()](ModuleUnitTest/testModuleInvokeAll.md) — Test that module_invoke_all() can load a hook defined in hook_hook_info().
- [testDependencyResolution()](ModuleUnitTest/testDependencyResolution.md) — Test dependency resolution.

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
