# update_test_update_status_alter()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 72–85 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L72-L85)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_update_status_alter()](../../update.api.php/hook_update_status_alter.md)

## Signature

```php
function update_test_update_status_alter(&$projects)
```

## Documentation

```text
Implements hook_update_status_alter().

Checks the 'update_test_update_status' variable and sees if we need to alter
the update status for the given project based on the setting. The setting is
expected to be a nested associative array. If the key '#all' is defined, its
subarray will include .info keys and values for all modules and themes on the
system. Otherwise, the settings array is keyed by the module or theme short
name and the subarrays contain settings just for that module or theme.
```

## Code

```php
function update_test_update_status_alter(&$projects) {
  $setting = variable_get('update_test_update_status', array());
  if (!empty($setting)) {
    foreach ($projects as $project_name => &$project) {
      foreach (array('#all', $project_name) as $id) {
        if (!empty($setting[$id])) {
          foreach ($setting[$id] as $key => $value) {
            $project[$key] = $value;
          }
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
