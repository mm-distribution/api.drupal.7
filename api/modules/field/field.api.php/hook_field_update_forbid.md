# hook_field_update_forbid()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2546–2564 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2546-L2564)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_update_forbid($field, $prior_field, $has_data)
```

## Documentation

```text
Forbid a field update from occurring.

Any module may forbid any update for any reason. For example, the
field's storage module might forbid an update if it would change
the storage schema while data for the field exists. A field type
module might forbid an update if it would change existing data's
semantics, or if there are external dependencies on field settings
that cannot be updated.

To forbid the update from occurring, throw a FieldUpdateForbiddenException.

@param $field
  The field as it will be post-update.
@param $prior_field
  The field as it is pre-update.
@param $has_data
  Whether any data already exists for this field.
```

## Code

```php
function hook_field_update_forbid($field, $prior_field, $has_data) {
  // A 'list' field stores integer keys mapped to display values. If
  // the new field will have fewer values, and any data exists for the
  // abandoned keys, the field will have no way to display them. So,
  // forbid such an update.
  if ($has_data && count($field['settings']['allowed_values']) < count($prior_field['settings']['allowed_values'])) {
    // Identify the keys that will be lost.
    $lost_keys = array_diff(array_keys($field['settings']['allowed_values']), array_keys($prior_field['settings']['allowed_values']));
    // If any data exist for those keys, forbid the update.
    $query = new EntityFieldQuery();
    $found = $query
      ->fieldCondition($prior_field['field_name'], 'value', $lost_keys)
      ->range(0, 1)
      ->execute();
    if ($found) {
      throw new FieldUpdateForbiddenException("Cannot update a list field not to include keys with existing data");
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_update_forbid()".

- [field_sql_storage_field_update_forbid()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_update_forbid.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_update_forbid()](../tests/field_test.field.inc/field_test_field_update_forbid.md) — `modules/field/tests/field_test.field.inc`
- [list_field_update_forbid()](../modules/list/list.module/list_field_update_forbid.md) — `modules/field/modules/list/list.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
