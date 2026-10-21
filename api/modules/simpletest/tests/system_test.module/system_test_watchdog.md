# system_test_watchdog()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 589–604 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L589-L604)
- **Module/theme:** batch_test
- **Implements:** [hook_watchdog()](../../../system/system.api.php/hook_watchdog.md)

## Signature

```php
function system_test_watchdog($log_entry)
```

## Documentation

```text
Implements hook_watchdog().
```

## Code

```php
function system_test_watchdog($log_entry) {
  // If an attempted recursive schema rebuild has been triggered by
  // system_test_drupal_get_filename_with_schema_rebuild(), perform the rebuild
  // in response to the missing file message triggered by system_test_schema().
  if (!variable_get('system_test_drupal_get_filename_attempt_recursive_rebuild')) {
    return;
  }
  if ($log_entry['type'] != 'php' || $log_entry['severity'] != WATCHDOG_WARNING) {
    return;
  }
  $module_name = variable_get('system_test_drupal_get_filename_test_module_name');
  if (!isset($log_entry['variables']['!message']) || strpos($log_entry['variables']['!message'], format_string('The following module is missing from the file system: %name', array('%name' => $module_name))) === FALSE) {
    return;
  }
  variable_set('system_test_drupal_get_filename_with_schema_rebuild_final_tables', array_keys(drupal_get_schema()));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
