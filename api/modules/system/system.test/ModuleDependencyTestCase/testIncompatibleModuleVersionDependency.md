# ModuleDependencyTestCase::testIncompatibleModuleVersionDependency()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 459–469 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L459-L469)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testIncompatibleModuleVersionDependency()
```

## Documentation

```text
Tests enabling a module that depends on an incompatible version of a module.
```

## Code

```php
  function testIncompatibleModuleVersionDependency() {
    // Test that the system_incompatible_module_version_dependencies_test is
    // marked as having an incompatible dependency.
    $this->drupalGet('admin/modules');
    $this->assertRaw(t('@module (<span class="admin-missing">incompatible with</span> version @version)', array(
      '@module' => 'System incompatible module version test (>2.0)',
      '@version' => '1.0',
    )), 'A module that depends on an incompatible version of a module is marked as such.');
    $checkbox = $this->xpath('//input[@type="checkbox" and @disabled="disabled" and @name="modules[Testing][system_incompatible_module_version_dependencies_test][enable]"]');
    $this->assert(count($checkbox) == 1, 'Checkbox for the module is disabled.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
