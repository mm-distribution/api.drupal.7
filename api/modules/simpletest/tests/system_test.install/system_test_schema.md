# system_test_schema()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.install`](_file.md), lines 11–20 · [local source](../../../../../source/modules/simpletest/tests/system_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.install#L11-L20)
- **Module/theme:** batch_test
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function system_test_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function system_test_schema() {
  // Trigger a search for a module in the filesystem when requested by
  // system_test_drupal_get_filename_with_schema_rebuild().
  if (variable_get('system_test_drupal_get_filename_attempt_recursive_rebuild')) {
    $module_name = variable_get('system_test_drupal_get_filename_test_module_name');
    drupal_get_filename('module', $module_name);
  }

  return array();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
