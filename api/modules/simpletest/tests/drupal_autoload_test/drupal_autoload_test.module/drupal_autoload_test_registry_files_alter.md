# drupal_autoload_test_registry_files_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module`](_file.md), lines 11–22 · [local source](../../../../../../source/modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module#L11-L22)
- **Module/theme:** drupal_autoload_test
- **Implements:** [hook_registry_files_alter()](../../../../system/system.api.php/hook_registry_files_alter.md)

## Signature

```php
function drupal_autoload_test_registry_files_alter(&$files, $modules)
```

## Documentation

```text
Implements hook_registry_files_alter().
```

## Code

```php
function drupal_autoload_test_registry_files_alter(&$files, $modules) {
  foreach ($modules as $module) {
    // Add the drupal_autoload_test_trait.sh file to the registry when PHP 5.4+
    // is being used.
    if ($module->name == 'drupal_autoload_test' && version_compare(PHP_VERSION, '5.4') >= 0) {
      $files["$module->dir/drupal_autoload_test_trait.sh"] = array(
        'module' => $module->name,
        'weight' => $module->weight,
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
