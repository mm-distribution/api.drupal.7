# field_test_field_storage_delete()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 189–200 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L189-L200)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_delete()](../../field.api.php/hook_field_storage_delete.md)

## Signature

```php
function field_test_field_storage_delete($entity_type, $entity, $fields)
```

## Documentation

```text
Implements hook_field_storage_delete().
```

## Code

```php
function field_test_field_storage_delete($entity_type, $entity, $fields) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Note: reusing field_test_storage_purge(), like field_sql_storage.module
  // does, is highly inefficient in our case...
  foreach (field_info_instances($bundle) as $instance) {
    if (isset($fields[$instance['field_id']])) {
      $field = field_info_field_by_id($instance['field_id']);
      field_test_field_storage_purge($entity_type, $entity, $field, $instance);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
