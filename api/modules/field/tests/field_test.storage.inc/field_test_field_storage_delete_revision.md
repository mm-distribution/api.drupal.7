# field_test_field_storage_delete_revision()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 225–241 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L225-L241)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_delete_revision()](../../field.api.php/hook_field_storage_delete_revision.md)

## Signature

```php
function field_test_field_storage_delete_revision($entity_type, $entity, $fields)
```

## Documentation

```text
Implements hook_field_storage_delete_revision().
```

## Code

```php
function field_test_field_storage_delete_revision($entity_type, $entity, $fields) {
  $data = _field_test_storage_data();

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  foreach ($fields as $field_id) {
    $field_data = &$data[$field_id];
    foreach (array('current', 'revisions') as $sub_table) {
      foreach ($field_data[$sub_table] as $key => $row) {
        if ($row->type == $entity_type && $row->entity_id == $id && $row->revision_id == $vid) {
          unset($field_data[$sub_table][$key]);
        }
      }
    }
  }

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
