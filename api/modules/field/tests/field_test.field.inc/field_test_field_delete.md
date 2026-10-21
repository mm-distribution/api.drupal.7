# field_test_field_delete()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 99–102 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L99-L102)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_delete()](../../field.api.php/hook_field_delete.md)

## Signature

```php
function field_test_field_delete($entity_type, $entity, $field, $instance, $items)
```

## Documentation

```text
Implements hook_field_delete().
```

## Code

```php
function field_test_field_delete($entity_type, $entity, $field, $instance, $items) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
