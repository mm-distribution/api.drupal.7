# _update_7000_field_sql_storage_write()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.install`](_file.md), lines 35–82 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install#L35-L82)
- **Module/theme:** field_sql_storage
- **Topics:** [update_api](../../../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_sql_storage_write($entity_type, $bundle, $entity_id, $revision_id, $field_name, $data)
```

## Documentation

```text
Utility function: write field data directly to SQL storage.

This function can be used for databases whose schema is at field module
version 7000 or higher.

@ingroup update_api
```

## Code

```php
function _update_7000_field_sql_storage_write($entity_type, $bundle, $entity_id, $revision_id, $field_name, $data) {
  $table_name = "field_data_{$field_name}";
  $revision_name = "field_revision_{$field_name}";

  db_delete($table_name)
    ->condition('entity_type', $entity_type)
    ->condition('entity_id', $entity_id)
    ->execute();
  db_delete($revision_name)
    ->condition('entity_type', $entity_type)
    ->condition('entity_id', $entity_id)
    ->condition('revision_id', $revision_id)
    ->execute();

  $columns = array();
  foreach ($data as $langcode => $items) {
    foreach ($items as $delta => $item) {
      $record = array(
        'entity_type' => $entity_type,
        'entity_id' => $entity_id,
        'revision_id' => $revision_id,
        'bundle' => $bundle,
        'delta' => $delta,
        'language' => $langcode,
      );
      foreach ($item as $column => $value) {
        $record[_field_sql_storage_columnname($field_name, $column)] = $value;
      }

      $records[] = $record;
      // Record the columns used.
      $columns += $record;
    }
  }

  if ($columns) {
    $query = db_insert($table_name)->fields(array_keys($columns));
    $revision_query = db_insert($revision_name)->fields(array_keys($columns));
    foreach ($records as $record) {
      $query->values($record);
      if ($revision_id) {
        $revision_query->values($record);
      }
    }
    $query->execute();
    $revision_query->execute();
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install) · Licensed GPL-2.0-or-later (see LICENSE)._
