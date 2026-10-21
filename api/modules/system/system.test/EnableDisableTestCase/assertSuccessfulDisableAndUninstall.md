# EnableDisableTestCase::assertSuccessfulDisableAndUninstall()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 313–348 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L313-L348)
- **Class:** [EnableDisableTestCase](../EnableDisableTestCase.md)
- **Module/theme:** system

## Signature

```php
function assertSuccessfulDisableAndUninstall($module)
```

## Documentation

```text
Disables and uninstalls a module and asserts that it was done correctly.

@param $module
  The name of the module to disable and uninstall.
```

## Code

```php
  function assertSuccessfulDisableAndUninstall($module) {
    // Disable the module.
    $edit = array();
    $edit['modules[Core][' . $module . '][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    $this->assertModules(array($module), FALSE);

    // Check that the appropriate hook was fired and the appropriate log
    // message appears.
    $this->assertText(t('hook_modules_disabled fired for @module', array('@module' => $module)));
    $this->assertLogMessage('system', "%module module disabled.", array('%module' => $module), WATCHDOG_INFO);

    //  Check that the module's database tables still exist.
    $this->assertModuleTablesExist($module);

    // Uninstall the module.
    $edit = array();
    $edit['uninstall[' . $module . ']'] = $module;
    $this->drupalPost('admin/modules/uninstall', $edit, t('Uninstall'));
    $this->drupalPost(NULL, NULL, t('Uninstall'));
    $this->assertText(t('The selected modules have been uninstalled.'), 'Modules status has been updated.');
    $this->assertModules(array($module), FALSE);

    // Check that the appropriate hook was fired and the appropriate log
    // message appears. (But don't check for the log message if the dblog
    // module was just uninstalled, since the {watchdog} table won't be there
    // anymore.)
    $this->assertText(t('hook_modules_uninstalled fired for @module', array('@module' => $module)));
    if ($module != 'dblog') {
      $this->assertLogMessage('system', "%module module uninstalled.", array('%module' => $module), WATCHDOG_INFO);
    }

    // Check that the module's database tables no longer exist.
    $this->assertModuleTablesDoNotExist($module);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
