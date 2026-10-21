# field_sql_storage_field_storage_create_field()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 278–284 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L278-L284)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_create_field()](../../../field.api.php/hook_field_storage_create_field.md)

## Signature

```php
function field_sql_storage_field_storage_create_field($field)
```

## Documentation

```text
Implements hook_field_storage_create_field().
```

## Code

```php
function field_sql_storage_field_storage_create_field($field) {
  $schema = _field_sql_storage_schema($field);
  foreach ($schema as $name => $table) {
    db_create_table($name, $table);
  }
  drupal_get_schema(NULL, TRUE);
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
