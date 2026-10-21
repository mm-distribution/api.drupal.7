# field_test_field_storage_delete_instance()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 299–313 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L299-L313)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_delete_instance()](../../field.api.php/hook_field_storage_delete_instance.md)

## Signature

```php
function field_test_field_storage_delete_instance($instance)
```

## Documentation

```text
Implements hook_field_storage_delete_instance().
```

## Code

```php
function field_test_field_storage_delete_instance($instance) {
  $data = _field_test_storage_data();

  $field = field_info_field($instance['field_name']);
  $field_data = &$data[$field['id']];
  foreach (array('current', 'revisions') as $sub_table) {
    foreach ($field_data[$sub_table] as &$row) {
      if ($row->bundle == $instance['bundle']) {
        $row->deleted = TRUE;
      }
    }
  }

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
