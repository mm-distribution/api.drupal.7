# field_test_field_update_forbid()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 53–57 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L53-L57)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_update_forbid()](../../field.api.php/hook_field_update_forbid.md)

## Signature

```php
function field_test_field_update_forbid($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_update_forbid().
```

## Code

```php
function field_test_field_update_forbid($field, $prior_field, $has_data) {
  if ($field['type'] == 'test_field' && $field['settings']['unchangeable'] != $prior_field['settings']['unchangeable']) {
    throw new FieldException("field_test 'unchangeable' setting cannot be changed'");
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
