# field_test_delete_bundle()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 202–211 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L202-L211)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_delete_bundle($bundle)
```

## Documentation

```text
Deletes a bundle for test_entity objects.

@param $bundle
  The machine-readable name of the bundle to delete.
```

## Code

```php
function field_test_delete_bundle($bundle) {
  $bundles = variable_get('field_test_bundles', array('test_bundle' => array('label' => 'Test Bundle')));
  unset($bundles[$bundle]);
  variable_set('field_test_bundles', $bundles);

  $info = field_test_entity_info();
  foreach ($info as $type => $type_info) {
    field_attach_delete_bundle($type, $bundle);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
