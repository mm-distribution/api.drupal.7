# field_has_data()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 953–967 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L953-L967)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_has_data($field)
```

## Documentation

```text
Determine whether a field has any data.

@param $field
  A field structure.
@return
  TRUE if the field has data for any entity; FALSE otherwise.
```

## Code

```php
function field_has_data($field) {
  $query = new EntityFieldQuery();
  $query = $query->fieldCondition($field)
    ->range(0, 1)
    ->count()
    // Neutralize the 'entity_field_access' query tag added by
    // field_sql_storage_field_storage_query(). The result cannot depend on the
    // access grants of the current user.
    ->addTag('DANGEROUS_ACCESS_CHECK_OPT_OUT');

  return (bool) $query
    ->execute() || (bool) $query
    ->age(FIELD_LOAD_REVISION)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
