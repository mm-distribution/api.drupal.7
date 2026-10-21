# image_rotate_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 636–665 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L636-L665)
- **Module/theme:** image

## Signature

```php
function image_rotate_form($data)
```

## Documentation

```text
Form structure for the image rotate form.

Note that this is not a complete form, it only contains the portion of the
form for configuring the rotate options. Therefore it does not not need to
include metadata about the effect, nor a submit button.

@param $data
  The current configuration for this rotate effect.
```

## Code

```php
function image_rotate_form($data) {
  $form['degrees'] = array(
    '#type' => 'textfield',
    '#default_value' => (isset($data['degrees'])) ? $data['degrees'] : 0,
    '#title' => t('Rotation angle'),
    '#description' => t('The number of degrees the image should be rotated. Positive numbers are clockwise, negative are counter-clockwise.'),
    '#field_suffix' => '&deg;',
    '#required' => TRUE,
    '#size' => 6,
    '#maxlength' => 4,
    '#element_validate' => array('image_effect_integer_validate'),
    '#allow_negative' => TRUE,
  );
  $form['bgcolor'] = array(
    '#type' => 'textfield',
    '#default_value' => (isset($data['bgcolor'])) ? $data['bgcolor'] : '#FFFFFF',
    '#title' => t('Background color'),
    '#description' => t('The background color to use for exposed areas of the image. Use web-style hex colors (#FFFFFF for white, #000000 for black). Leave blank for transparency on image types that support it.'),
    '#size' => 7,
    '#maxlength' => 7,
    '#element_validate' => array('image_effect_color_validate'),
  );
  $form['random'] = array(
    '#type' => 'checkbox',
    '#default_value' => (isset($data['random'])) ? $data['random'] : 0,
    '#title' => t('Randomize'),
    '#description' => t('Randomize the rotation angle for each image. The angle specified above is used as a maximum.'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
