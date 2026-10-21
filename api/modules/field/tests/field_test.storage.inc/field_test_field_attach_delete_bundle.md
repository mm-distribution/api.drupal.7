# field_test_field_attach_delete_bundle()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 350–368 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L350-L368)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_attach_delete_bundle()](../../field.api.php/hook_field_attach_delete_bundle.md)

## Signature

```php
function field_test_field_attach_delete_bundle($entity_type, $bundle, $instances)
```

## Documentation

```text
Implements hook_field_attach_delete_bundle().
```

## Code

```php
function field_test_field_attach_delete_bundle($entity_type, $bundle, $instances) {
  $data = _field_test_storage_data();

  foreach ($instances as $instance) {
    $field = field_info_field_by_id($instance['field_id']);
    if ($field['storage']['type'] == 'field_test_storage') {
      $field_data = &$data[$field['id']];
      foreach (array('current', 'revisions') as $sub_table) {
        foreach ($field_data[$sub_table] as &$row) {
          if ($row->bundle == $bundle) {
            $row->deleted = TRUE;
          }
        }
      }
    }
  }

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
