# image_image_default_styles()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 346–383 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L346-L383)
- **Module/theme:** image
- **Implements:** [hook_image_default_styles()](../image.api.php/hook_image_default_styles.md)

## Signature

```php
function image_image_default_styles()
```

## Documentation

```text
Implements hook_image_default_styles().
```

## Code

```php
function image_image_default_styles() {
  $styles = array();

  $styles['thumbnail'] = array(
    'label' => 'Thumbnail (100x100)',
    'effects' => array(
      array(
        'name' => 'image_scale',
        'data' => array('width' => 100, 'height' => 100, 'upscale' => 1),
        'weight' => 0,
      ),
    )
  );

  $styles['medium'] = array(
    'label' => 'Medium (220x220)',
    'effects' => array(
      array(
        'name' => 'image_scale',
        'data' => array('width' => 220, 'height' => 220, 'upscale' => 1),
        'weight' => 0,
      ),
    )
  );

  $styles['large'] = array(
    'label' => 'Large (480x480)',
    'effects' => array(
      array(
        'name' => 'image_scale',
        'data' => array('width' => 480, 'height' => 480, 'upscale' => 0),
        'weight' => 0,
      ),
    )
  );

  return $styles;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
