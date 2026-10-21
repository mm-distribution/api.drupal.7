# ModuleUnitTest::testModuleList()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 33–85 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L33-L85)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleList()
```

## Documentation

```text
The basic functionality of module_list().
```

## Code

```php
  function testModuleList() {
    // Build a list of modules, sorted alphabetically.
    $profile_info = install_profile_info('standard', 'en');
    $module_list = $profile_info['dependencies'];

    // Installation profile is a module that is expected to be loaded.
    $module_list[] = 'standard';

    sort($module_list);
    // Compare this list to the one returned by module_list(). We expect them
    // to match, since all default profile modules have a weight equal to 0
    // (except for block.module, which has a lower weight but comes first in
    // the alphabet anyway).
    $this->assertModuleList($module_list, t('Standard profile'));

    // Try to install a new module.
    module_enable(array('contact'));
    $module_list[] = 'contact';
    sort($module_list);
    $this->assertModuleList($module_list, t('After adding a module'));

    // Try to mess with the module weights.
    db_update('system')
      ->fields(array('weight' => 20))
      ->condition('name', 'contact')
      ->condition('type', 'module')
      ->execute();
    // Reset the module list.
    module_list(TRUE);
    // Move contact to the end of the array.
    unset($module_list[array_search('contact', $module_list)]);
    $module_list[] = 'contact';
    $this->assertModuleList($module_list, t('After changing weights'));

    // Test the fixed list feature.
    $fixed_list = array(
      'system' => array('filename' => drupal_get_path('module', 'system')),
      'menu' => array('filename' => drupal_get_path('module', 'menu')),
    );
    module_list(FALSE, FALSE, FALSE, $fixed_list);
    $new_module_list = array_combine(array_keys($fixed_list), array_keys($fixed_list));
    $this->assertModuleList($new_module_list, t('When using a fixed list'));

    // Reset the module list.
    module_list(TRUE);
    $this->assertModuleList($module_list, t('After reset'));

    // Verify that the module_list() returns correct bootstrap modules.
    $bootstrap_module_list = module_list(TRUE, TRUE);
    $expected_bootstrap_modules = db_query("SELECT name, filename FROM {system} WHERE status = 1 AND bootstrap = 1 AND type = 'module' ORDER BY weight ASC, name ASC")->fetchAllAssoc('name');
    $expected_bootstrap_module_list = array_combine(array_keys($expected_bootstrap_modules), array_keys($expected_bootstrap_modules));
    $this->assertIdentical($expected_bootstrap_module_list, $bootstrap_module_list, 'module_list() returns correct bootstrap modules.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
