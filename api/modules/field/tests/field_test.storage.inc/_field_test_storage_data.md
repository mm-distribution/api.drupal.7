# _field_test_storage_data()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 71–78 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L71-L78)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function _field_test_storage_data($data = NULL)
```

## Documentation

```text
Helper function: stores or retrieves data from the 'storage backend'.
```

## Code

```php
function _field_test_storage_data($data = NULL) {
  if (!isset($data)) {
    return variable_get('field_test_storage_data', array());
  }
  else {
    variable_set('field_test_storage_data', $data);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
