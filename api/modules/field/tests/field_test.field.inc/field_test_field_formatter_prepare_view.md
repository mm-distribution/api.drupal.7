# field_test_field_formatter_prepare_view()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 349–362 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L349-L362)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_formatter_prepare_view()](../../field.api.php/hook_field_formatter_prepare_view.md)

## Signature

```php
function field_test_field_formatter_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $displays)
```

## Documentation

```text
Implements hook_field_formatter_prepare_view().
```

## Code

```php
function field_test_field_formatter_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $displays) {
  foreach ($items as $id => $item) {
    // To keep the test non-intrusive, only act on the
    // 'field_test_with_prepare_view' formatter.
    if ($displays[$id]['type'] == 'field_test_with_prepare_view') {
      foreach ($item as $delta => $value) {
        // Don't add anything on empty values.
        if ($value) {
          $items[$id][$delta]['additional_formatter_value'] = $value['value'] + 1;
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
