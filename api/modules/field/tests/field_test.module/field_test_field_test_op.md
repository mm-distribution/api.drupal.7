# field_test_field_test_op()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 78–80 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L78-L80)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_field_test_op($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Generic op to test _field_invoke behavior.

This simulates a field operation callback to be invoked by _field_invoke().
```

## Code

```php
function field_test_field_test_op($entity_type, $entity, $field, $instance, $langcode, &$items) {
  return array($langcode => hash('sha256', serialize(array($entity_type, $entity, $field['field_name'], $langcode, $items))));
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
