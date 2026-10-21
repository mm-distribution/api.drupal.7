# image_scale_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 572–584 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L572-L584)
- **Module/theme:** image

## Signature

```php
function image_scale_form($data)
```

## Documentation

```text
Form structure for the image scale form.

Note that this is not a complete form, it only contains the portion of the
form for configuring the scale options. Therefore it does not not need to
include metadata about the effect, nor a submit button.

@param $data
  The current configuration for this scale effect.
```

## Code

```php
function image_scale_form($data) {
  $form = image_resize_form($data);
  $form['#element_validate'] = array('image_effect_scale_validate');
  $form['width']['#required'] = FALSE;
  $form['height']['#required'] = FALSE;
  $form['upscale'] = array(
    '#type' => 'checkbox',
    '#default_value' => (isset($data['upscale'])) ? $data['upscale'] : 0,
    '#title' => t('Allow Upscaling'),
    '#description' => t('Let scale make images larger than their original size'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
