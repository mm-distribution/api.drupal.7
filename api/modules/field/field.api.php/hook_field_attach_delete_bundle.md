# hook_field_attach_delete_bundle()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1659–1666 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1659-L1666)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_delete_bundle($entity_type, $bundle, $instances)
```

## Documentation

```text
Act on field_attach_delete_bundle.

This hook is invoked after the field module has performed the operation.

@param $entity_type
  The type of entity; for example, 'node' or 'user'.
@param $bundle
  The name of the bundle that was just deleted.
@param $instances
  An array of all instances that existed for the bundle before it was
  deleted.
```

## Code

```php
function hook_field_attach_delete_bundle($entity_type, $bundle, $instances) {
  // Remove the extra weights variable information for this bundle.
  $extra_weights = variable_get('field_extra_weights', array());
  if (isset($extra_weights[$entity_type][$bundle])) {
    unset($extra_weights[$entity_type][$bundle]);
    variable_set('field_extra_weights', $extra_weights);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_delete_bundle()".

- [field_test_field_attach_delete_bundle()](../tests/field_test.storage.inc/field_test_field_attach_delete_bundle.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
