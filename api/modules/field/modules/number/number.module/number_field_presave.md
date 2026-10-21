# number_field_presave()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 157–176 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L157-L176)
- **Module/theme:** number
- **Implements:** [hook_field_presave()](../../../field.api.php/hook_field_presave.md)

## Signature

```php
function number_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_presave().
```

## Code

```php
function number_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items) {
  if ($field['type'] == 'number_decimal') {
    // Let PHP round the value to ensure consistent behavior across storage
    // backends.
    foreach ($items as $delta => $item) {
      if (isset($item['value'])) {
        $items[$delta]['value'] = round($item['value'], $field['settings']['scale']);
      }
    }
  }
  if ($field['type'] == 'number_float') {
    // Remove the decimal point from float values with decimal
    // point but no decimal numbers.
    foreach ($items as $delta => $item) {
      if (isset($item['value'])) {
        $items[$delta]['value'] = floatval($item['value']);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
