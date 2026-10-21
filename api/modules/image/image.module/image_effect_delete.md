# image_effect_delete()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1401–1405 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1401-L1405)
- **Module/theme:** image

## Signature

```php
function image_effect_delete($effect)
```

## Documentation

```text
Deletes an image effect.

@param $effect
  An image effect array.
```

## Code

```php
function image_effect_delete($effect) {
  db_delete('image_effects')->condition('ieid', $effect['ieid'])->execute();
  $style = image_style_load(NULL, $effect['isid']);
  image_style_flush($style);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
