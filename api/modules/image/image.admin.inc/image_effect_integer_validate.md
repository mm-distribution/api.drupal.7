# image_effect_integer_validate()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 494–504 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L494-L504)
- **Module/theme:** image

## Signature

```php
function image_effect_integer_validate($element, &$form_state)
```

## Documentation

```text
Element validate handler to ensure an integer pixel value.

The property #allow_negative = TRUE may be set to allow negative integers.
```

## Code

```php
function image_effect_integer_validate($element, &$form_state) {
  $value = empty($element['#allow_negative']) ? $element['#value'] : preg_replace('/^-/', '', $element['#value']);
  if ($element['#value'] != '' && (!is_numeric($value) || intval($value) <= 0)) {
    if (empty($element['#allow_negative'])) {
      form_error($element, t('!name must be an integer.', array('!name' => $element['#title'])));
    }
    else {
      form_error($element, t('!name must be a positive integer.', array('!name' => $element['#title'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
