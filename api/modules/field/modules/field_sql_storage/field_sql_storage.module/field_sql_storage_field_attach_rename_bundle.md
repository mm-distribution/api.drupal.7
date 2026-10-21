# field_sql_storage_field_attach_rename_bundle()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 876–896 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L876-L896)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_attach_rename_bundle()](../../../field.api.php/hook_field_attach_rename_bundle.md)

## Signature

```php
function field_sql_storage_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new)
```

## Documentation

```text
Implements hook_field_attach_rename_bundle().
```

## Code

```php
function field_sql_storage_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new) {
  // We need to account for deleted or inactive fields and instances.
  $instances = field_read_instances(array('entity_type' => $entity_type, 'bundle' => $bundle_new), array('include_deleted' => TRUE, 'include_inactive' => TRUE));
  foreach ($instances as $instance) {
    $field = field_info_field_by_id($instance['field_id']);
    if ($field['storage']['type'] == 'field_sql_storage') {
      $table_name = _field_sql_storage_tablename($field);
      $revision_name = _field_sql_storage_revision_tablename($field);
      db_update($table_name)
        ->fields(array('bundle' => $bundle_new))
        ->condition('entity_type', $entity_type)
        ->condition('bundle', $bundle_old)
        ->execute();
      db_update($revision_name)
        ->fields(array('bundle' => $bundle_new))
        ->condition('entity_type', $entity_type)
        ->condition('bundle', $bundle_old)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
