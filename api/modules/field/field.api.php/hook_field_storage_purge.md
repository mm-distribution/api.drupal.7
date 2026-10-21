# hook_field_storage_purge()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2736–2749 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2736-L2749)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_purge($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Remove field storage information when field data is purged.

Called from field_purge_data() to allow the field storage
module to delete field data information.

@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The pseudo-entity whose field data to delete.
@param $field
  The (possibly deleted) field whose data is being purged.
@param $instance
  The deleted field instance whose data is being purged.

@ingroup field_storage
```

## Code

```php
function hook_field_storage_purge($entity_type, $entity, $field, $instance) {
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

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_purge()".

- [field_sql_storage_field_storage_purge()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_purge.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_purge()](../tests/field_test.storage.inc/field_test_field_storage_purge.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
