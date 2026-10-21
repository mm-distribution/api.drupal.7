# HookRequirementsTestCase::testHookRequirementsFailure()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 366–377 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L366-L377)
- **Class:** [HookRequirementsTestCase](../HookRequirementsTestCase.md)
- **Module/theme:** system

## Signature

```php
function testHookRequirementsFailure()
```

## Documentation

```text
Assert that a module cannot be installed if it fails hook_requirements().
```

## Code

```php
  function testHookRequirementsFailure() {
    $this->assertModules(array('requirements1_test'), FALSE);

    // Attempt to install the requirements1_test module.
    $edit = array();
    $edit['modules[Testing][requirements1_test][enable]'] = 'requirements1_test';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));

    // Makes sure the module was NOT installed.
    $this->assertText(t('Requirements 1 Test failed requirements'), 'Modules status has been updated.');
    $this->assertModules(array('requirements1_test'), FALSE);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
