# field_sql_storage_field_storage_delete_revision()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 836–850 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L836-L850)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_delete_revision()](../../../field.api.php/hook_field_storage_delete_revision.md)

## Signature

```php
function field_sql_storage_field_storage_delete_revision($entity_type, $entity, $fields)
```

## Documentation

```text
Implements hook_field_storage_delete_revision().

This function actually deletes the data from the database.
```

## Code

```php
function field_sql_storage_field_storage_delete_revision($entity_type, $entity, $fields) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  if (isset($vid)) {
    foreach ($fields as $field_id) {
      $field = field_info_field_by_id($field_id);
      $revision_name = _field_sql_storage_revision_tablename($field);
      db_delete($revision_name)
        ->condition('entity_type', $entity_type)
        ->condition('entity_id', $id)
        ->condition('revision_id', $vid)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
