# field_test_field_is_empty()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 127–129 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L127-L129)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_is_empty()](../../field.api.php/hook_field_is_empty.md)

## Signature

```php
function field_test_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function field_test_field_is_empty($item, $field) {
  return empty($item['value']);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
