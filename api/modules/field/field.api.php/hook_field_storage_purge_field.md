# hook_field_storage_purge_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2694–2699 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2694-L2699)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_purge_field($field)
```

## Documentation

```text
Remove field storage information when a field record is purged.

Called from field_purge_field() to allow the field storage module
to remove field information when a field is being purged.

@param $field
  The field being purged.

@ingroup field_storage
```

## Code

```php
function hook_field_storage_purge_field($field) {
  $table_name = _field_sql_storage_tablename($field);
  $revision_name = _field_sql_storage_revision_tablename($field);
  db_drop_table($table_name);
  db_drop_table($revision_name);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_purge_field()".

- [field_sql_storage_field_storage_purge_field()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_purge_field.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
