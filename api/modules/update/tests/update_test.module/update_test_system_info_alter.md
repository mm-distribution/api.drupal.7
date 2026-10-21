# update_test_system_info_alter()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 51–60 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L51-L60)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_system_info_alter()](../../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function update_test_system_info_alter(&$info, $file)
```

## Documentation

```text
Implements hook_system_info_alter().

Checks the 'update_test_system_info' variable and sees if we need to alter
the system info for the given $file based on the setting. The setting is
expected to be a nested associative array. If the key '#all' is defined, its
subarray will include .info keys and values for all modules and themes on the
system. Otherwise, the settings array is keyed by the module or theme short
name ($file->name) and the subarrays contain settings just for that module or
theme.
```

## Code

```php
function update_test_system_info_alter(&$info, $file) {
  $setting = variable_get('update_test_system_info', array());
  foreach (array('#all', $file->name) as $id) {
    if (!empty($setting[$id])) {
      foreach ($setting[$id] as $key => $value) {
        $info[$key] = $value;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
