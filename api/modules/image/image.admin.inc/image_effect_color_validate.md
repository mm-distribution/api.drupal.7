# image_effect_color_validate()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 509–516 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L509-L516)
- **Module/theme:** image

## Signature

```php
function image_effect_color_validate($element, &$form_state)
```

## Documentation

```text
Element validate handler to ensure a hexadecimal color value.
```

## Code

```php
function image_effect_color_validate($element, &$form_state) {
  if ($element['#value'] != '') {
    $hex_value = preg_replace('/^#/', '', $element['#value']);
    if (!preg_match('/^#[0-9A-F]{3}([0-9A-F]{3})?$/', $element['#value'])) {
      form_error($element, t('!name must be a hexadecimal color value.', array('!name' => $element['#title'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
