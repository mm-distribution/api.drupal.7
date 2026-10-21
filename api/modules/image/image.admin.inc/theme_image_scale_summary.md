# theme_image_scale_summary()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 909–912 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L909-L912)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_scale_summary($variables)
```

## Documentation

```text
Returns HTML for a summary of an image scale effect.

@param $variables
  An associative array containing:
  - data: The current configuration for this scale effect.

@ingroup themeable
```

## Code

```php
function theme_image_scale_summary($variables) {
  $data = $variables['data'];
  return theme('image_resize_summary', array('data' => $data)) . ' ' . ($data['upscale'] ? '(' . t('upscaling allowed') . ')' : '');
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
