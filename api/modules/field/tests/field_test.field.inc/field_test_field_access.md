# field_test_field_access()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 408–413 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L408-L413)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_access()](../../field.api.php/hook_field_access.md)

## Signature

```php
function field_test_field_access($op, $field, $entity_type, $entity, $account)
```

## Documentation

```text
Implements hook_field_access().
```

## Code

```php
function field_test_field_access($op, $field, $entity_type, $entity, $account) {
  if ($field['field_name'] == "field_no_{$op}_access") {
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
