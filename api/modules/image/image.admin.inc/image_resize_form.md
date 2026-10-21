# image_resize_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 538–560 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L538-L560)
- **Module/theme:** image

## Signature

```php
function image_resize_form($data)
```

## Documentation

```text
Form structure for the image resize form.

Note that this is not a complete form, it only contains the portion of the
form for configuring the resize options. Therefore it does not not need to
include metadata about the effect, nor a submit button.

@param $data
  The current configuration for this resize effect.
```

## Code

```php
function image_resize_form($data) {
  $form['width'] = array(
    '#type' => 'textfield',
    '#title' => t('Width'),
    '#default_value' => isset($data['width']) ? $data['width'] : '',
    '#field_suffix' => ' ' . t('pixels'),
    '#required' => TRUE,
    '#size' => 10,
    '#element_validate' => array('image_effect_integer_validate'),
    '#allow_negative' => FALSE,
  );
  $form['height'] = array(
    '#type' => 'textfield',
    '#title' => t('Height'),
    '#default_value' => isset($data['height']) ? $data['height'] : '',
    '#field_suffix' => ' ' . t('pixels'),
    '#required' => TRUE,
    '#size' => 10,
    '#element_validate' => array('image_effect_integer_validate'),
    '#allow_negative' => FALSE,
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
