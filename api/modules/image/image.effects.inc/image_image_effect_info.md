# image_image_effect_info()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 11–62 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L11-L62)
- **Module/theme:** image
- **Implements:** [hook_image_effect_info()](../image.api.php/hook_image_effect_info.md)

## Signature

```php
function image_image_effect_info()
```

## Documentation

```text
Implements hook_image_effect_info().
```

## Code

```php
function image_image_effect_info() {
  $effects = array(
    'image_resize' => array(
      'label' => t('Resize'),
      'help' => t('Resizing will make images an exact set of dimensions. This may cause images to be stretched or shrunk disproportionately.'),
      'effect callback' => 'image_resize_effect',
      'dimensions callback' => 'image_resize_dimensions',
      'form callback' => 'image_resize_form',
      'summary theme' => 'image_resize_summary',
    ),
    'image_scale' => array(
      'label' => t('Scale'),
      'help' => t('Scaling will maintain the aspect-ratio of the original image. If only a single dimension is specified, the other dimension will be calculated.'),
      'effect callback' => 'image_scale_effect',
      'dimensions callback' => 'image_scale_dimensions',
      'form callback' => 'image_scale_form',
      'summary theme' => 'image_scale_summary',
    ),
    'image_scale_and_crop' => array(
      'label' => t('Scale and crop'),
      'help' => t('Scale and crop will maintain the aspect-ratio of the original image, then crop the larger dimension. This is most useful for creating perfectly square thumbnails without stretching the image.'),
      'effect callback' => 'image_scale_and_crop_effect',
      'dimensions callback' => 'image_resize_dimensions',
      'form callback' => 'image_resize_form',
      'summary theme' => 'image_resize_summary',
    ),
    'image_crop' => array(
      'label' => t('Crop'),
      'help' => t('Cropping will remove portions of an image to make it the specified dimensions.'),
      'effect callback' => 'image_crop_effect',
      'dimensions callback' => 'image_resize_dimensions',
      'form callback' => 'image_crop_form',
      'summary theme' => 'image_crop_summary',
    ),
    'image_desaturate' => array(
      'label' => t('Desaturate'),
      'help' => t('Desaturate converts an image to grayscale.'),
      'effect callback' => 'image_desaturate_effect',
      'dimensions passthrough' => TRUE,
    ),
    'image_rotate' => array(
      'label' => t('Rotate'),
      'help' => t('Rotating an image may cause the dimensions of an image to increase to fit the diagonal.'),
      'effect callback' => 'image_rotate_effect',
      'dimensions callback' => 'image_rotate_dimensions',
      'form callback' => 'image_rotate_form',
      'summary theme' => 'image_rotate_summary',
    ),
  );

  return $effects;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
