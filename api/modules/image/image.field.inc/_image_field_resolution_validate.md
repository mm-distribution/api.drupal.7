# _image_field_resolution_validate()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 171–193 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L171-L193)
- **Module/theme:** image

## Signature

```php
function _image_field_resolution_validate($element, &$form_state)
```

## Documentation

```text
Element validate function for resolution fields.
```

## Code

```php
function _image_field_resolution_validate($element, &$form_state) {
  if (!empty($element['x']['#value']) || !empty($element['y']['#value'])) {
    foreach (array('x', 'y') as $dimension) {
      $value = $element[$dimension]['#value'];
      if (!is_numeric($value)) {
        form_error($element[$dimension], t('Height and width values must be numeric.'));
        return;
      }
      if (intval($value) < 0) {
        form_error($element[$dimension], t('Height and width values must be positive numbers.'));
        return;
      }
      if (intval($value) == 0) {
        form_error($element[$dimension], t('Both a height and width value must be specified in the !name field.', array('!name' => $element['#title'])));
        return;
      }
    }
    form_set_value($element, intval($element['x']['#value']) . 'x' . intval($element['y']['#value']), $form_state);
  }
  else {
    form_set_value($element, '', $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
