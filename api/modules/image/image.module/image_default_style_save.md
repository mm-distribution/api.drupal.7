# image_default_style_save()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1197–1207 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1197-L1207)
- **Module/theme:** image

## Signature

```php
function image_default_style_save($style)
```

## Documentation

```text
Saves a default image style to the database.

@param style
  An image style array provided by a module.

@return
  An image style array. The returned style array will include the new 'isid'
  assigned to the style.
```

## Code

```php
function image_default_style_save($style) {
  $style = image_style_save($style);
  $effects = array();
  foreach ($style['effects'] as $effect) {
    $effect['isid'] = $style['isid'];
    $effect = image_effect_save($effect);
    $effects[$effect['ieid']] = $effect;
  }
  $style['effects'] = $effects;
  return $style;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
