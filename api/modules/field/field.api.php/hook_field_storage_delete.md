# hook_field_storage_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1972–1981 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1972-L1981)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_delete($entity_type, $entity, $fields)
```

## Documentation

```text
Delete all field data for an entity.

This hook is invoked from field_attach_delete() to ask the field storage
module to delete field data.

@param $entity_type
  The entity type of entity, such as 'node' or 'user'.
@param $entity
  The entity on which to operate.
@param $fields
  An array listing the fields to delete. The keys and values of the
  array are field IDs.
```

## Code

```php
function hook_field_storage_delete($entity_type, $entity, $fields) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    if (isset($fields[$instance['field_id']])) {
      $field = field_info_field_by_id($instance['field_id']);
      field_sql_storage_field_storage_purge($entity_type, $entity, $field, $instance);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_delete()".

- [field_sql_storage_field_storage_delete()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_delete.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_delete()](../tests/field_test.storage.inc/field_test_field_storage_delete.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
