# ModuleDependencyTestCase::testMissingModules()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 433–454 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L433-L454)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testMissingModules()
```

## Documentation

```text
Attempt to enable a module with a missing dependency.
```

## Code

```php
  function testMissingModules() {
    // Test that the system_dependencies_test module is marked
    // as missing a dependency.
    $this->drupalGet('admin/modules');
    $this->assertRaw(t('@module (<span class="admin-missing">missing</span>)', array('@module' => drupal_ucfirst('_missing_dependency'))), 'A module with missing dependencies is marked as such.');
    $checkbox = $this->xpath('//input[@type="checkbox" and @disabled="disabled" and @name="modules[Testing][system_dependencies_test][enable]"]');
    $this->assert(count($checkbox) == 1, 'Checkbox for the module is disabled.');

    // Force enable the system_dependencies_test module.
    module_enable(array('system_dependencies_test'), FALSE);

    // Verify that the module is forced to be disabled when submitting
    // the module page.
    $this->drupalPost('admin/modules', array(), t('Save configuration'));
    $this->assertText(t('The @module module is missing, so the following module will be disabled: @depends.', array('@module' => '_missing_dependency', '@depends' => 'system_dependencies_test')), 'The module missing dependencies will be disabled.');

    // Confirm.
    $this->drupalPost(NULL, NULL, t('Continue'));

    // Verify that the module has been disabled.
    $this->assertModules(array('system_dependencies_test'), FALSE);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
