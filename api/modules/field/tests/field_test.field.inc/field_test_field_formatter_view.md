# field_test_field_formatter_view()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 367–396 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L367-L396)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_formatter_view()](../../field.api.php/hook_field_formatter_view.md)

## Signature

```php
function field_test_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function field_test_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();
  $settings = $display['settings'];

  switch ($display['type']) {
    case 'field_test_default':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => $settings['test_formatter_setting'] . '|' . $item['value']);
      }
      break;

    case 'field_test_with_prepare_view':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => $settings['test_formatter_setting_additional'] . '|' . $item['value'] . '|' . $item['additional_formatter_value']);
      }
      break;

    case 'field_test_multiple':
      if (!empty($items)) {
        $array = array();
        foreach ($items as $delta => $item) {
          $array[] = $delta . ':' . $item['value'];
        }
        $element[0] = array('#markup' => $settings['test_formatter_setting_multiple'] . '|' . implode('|', $array));
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
