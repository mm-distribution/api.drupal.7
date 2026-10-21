# image_crop_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 596–624 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L596-L624)
- **Module/theme:** image

## Signature

```php
function image_crop_form($data)
```

## Documentation

```text
Form structure for the image crop form.

Note that this is not a complete form, it only contains the portion of the
form for configuring the crop options. Therefore it does not not need to
include metadata about the effect, nor a submit button.

@param $data
  The current configuration for this crop effect.
```

## Code

```php
function image_crop_form($data) {
  $data += array(
    'width' => '',
    'height' => '',
    'anchor' => 'center-center',
  );

  $form = image_resize_form($data);
  $form['anchor'] = array(
    '#type' => 'radios',
    '#title' => t('Anchor'),
    '#options' => array(
      'left-top'      => t('Top left'),
      'center-top'    => t('Top center'),
      'right-top'     => t('Top right'),
      'left-center'   => t('Center left'),
      'center-center' => t('Center'),
      'right-center'  => t('Center right'),
      'left-bottom'   => t('Bottom left'),
      'center-bottom' => t('Bottom center'),
      'right-bottom'  => t('Bottom right'),
    ),
    '#theme' => 'image_anchor',
    '#default_value' => $data['anchor'],
    '#description' => t('The part of the image that will be retained during the crop.'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
