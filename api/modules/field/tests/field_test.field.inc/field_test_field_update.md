# field_test_field_update()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 91–94 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L91-L94)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_update()](../../field.api.php/hook_field_update.md)

## Signature

```php
function field_test_field_update($entity_type, $entity, $field, $instance, $items)
```

## Documentation

```text
Implements hook_field_update().
```

## Code

```php
function field_test_field_update($entity_type, $entity, $field, $instance, $items) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
