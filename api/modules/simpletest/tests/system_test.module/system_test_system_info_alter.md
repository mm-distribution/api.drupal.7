# system_test_system_info_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 342–376 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L342-L376)
- **Module/theme:** batch_test
- **Implements:** [hook_system_info_alter()](../../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function system_test_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().
```

## Code

```php
function system_test_system_info_alter(&$info, $file, $type) {
  // We need a static otherwise the last test will fail to alter common_test.
  static $test;
  if (($dependencies = variable_get('dependencies', array())) || $test) {
    if ($file->name == 'module_test') {
      $info['hidden'] = FALSE;
      $info['dependencies'][] = array_shift($dependencies);
      variable_set('dependencies', $dependencies);
      $test = TRUE;
    }
    if ($file->name == 'common_test') {
      $info['hidden'] = FALSE;
      $info['version'] = '7.x-2.4-beta3';
    }
  }

  if ($file->name == 'system_project_namespace_test') {
    $info['hidden'] = FALSE;
  }
  // Make the system_dependencies_test visible by default.
  if ($file->name == 'system_dependencies_test') {
    $info['hidden'] = FALSE;
  }
  if (in_array($file->name, array(
    'system_incompatible_module_version_dependencies_test',
    'system_incompatible_core_version_dependencies_test',
    'system_incompatible_module_version_test',
    'system_incompatible_core_version_test',
  ))) {
    $info['hidden'] = FALSE;
  }
  if ($file->name == 'requirements1_test' || $file->name == 'requirements2_test') {
    $info['hidden'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
