# hook_field_storage_delete_instance()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2187–2201 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2187-L2201)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_delete_instance($instance)
```

## Documentation

```text
Act on deletion of a field instance.

This hook is invoked from field_delete_instance() to ask the field storage
module to mark all information stored for the field instance for deletion.

@param $instance
  The instance being deleted.
```

## Code

```php
function hook_field_storage_delete_instance($instance) {
  $field = field_info_field($instance['field_name']);
  $table_name = _field_sql_storage_tablename($field);
  $revision_name = _field_sql_storage_revision_tablename($field);
  db_update($table_name)
    ->fields(array('deleted' => 1))
    ->condition('entity_type', $instance['entity_type'])
    ->condition('bundle', $instance['bundle'])
    ->execute();
  db_update($revision_name)
    ->fields(array('deleted' => 1))
    ->condition('entity_type', $instance['entity_type'])
    ->condition('bundle', $instance['bundle'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_delete_instance()".

- [field_sql_storage_field_storage_delete_instance()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_delete_instance.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_delete_instance()](../tests/field_test.storage.inc/field_test_field_storage_delete_instance.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
