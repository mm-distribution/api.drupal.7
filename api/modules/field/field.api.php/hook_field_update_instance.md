# hook_field_update_instance()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2606–2608 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2606-L2608)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_update_instance($instance, $prior_instance)
```

## Documentation

```text
Act on a field instance being updated.

This hook is invoked from field_update_instance() after the instance record
is saved, so it cannot be used by a module to modify the instance itself.

@param $instance
  The instance as it is post-update.
@param $prior_instance
  The instance as it was pre-update.
```

## Code

```php
function hook_field_update_instance($instance, $prior_instance) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_update_instance()".

- [image_field_update_instance()](../../image/image.module/image_field_update_instance.md) — `modules/image/image.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
