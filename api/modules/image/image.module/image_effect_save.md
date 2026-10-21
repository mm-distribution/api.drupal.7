# image_effect_save()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1383–1393 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1383-L1393)
- **Module/theme:** image

## Signature

```php
function image_effect_save($effect)
```

## Documentation

```text
Saves an image effect.

@param $effect
  An image effect array.

@return
  An image effect array. In the case of a new effect, 'ieid' will be set.
```

## Code

```php
function image_effect_save($effect) {
  if (!empty($effect['ieid'])) {
    drupal_write_record('image_effects', $effect, 'ieid');
  }
  else {
    drupal_write_record('image_effects', $effect);
  }
  $style = image_style_load(NULL, $effect['isid']);
  image_style_flush($style);
  return $effect;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
