# field_test_field_validate()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 110–122 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L110-L122)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_validate()](../../field.api.php/hook_field_validate.md)

## Signature

```php
function field_test_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Implements hook_field_validate().

Possible error codes:
- 'field_test_invalid': The value is invalid.
```

## Code

```php
function field_test_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);

  foreach ($items as $delta => $item) {
    if ($item['value'] == -1) {
      $errors[$field['field_name']][$langcode][$delta][] = array(
        'error' => 'field_test_invalid',
        'message' => t('%name does not accept the value -1.', array('%name' => $instance['label'])),
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
