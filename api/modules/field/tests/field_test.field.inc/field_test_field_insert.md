# field_test_field_insert()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 83–86 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L83-L86)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_insert()](../../field.api.php/hook_field_insert.md)

## Signature

```php
function field_test_field_insert($entity_type, $entity, $field, $instance, $items)
```

## Documentation

```text
Implements hook_field_insert().
```

## Code

```php
function field_test_field_insert($entity_type, $entity, $field, $instance, $items) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
