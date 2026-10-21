# field_sql_storage_field_storage_delete()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 633–642 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L633-L642)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_delete()](../../../field.api.php/hook_field_storage_delete.md)

## Signature

```php
function field_sql_storage_field_storage_delete($entity_type, $entity, $fields)
```

## Documentation

```text
Implements hook_field_storage_delete().

This function deletes data for all fields for an entity from the database.
```

## Code

```php
function field_sql_storage_field_storage_delete($entity_type, $entity, $fields) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    if (isset($fields[$instance['field_id']])) {
      $field = field_info_field_by_id($instance['field_id']);
      field_sql_storage_field_storage_purge($entity_type, $entity, $field, $instance);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
