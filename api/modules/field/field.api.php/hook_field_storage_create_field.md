# hook_field_storage_create_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2143–2149 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2143-L2149)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_create_field($field)
```

## Documentation

```text
Act on creation of a new field.

This hook is invoked from field_create_field() to ask the field storage
module to save field information and prepare for storing field instances.
If there is a problem, the field storage module should throw an exception.

@param $field
  The field structure being created.
```

## Code

```php
function hook_field_storage_create_field($field) {
  $schema = _field_sql_storage_schema($field);
  foreach ($schema as $name => $table) {
    db_create_table($name, $table);
  }
  drupal_get_schema(NULL, TRUE);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_create_field()".

- [field_sql_storage_field_storage_create_field()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_create_field.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_create_field()](../tests/field_test.storage.inc/field_test_field_storage_create_field.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
