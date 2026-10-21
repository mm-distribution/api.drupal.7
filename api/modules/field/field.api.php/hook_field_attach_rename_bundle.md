# hook_field_attach_rename_bundle()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1634–1644 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1634-L1644)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new)
```

## Documentation

```text
Act on field_attach_rename_bundle().

This hook is invoked after the field module has performed the operation.

See field_attach_rename_bundle() for details and arguments.
```

## Code

```php
function hook_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new) {
  // Update the extra weights variable with new information.
  if ($bundle_old !== $bundle_new) {
    $extra_weights = variable_get('field_extra_weights', array());
    if (isset($info[$entity_type][$bundle_old])) {
      $extra_weights[$entity_type][$bundle_new] = $extra_weights[$entity_type][$bundle_old];
      unset($extra_weights[$entity_type][$bundle_old]);
      variable_set('field_extra_weights', $extra_weights);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_rename_bundle()".

- [field_sql_storage_field_attach_rename_bundle()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_attach_rename_bundle.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_attach_rename_bundle()](../tests/field_test.storage.inc/field_test_field_attach_rename_bundle.md) — `modules/field/tests/field_test.storage.inc`
- [field_ui_field_attach_rename_bundle()](../../field_ui/field_ui.module/field_ui_field_attach_rename_bundle.md) — `modules/field_ui/field_ui.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
