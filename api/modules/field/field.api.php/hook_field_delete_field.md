# hook_field_delete_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2591–2593 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2591-L2593)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_delete_field($field)
```

## Documentation

```text
Act on a field being deleted.

This hook is invoked just after a field is deleted by field_delete_field().

@param $field
  The field just deleted.
```

## Code

```php
function hook_field_delete_field($field) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_delete_field()".

- [image_field_delete_field()](../../image/image.module/image_field_delete_field.md) — `modules/image/image.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
