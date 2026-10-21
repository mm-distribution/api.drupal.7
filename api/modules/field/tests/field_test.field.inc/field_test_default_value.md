# field_test_default_value()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 401–403 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L401-L403)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_default_value($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Sample 'default value' callback.
```

## Code

```php
function field_test_default_value($entity_type, $entity, $field, $instance) {
  return array(array('value' => 99));
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
