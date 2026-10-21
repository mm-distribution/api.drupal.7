# theme_image_resize_summary()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 889–898 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L889-L898)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_resize_summary($variables)
```

## Documentation

```text
Returns HTML for a summary of an image resize effect.

@param $variables
  An associative array containing:
  - data: The current configuration for this resize effect.

@ingroup themeable
```

## Code

```php
function theme_image_resize_summary($variables) {
  $data = $variables['data'];

  if ($data['width'] && $data['height']) {
    return check_plain($data['width']) . 'x' . check_plain($data['height']);
  }
  else {
    return ($data['width']) ? t('width @width', array('@width' => $data['width'])) : t('height @height', array('@height' => $data['height']));
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
