# number_field_validate()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 135–152 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L135-L152)
- **Module/theme:** number
- **Implements:** [hook_field_validate()](../../../field.api.php/hook_field_validate.md)

## Signature

```php
function number_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Implements hook_field_validate().

Possible error codes:
- 'number_min': The value is less than the allowed minimum value.
- 'number_max': The value is greater than the allowed maximum value.
```

## Code

```php
function number_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  foreach ($items as $delta => $item) {
    if ($item['value'] != '') {
      if (is_numeric($instance['settings']['min']) && $item['value'] < $instance['settings']['min']) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'number_min',
          'message' => t('%name: the value may be no less than %min.', array('%name' => $instance['label'], '%min' => $instance['settings']['min'])),
        );
      }
      if (is_numeric($instance['settings']['max']) && $item['value'] > $instance['settings']['max']) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'number_max',
          'message' => t('%name: the value may be no greater than %max.', array('%name' => $instance['label'], '%max' => $instance['settings']['max'])),
        );
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
