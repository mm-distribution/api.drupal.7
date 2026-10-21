# field_sql_storage_field_storage_purge()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 650–663 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L650-L663)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_purge()](../../../field.api.php/hook_field_storage_purge.md)

## Signature

```php
function field_sql_storage_field_storage_purge($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Implements hook_field_storage_purge().

This function deletes data from the database for a single field on
an entity.
```

## Code

```php
function field_sql_storage_field_storage_purge($entity_type, $entity, $field, $instance) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  $table_name = _field_sql_storage_tablename($field);
  $revision_name = _field_sql_storage_revision_tablename($field);
  db_delete($table_name)
    ->condition('entity_type', $entity_type)
    ->condition('entity_id', $id)
    ->execute();
  db_delete($revision_name)
    ->condition('entity_type', $entity_type)
    ->condition('entity_id', $id)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
