# hook_field_storage_delete_revision()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2002–2016 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2002-L2016)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_delete_revision($entity_type, $entity, $fields)
```

## Documentation

```text
Delete a single revision of field data for an entity.

This hook is invoked from field_attach_delete_revision() to ask the field
storage module to delete field revision data.

Deleting the current (most recently written) revision is not
allowed as has undefined results.

@param $entity_type
  The entity type of entity, such as 'node' or 'user'.
@param $entity
  The entity on which to operate. The revision to delete is
  indicated by the entity's revision ID property, as identified by
  hook_fieldable_info() for $entity_type.
@param $fields
  An array listing the fields to delete. The keys and values of the
  array are field IDs.
```

## Code

```php
function hook_field_storage_delete_revision($entity_type, $entity, $fields) {
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

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_delete_revision()".

- [field_sql_storage_field_storage_delete_revision()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_delete_revision.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_delete_revision()](../tests/field_test.storage.inc/field_test_field_storage_delete_revision.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
