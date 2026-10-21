# field_test_field_storage_purge()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 205–220 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L205-L220)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_purge()](../../field.api.php/hook_field_storage_purge.md)

## Signature

```php
function field_test_field_storage_purge($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Implements hook_field_storage_purge().
```

## Code

```php
function field_test_field_storage_purge($entity_type, $entity, $field, $instance) {
  $data = _field_test_storage_data();

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  $field_data = &$data[$field['id']];
  foreach (array('current', 'revisions') as $sub_table) {
    foreach ($field_data[$sub_table] as $key => $row) {
      if ($row->type == $entity_type && $row->entity_id == $id) {
        unset($field_data[$sub_table][$key]);
      }
    }
  }

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
