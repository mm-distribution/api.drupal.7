# list_allowed_values_setting_validate()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 160–198 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L160-L198)
- **Module/theme:** list

## Signature

```php
function list_allowed_values_setting_validate($element, &$form_state)
```

## Documentation

```text
Element validate callback; check that the entered values are valid.
```

## Code

```php
function list_allowed_values_setting_validate($element, &$form_state) {
  $field = $element['#field'];
  $has_data = $element['#field_has_data'];
  $field_type = $field['type'];
  $generate_keys = ($field_type == 'list_integer' || $field_type == 'list_float') && !$has_data;

  $values = list_extract_allowed_values($element['#value'], $field['type'], $generate_keys);

  if (!is_array($values)) {
    form_error($element, t('Allowed values list: invalid input.'));
  }
  else {
    // Check that keys are valid for the field type.
    foreach ($values as $key => $value) {
      if ($field_type == 'list_integer' && !preg_match('/^-?\d+$/', $key)) {
        form_error($element, t('Allowed values list: keys must be integers.'));
        break;
      }
      if ($field_type == 'list_float' && !is_numeric($key)) {
        form_error($element, t('Allowed values list: each key must be a valid integer or decimal.'));
        break;
      }
      elseif ($field_type == 'list_text' && drupal_strlen($key) > 255) {
        form_error($element, t('Allowed values list: each key must be a string at most 255 characters long.'));
        break;
      }
    }

    // Prevent removing values currently in use.
    if ($has_data) {
      $lost_keys = array_diff(array_keys($field['settings']['allowed_values']), array_keys($values));
      if (_list_values_in_use($field, $lost_keys)) {
        form_error($element, t('Allowed values list: some values are being removed while currently in use.'));
      }
    }

    form_set_value($element, $values, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
