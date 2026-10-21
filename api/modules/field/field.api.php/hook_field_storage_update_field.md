# hook_field_storage_update_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 584–602 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L584-L602)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_storage_update_field($field, $prior_field, $has_data)
```

## Documentation

```text
Update the storage information for a field.

This is invoked on the field's storage module from field_update_field(),
before the new field information is saved to the database. The field storage
module should update its storage tables to agree with the new field
information. If there is a problem, the field storage module should throw an
exception.

@param $field
  The updated field structure to be saved.
@param $prior_field
  The previously-saved field structure.
@param $has_data
  TRUE if the field has data in storage currently.
```

## Code

```php
function hook_field_storage_update_field($field, $prior_field, $has_data) {
  if (!$has_data) {
    // There is no data. Re-create the tables completely.
    $prior_schema = _field_sql_storage_schema($prior_field);
    foreach ($prior_schema as $name => $table) {
      db_drop_table($name, $table);
    }
    $schema = _field_sql_storage_schema($field);
    foreach ($schema as $name => $table) {
      db_create_table($name, $table);
    }
  }
  else {
    // There is data. See field_sql_storage_field_storage_update_field() for
    // an example of what to do to modify the schema in place, preserving the
    // old data as much as possible.
  }
  drupal_get_schema(NULL, TRUE);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_update_field()".

- [field_sql_storage_field_storage_update_field()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_update_field.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
