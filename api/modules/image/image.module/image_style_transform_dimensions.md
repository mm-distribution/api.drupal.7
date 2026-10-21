# image_style_transform_dimensions()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1030–1050 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1030-L1050)
- **Module/theme:** image

## Signature

```php
function image_style_transform_dimensions($style_name, array &$dimensions)
```

## Documentation

```text
Determines the dimensions of the styled image.

Applies all of an image style's effects to $dimensions.

@param $style_name
  The name of the style to be applied.
@param $dimensions
  Dimensions to be modified - an array with components width and height, in
  pixels.
```

## Code

```php
function image_style_transform_dimensions($style_name, array &$dimensions) {
  module_load_include('inc', 'image', 'image.effects');
  $style = image_style_load($style_name);

  if (!is_array($style)) {
    return;
  }

  foreach ($style['effects'] as $effect) {
    if (isset($effect['dimensions passthrough'])) {
      continue;
    }

    if (isset($effect['dimensions callback'])) {
      $effect['dimensions callback']($dimensions, $effect['data']);
    }
    else {
      $dimensions['width'] = $dimensions['height'] = NULL;
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
