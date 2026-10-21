# ModuleDependencyTestCase::testIncompatibleCoreVersionDependency()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 474–483 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L474-L483)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testIncompatibleCoreVersionDependency()
```

## Documentation

```text
Tests enabling a module that depends on a module with an incompatible core version.
```

## Code

```php
  function testIncompatibleCoreVersionDependency() {
    // Test that the system_incompatible_core_version_dependencies_test is
    // marked as having an incompatible dependency.
    $this->drupalGet('admin/modules');
    $this->assertRaw(t('@module (<span class="admin-missing">incompatible with</span> this version of Drupal core)', array(
      '@module' => 'System incompatible core version test',
    )), 'A module that depends on a module with an incompatible core version is marked as such.');
    $checkbox = $this->xpath('//input[@type="checkbox" and @disabled="disabled" and @name="modules[Testing][system_incompatible_core_version_dependencies_test][enable]"]');
    $this->assert(count($checkbox) == 1, 'Checkbox for the module is disabled.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
