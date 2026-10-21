# EnableDisableTestCase::testEnableDisable()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 146–272 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L146-L272)
- **Class:** [EnableDisableTestCase](../EnableDisableTestCase.md)
- **Module/theme:** system

## Signature

```php
function testEnableDisable()
```

## Documentation

```text
Test that all core modules can be enabled, disabled and uninstalled.
```

## Code

```php
  function testEnableDisable() {
    // Try to enable, disable and uninstall all core modules, unless they are
    // hidden or required.
    $modules = system_rebuild_module_data();
    foreach ($modules as $name => $module) {
      if ($module->info['package'] != 'Core' || !empty($module->info['hidden']) || !empty($module->info['required'])) {
        unset($modules[$name]);
      }
    }
    $this->assertTrue(count($modules), format_string('Found @count core modules that we can try to enable in this test.', array('@count' => count($modules))));

    // Enable the dblog module first, since we will be asserting the presence
    // of log messages throughout the test.
   if (isset($modules['dblog'])) {
     $modules = array('dblog' => $modules['dblog']) + $modules;
   }

   // Set a variable so that the hook implementations in system_test.module
   // will display messages via drupal_set_message().
   variable_set('test_verbose_module_hooks', TRUE);

    // Throughout this test, some modules may be automatically enabled (due to
    // dependencies). We'll keep track of them in an array, so we can handle
    // them separately.
    $automatically_enabled = array();

    // Go through each module in the list and try to enable it (unless it was
    // already enabled automatically due to a dependency).
    foreach ($modules as $name => $module) {
      if (empty($automatically_enabled[$name])) {
        // Start a list of modules that we expect to be enabled this time.
        $modules_to_enable = array($name);

        // Find out if the module has any dependencies that aren't enabled yet;
        // if so, add them to the list of modules we expect to be automatically
        // enabled.
        foreach (array_keys($module->requires) as $dependency) {
          if (isset($modules[$dependency]) && empty($automatically_enabled[$dependency])) {
            $modules_to_enable[] = $dependency;
            $automatically_enabled[$dependency] = TRUE;
          }
        }

        // Check that each module is not yet enabled and does not have any
        // database tables yet.
        foreach ($modules_to_enable as $module_to_enable) {
          $this->assertModules(array($module_to_enable), FALSE);
          $this->assertModuleTablesDoNotExist($module_to_enable);
        }

        // Install and enable the module.
        $edit = array();
        $edit['modules[Core][' . $name . '][enable]'] = $name;
        $this->drupalPost('admin/modules', $edit, t('Save configuration'));
        // Handle the case where modules were installed along with this one and
        // where we therefore hit a confirmation screen.
        if (count($modules_to_enable) > 1) {
          $this->drupalPost(NULL, array(), t('Continue'));
        }
        $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');

        // Check that hook_modules_installed() and hook_modules_enabled() were
        // invoked with the expected list of modules, that each module's
        // database tables now exist, and that appropriate messages appear in
        // the logs.
        foreach ($modules_to_enable as $module_to_enable) {
          $this->assertText(t('hook_modules_installed fired for @module', array('@module' => $module_to_enable)));
          $this->assertText(t('hook_modules_enabled fired for @module', array('@module' => $module_to_enable)));
          $this->assertModules(array($module_to_enable), TRUE);
          $this->assertModuleTablesExist($module_to_enable);
          $this->assertLogMessage('system', "%module module installed.", array('%module' => $module_to_enable), WATCHDOG_INFO);
          $this->assertLogMessage('system', "%module module enabled.", array('%module' => $module_to_enable), WATCHDOG_INFO);
        }

        // Disable and uninstall the original module, and check appropriate
        // hooks, tables, and log messages. (Later, we'll go back and do the
        // same thing for modules that were enabled automatically.) Skip this
        // for the dblog module, because that is needed for the test; we'll go
        // back and do that one at the end also.
        if ($name != 'dblog') {
          $this->assertSuccessfulDisableAndUninstall($name);
        }
      }
    }

    // Go through all modules that were automatically enabled, and try to
    // disable and uninstall them one by one.
    while (!empty($automatically_enabled)) {
      $initial_count = count($automatically_enabled);
      foreach (array_keys($automatically_enabled) as $name) {
        // If the module can't be disabled due to dependencies, skip it and try
        // again the next time. Otherwise, try to disable it.
        $this->drupalGet('admin/modules');
        $disabled_checkbox = $this->xpath('//input[@type="checkbox" and @disabled="disabled" and @name="modules[Core][' . $name . '][enable]"]');
        if (empty($disabled_checkbox) && $name != 'dblog') {
          unset($automatically_enabled[$name]);
          $this->assertSuccessfulDisableAndUninstall($name);
        }
      }
      $final_count = count($automatically_enabled);
      // If all checkboxes were disabled, something is really wrong with the
      // test. Throw a failure and avoid an infinite loop.
      if ($initial_count == $final_count) {
        $this->fail(t('Remaining modules could not be disabled.'));
        break;
      }
    }

    // Disable and uninstall the dblog module last, since we needed it for
    // assertions in all the above tests.
    if (isset($modules['dblog'])) {
      $this->assertSuccessfulDisableAndUninstall('dblog');
    }

    // Now that all modules have been tested, go back and try to enable them
    // all again at once. This tests two things:
    // - That each module can be successfully enabled again after being
    //   uninstalled.
    // - That enabling more than one module at the same time does not lead to
    //   any errors.
    $edit = array();
    foreach (array_keys($modules) as $name) {
      $edit['modules[Core][' . $name . '][enable]'] = $name;
    }
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
