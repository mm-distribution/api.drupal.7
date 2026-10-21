# theme_image_crop_summary()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 923–925 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L923-L925)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_crop_summary($variables)
```

## Documentation

```text
Returns HTML for a summary of an image crop effect.

@param $variables
  An associative array containing:
  - data: The current configuration for this crop effect.

@ingroup themeable
```

## Code

```php
function theme_image_crop_summary($variables) {
  return theme('image_resize_summary', $variables);
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
