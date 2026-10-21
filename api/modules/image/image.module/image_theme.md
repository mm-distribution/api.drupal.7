# image_theme()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 186–235 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L186-L235)
- **Module/theme:** image
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function image_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function image_theme() {
  return array(
    // Theme functions in image.module.
    'image_style' => array(
      'variables' => array(
        'style_name' => NULL,
        'path' => NULL,
        'width' => NULL,
        'height' => NULL,
        'alt' => '',
        'title' => NULL,
        'attributes' => array(),
      ),
    ),

    // Theme functions in image.admin.inc.
    'image_style_list' => array(
      'variables' => array('styles' => NULL),
    ),
    'image_style_effects' => array(
      'render element' => 'form',
    ),
    'image_style_preview' => array(
      'variables' => array('style' => NULL),
    ),
    'image_anchor' => array(
      'render element' => 'element',
    ),
    'image_resize_summary' => array(
      'variables' => array('data' => NULL),
    ),
    'image_scale_summary' => array(
      'variables' => array('data' => NULL),
    ),
    'image_crop_summary' => array(
      'variables' => array('data' => NULL),
    ),
    'image_rotate_summary' => array(
      'variables' => array('data' => NULL),
    ),

    // Theme functions in image.field.inc.
    'image_widget' => array(
      'render element' => 'element',
    ),
    'image_formatter' => array(
      'variables' => array('item' => NULL, 'path' => NULL, 'image_style' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
