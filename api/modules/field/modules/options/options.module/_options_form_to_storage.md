# _options_form_to_storage()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 311–336 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L311-L336)
- **Module/theme:** options

## Signature

```php
function _options_form_to_storage($element)
```

## Documentation

```text
Transforms submitted form values into field storage format.
```

## Code

```php
function _options_form_to_storage($element) {
  $values = array_values((array) $element['#value']);
  $properties = $element['#properties'];

  // On/off checkbox: transform '0 / 1' into the 'on / off' values.
  if ($element['#type'] == 'checkbox') {
    $values = array($values[0] ? $element['#on_value'] : $element['#off_value']);
  }

  // Filter out the 'none' option. Use a strict comparison, because
  // 0 == 'any string'.
  if ($properties['empty_option']) {
    $index = array_search('_none', $values, TRUE);
    if ($index !== FALSE) {
      unset($values[$index]);
    }
  }

  // Make sure we populate at least an empty value.
  if (empty($values)) {
    $values = array(NULL);
  }

  $result = options_array_transpose(array($element['#value_key'] => $values));
  return $result;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
