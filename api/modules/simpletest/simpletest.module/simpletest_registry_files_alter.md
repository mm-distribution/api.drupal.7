# simpletest_registry_files_alter()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 497–512 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L497-L512)
- **Module/theme:** simpletest
- **Implements:** [hook_registry_files_alter()](../../system/system.api.php/hook_registry_files_alter.md)

## Signature

```php
function simpletest_registry_files_alter(&$files, $modules)
```

## Documentation

```text
Implements hook_registry_files_alter().

Add the test files for disabled modules so that we get a list containing
all the available tests.
```

## Code

```php
function simpletest_registry_files_alter(&$files, $modules) {
  foreach ($modules as $module) {
    // Only add test files for disabled modules, as enabled modules should
    // already include any test files they provide.
    if (!$module->status) {
      $dir = $module->dir;
      if (!empty($module->info['files'])) {
        foreach ($module->info['files'] as $file) {
          if (substr($file, -5) == '.test') {
            $files["$dir/$file"] = array('module' => $module->name, 'weight' => $module->weight);
          }
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
