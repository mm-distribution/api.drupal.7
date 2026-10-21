# field_test_create_bundle()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 165–174 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L165-L174)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_create_bundle($bundle, $text = NULL)
```

## Documentation

```text
Creates a new bundle for test_entity entities.

@param $bundle
  The machine-readable name of the bundle.
@param $text
  The human-readable name of the bundle. If none is provided, the machine
  name will be used.
```

## Code

```php
function field_test_create_bundle($bundle, $text = NULL) {
  $bundles = variable_get('field_test_bundles', array('test_bundle' => array('label' => 'Test Bundle')));
  $bundles += array($bundle => array('label' => $text ? $text : $bundle));
  variable_set('field_test_bundles', $bundles);

  $info = field_test_entity_info();
  foreach ($info as $type => $type_info) {
    field_attach_create_bundle($type, $bundle);
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
