# hook_field_storage_delete_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2160–2176 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2160-L2176)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_delete_field($field)
```

## Documentation

```text
Act on deletion of a field.

This hook is invoked from field_delete_field() to ask the field storage
module to mark all information stored in the field for deletion.

@param $field
  The field being deleted.
```

## Code

```php
function hook_field_storage_delete_field($field) {
  // Mark all data associated with the field for deletion.
  $field['deleted'] = 0;
  $table = _field_sql_storage_tablename($field);
  $revision_table = _field_sql_storage_revision_tablename($field);
  db_update($table)
    ->fields(array('deleted' => 1))
    ->execute();

  // Move the table to a unique name while the table contents are being deleted.
  $field['deleted'] = 1;
  $new_table = _field_sql_storage_tablename($field);
  $revision_new_table = _field_sql_storage_revision_tablename($field);
  db_rename_table($table, $new_table);
  db_rename_table($revision_table, $revision_new_table);
  drupal_get_schema(NULL, TRUE);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_delete_field()".

- [field_sql_storage_field_storage_delete_field()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_delete_field.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_delete_field()](../tests/field_test.storage.inc/field_test_field_storage_delete_field.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
