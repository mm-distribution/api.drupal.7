# ModuleDependencyTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 383–599 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L383-L599)
- **Module/theme:** system

## Signature

```php
class ModuleDependencyTestCase extends ModuleTestCase
```

## Documentation

```text
Test module dependency functionality.
```

## Methods (derived index)

- [getInfo()](ModuleDependencyTestCase/getInfo.md)
- [testProjectNamespaceForDependencies()](ModuleDependencyTestCase/testProjectNamespaceForDependencies.md) — Checks functionality of project namespaces for dependencies.
- [testEnableWithoutDependency()](ModuleDependencyTestCase/testEnableWithoutDependency.md) — Attempt to enable translation module without locale enabled.
- [testMissingModules()](ModuleDependencyTestCase/testMissingModules.md) — Attempt to enable a module with a missing dependency.
- [testIncompatibleModuleVersionDependency()](ModuleDependencyTestCase/testIncompatibleModuleVersionDependency.md) — Tests enabling a module that depends on an incompatible version of a module.
- [testIncompatibleCoreVersionDependency()](ModuleDependencyTestCase/testIncompatibleCoreVersionDependency.md) — Tests enabling a module that depends on a module with an incompatible core version.
- [testEnableRequirementsFailureDependency()](ModuleDependencyTestCase/testEnableRequirementsFailureDependency.md) — Tests enabling a module that depends on a module which fails hook_requirements().
- [testModuleEnableOrder()](ModuleDependencyTestCase/testModuleEnableOrder.md) — Tests that module dependencies are enabled in the correct order via the UI. Dependencies should be enabled before their dependents.
- [testUninstallDependents()](ModuleDependencyTestCase/testUninstallDependents.md) — Tests attempting to uninstall a module that has installed dependents.
- [testModuleMetaData()](ModuleDependencyTestCase/testModuleMetaData.md) — Tests whether the correct module metadata is returned.
- [testThemeMetaData()](ModuleDependencyTestCase/testThemeMetaData.md) — Tests whether the correct theme metadata is returned.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
