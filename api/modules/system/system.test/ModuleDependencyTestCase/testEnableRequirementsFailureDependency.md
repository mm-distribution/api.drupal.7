# ModuleDependencyTestCase::testEnableRequirementsFailureDependency()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 488–507 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L488-L507)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testEnableRequirementsFailureDependency()
```

## Documentation

```text
Tests enabling a module that depends on a module which fails hook_requirements().
```

## Code

```php
  function testEnableRequirementsFailureDependency() {
    $this->assertModules(array('requirements1_test'), FALSE);
    $this->assertModules(array('requirements2_test'), FALSE);

    // Attempt to install both modules at the same time.
    $edit = array();
    $edit['modules[Testing][requirements1_test][enable]'] = 'requirements1_test';
    $edit['modules[Testing][requirements2_test][enable]'] = 'requirements2_test';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));

    // Makes sure the modules were NOT installed.
    $this->assertText(t('Requirements 1 Test failed requirements'), 'Modules status has been updated.');
    $this->assertModules(array('requirements1_test'), FALSE);
    $this->assertModules(array('requirements2_test'), FALSE);

    // Makes sure that already enabled modules the failing modules depend on
    // were not disabled.
    $this->assertModules(array('comment'), TRUE);

  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
