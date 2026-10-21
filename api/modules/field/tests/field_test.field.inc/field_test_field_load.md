# field_test_field_load()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 62–78 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L62-L78)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_load()](../../field.api.php/hook_field_load.md)

## Signature

```php
function field_test_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age)
```

## Documentation

```text
Implements hook_field_load().
```

## Code

```php
function field_test_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);

  foreach ($items as $id => $item) {
    // To keep the test non-intrusive, only act for instances with the
    // test_hook_field_load setting explicitly set to TRUE.
    if ($instances[$id]['settings']['test_hook_field_load']) {
      foreach ($item as $delta => $value) {
        // Don't add anything on empty values.
        if ($value) {
          $items[$id][$delta]['additional_key'] = 'additional_value';
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
