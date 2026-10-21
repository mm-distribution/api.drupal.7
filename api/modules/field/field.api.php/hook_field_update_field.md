# hook_field_update_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2578–2581 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2578-L2581)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_update_field($field, $prior_field, $has_data)
```

## Documentation

```text
Act on a field being updated.

This hook is invoked just after field is updated in field_update_field().

@param $field
  The field as it is post-update.
@param $prior_field
  The field as it was pre-update.
@param $has_data
  Whether any data already exists for this field.
```

## Code

```php
function hook_field_update_field($field, $prior_field, $has_data) {
  // Reset the static value that keeps track of allowed values for list fields.
  drupal_static_reset('list_allowed_values');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_update_field()".

- [image_field_update_field()](../../image/image.module/image_field_update_field.md) — `modules/image/image.module`
- [list_field_update_field()](../modules/list/list.module/list_field_update_field.md) — `modules/field/modules/list/list.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
