# theme_image_rotate_summary()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 936–939 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L936-L939)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_rotate_summary($variables)
```

## Documentation

```text
Returns HTML for a summary of an image rotate effect.

@param $variables
  An associative array containing:
  - data: The current configuration for this rotate effect.

@ingroup themeable
```

## Code

```php
function theme_image_rotate_summary($variables) {
  $data = $variables['data'];
  return ($data['random']) ? t('random between -@degrees&deg and @degrees&deg', array('@degrees' => str_replace('-', '', $data['degrees']))) : t('@degrees&deg', array('@degrees' => $data['degrees']));
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
