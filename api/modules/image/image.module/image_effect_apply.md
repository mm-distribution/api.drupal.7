# image_effect_apply()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1418–1425 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1418-L1425)
- **Module/theme:** image

## Signature

```php
function image_effect_apply($image, $effect)
```

## Documentation

```text
Applies an image effect to the image object.

@param $image
  An image object returned by image_load().
@param $effect
  An image effect array.

@return
  TRUE on success. FALSE if unable to perform the image effect on the image.
```

## Code

```php
function image_effect_apply($image, $effect) {
  module_load_include('inc', 'image', 'image.effects');
  $function = $effect['effect callback'];
  if (function_exists($function)) {
    return $function($image, $effect['data']);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
