# field_test_rename_bundle()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 184–194 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L184-L194)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_rename_bundle($bundle_old, $bundle_new)
```

## Documentation

```text
Renames a bundle for test_entity entities.

@param $bundle_old
  The machine-readable name of the bundle to rename.
@param $bundle_new
  The new machine-readable name of the bundle.
```

## Code

```php
function field_test_rename_bundle($bundle_old, $bundle_new) {
  $bundles = variable_get('field_test_bundles', array('test_bundle' => array('label' => 'Test Bundle')));
  $bundles[$bundle_new] = $bundles[$bundle_old];
  unset($bundles[$bundle_old]);
  variable_set('field_test_bundles', $bundles);

  $info = field_test_entity_info();
  foreach ($info as $type => $type_info) {
    field_attach_rename_bundle($type, $bundle_old, $bundle_new);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
