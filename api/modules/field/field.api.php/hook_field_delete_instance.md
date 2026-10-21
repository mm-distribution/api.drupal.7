# hook_field_delete_instance()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2619–2621 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2619-L2621)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_delete_instance($instance)
```

## Documentation

```text
Act on a field instance being deleted.

This hook is invoked from field_delete_instance() after the instance is
deleted.

@param $instance
  The instance just deleted.
```

## Code

```php
function hook_field_delete_instance($instance) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_delete_instance()".

- [image_field_delete_instance()](../../image/image.module/image_field_delete_instance.md) — `modules/image/image.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
