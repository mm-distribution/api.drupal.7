# ModuleUnitTest::testDependencyResolution()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 177–276 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L177-L276)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDependencyResolution()
```

## Documentation

```text
Test dependency resolution.
```

## Code

```php
  function testDependencyResolution() {
    // Enable the test module, and make sure that other modules we are testing
    // are not already enabled. (If they were, the tests below would not work
    // correctly.)
    module_enable(array('module_test'), FALSE);
    $this->assertTrue(module_exists('module_test'), 'Test module is enabled.');
    $this->assertFalse(module_exists('forum'), 'Forum module is disabled.');
    $this->assertFalse(module_exists('poll'), 'Poll module is disabled.');
    $this->assertFalse(module_exists('php'), 'PHP module is disabled.');

    // First, create a fake missing dependency. Forum depends on poll, which
    // depends on a made-up module, foo. Nothing should be installed.
    variable_set('dependency_test', 'missing dependency');
    drupal_static_reset('system_rebuild_module_data');
    $result = module_enable(array('forum'));
    $this->assertFalse($result, 'module_enable() returns FALSE if dependencies are missing.');
    $this->assertFalse(module_exists('forum'), 'module_enable() aborts if dependencies are missing.');

    // Now, fix the missing dependency. Forum module depends on poll, but poll
    // depends on the PHP module. module_enable() should work.
    variable_set('dependency_test', 'dependency');
    drupal_static_reset('system_rebuild_module_data');
    $result = module_enable(array('forum'));
    $this->assertTrue($result, 'module_enable() returns the correct value.');
    // Verify that the fake dependency chain was installed.
    $this->assertTrue(module_exists('poll') && module_exists('php'), 'Dependency chain was installed by module_enable().');
    // Verify that the original module was installed.
    $this->assertTrue(module_exists('forum'), 'Module installation with unlisted dependencies succeeded.');
    // Finally, verify that the modules were enabled in the correct order.
    $this->assertEqual(variable_get('test_module_enable_order', array()), array('php', 'poll', 'forum'), 'Modules were enabled in the correct order by module_enable().');

    // Now, disable the PHP module. Both forum and poll should be disabled as
    // well, in the correct order.
    module_disable(array('php'));
    $this->assertTrue(!module_exists('forum') && !module_exists('poll'), 'Depedency chain was disabled by module_disable().');
    $this->assertFalse(module_exists('php'), 'Disabling a module with unlisted dependents succeeded.');
    $this->assertEqual(variable_get('test_module_disable_order', array()), array('forum', 'poll', 'php'), 'Modules were disabled in the correct order by module_disable().');

    // Disable a module that is listed as a dependency by the installation
    // profile. Make sure that the profile itself is not on the list of
    // dependent modules to be disabled.
    $profile = drupal_get_profile();
    $info = install_profile_info($profile);
    $this->assertTrue(in_array('comment', $info['dependencies']), 'Comment module is listed as a dependency of the installation profile.');
    $this->assertTrue(module_exists('comment'), 'Comment module is enabled.');
    module_disable(array('comment'));
    $this->assertFalse(module_exists('comment'), 'Comment module was disabled.');
    $disabled_modules = variable_get('test_module_disable_order', array());
    $this->assertTrue(in_array('comment', $disabled_modules), 'Comment module is in the list of disabled modules.');
    $this->assertFalse(in_array($profile, $disabled_modules), 'The installation profile is not in the list of disabled modules.');

    // Try to uninstall the PHP module by itself. This should be rejected,
    // since the modules which it depends on need to be uninstalled first, and
    // that is too destructive to perform automatically.
    $result = drupal_uninstall_modules(array('php'));
    $this->assertFalse($result, 'Calling drupal_uninstall_modules() on a module whose dependents are not uninstalled fails.');
    foreach (array('forum', 'poll', 'php') as $module) {
      $this->assertNotEqual(drupal_get_installed_schema_version($module), SCHEMA_UNINSTALLED, format_string('The @module module was not uninstalled.', array('@module' => $module)));
    }

    // Now uninstall all three modules explicitly, but in the incorrect order,
    // and make sure that drupal_uninstal_modules() uninstalled them in the
    // correct sequence.
    $result = drupal_uninstall_modules(array('poll', 'php', 'forum'));
    $this->assertTrue($result, 'drupal_uninstall_modules() returns the correct value.');
    foreach (array('forum', 'poll', 'php') as $module) {
      $this->assertEqual(drupal_get_installed_schema_version($module), SCHEMA_UNINSTALLED, format_string('The @module module was uninstalled.', array('@module' => $module)));
    }
    $this->assertEqual(variable_get('test_module_uninstall_order', array()), array('forum', 'poll', 'php'), 'Modules were uninstalled in the correct order by drupal_uninstall_modules().');

    // Uninstall the profile module from above, and make sure that the profile
    // itself is not on the list of dependent modules to be uninstalled.
    $result = drupal_uninstall_modules(array('comment'));
    $this->assertTrue($result, 'drupal_uninstall_modules() returns the correct value.');
    $this->assertEqual(drupal_get_installed_schema_version('comment'), SCHEMA_UNINSTALLED, 'Comment module was uninstalled.');
    $uninstalled_modules = variable_get('test_module_uninstall_order', array());
    $this->assertTrue(in_array('comment', $uninstalled_modules), 'Comment module is in the list of uninstalled modules.');
    $this->assertFalse(in_array($profile, $uninstalled_modules), 'The installation profile is not in the list of uninstalled modules.');

    // Enable forum module again, which should enable both the poll module and
    // php module. But, this time do it with poll module declaring a dependency
    // on a specific version of php module in its info file. Make sure that
    // module_enable() still works.
    variable_set('dependency_test', 'version dependency');
    drupal_static_reset('system_rebuild_module_data');
    $result = module_enable(array('forum'));
    $this->assertTrue($result, 'module_enable() returns the correct value.');
    // Verify that the fake dependency chain was installed.
    $this->assertTrue(module_exists('poll') && module_exists('php'), 'Dependency chain was installed by module_enable().');
    // Verify that the original module was installed.
    $this->assertTrue(module_exists('forum'), 'Module installation with version dependencies succeeded.');
    // Finally, verify that the modules were enabled in the correct order.
    $enable_order = variable_get('test_module_enable_order', array());
    $php_position = array_search('php', $enable_order);
    $poll_position = array_search('poll', $enable_order);
    $forum_position = array_search('forum', $enable_order);
    $php_before_poll = $php_position !== FALSE && $poll_position !== FALSE && $php_position < $poll_position;
    $poll_before_forum = $poll_position !== FALSE && $forum_position !== FALSE && $poll_position < $forum_position;
    $this->assertTrue($php_before_poll && $poll_before_forum, 'Modules were enabled in the correct order by module_enable().');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
