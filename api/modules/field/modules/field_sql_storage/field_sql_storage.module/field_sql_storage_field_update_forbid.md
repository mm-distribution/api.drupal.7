# field_sql_storage_field_update_forbid()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 292–296 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L292-L296)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_update_forbid()](../../../field.api.php/hook_field_update_forbid.md)

## Signature

```php
function field_sql_storage_field_update_forbid($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_update_forbid().

Forbid any field update that changes column definitions if there is
any data.
```

## Code

```php
function field_sql_storage_field_update_forbid($field, $prior_field, $has_data) {
  if ($has_data && $field['columns'] != $prior_field['columns']) {
    throw new FieldUpdateForbiddenException("field_sql_storage cannot change the schema for an existing field with data.");
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
