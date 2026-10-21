# hook_image_default_styles()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 176–196 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L176-L196)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_default_styles()
```

## Documentation

```text
Provide module-based image styles for reuse throughout Drupal.

This hook allows your module to provide image styles. This may be useful if
you require images to fit within exact dimensions. Note that you should
attempt to re-use the default styles provided by Image module whenever
possible, rather than creating image styles that are specific to your module.
Image provides the styles "thumbnail", "medium", and "large".

You may use this hook to more easily manage your site's changes by moving
existing image styles from the database to a custom module. Note however that
moving image styles to code instead storing them in the database has a
negligible effect on performance, since custom image styles are loaded
from the database all at once. Even if all styles are pulled from modules,
Image module will still perform the same queries to check the database for
any custom styles.

@return
  An array of image styles, keyed by the style name.
@see image_image_default_styles()
```

## Code

```php
function hook_image_default_styles() {
  $styles = array();

  $styles['mymodule_preview'] = array(
    'label' => 'My module preview',
    'effects' => array(
      array(
        'name' => 'image_scale',
        'data' => array('width' => 400, 'height' => 400, 'upscale' => 1),
        'weight' => 0,
      ),
      array(
        'name' => 'image_desaturate',
        'data' => array(),
        'weight' => 1,
      ),
    ),
  );

  return $styles;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_default_styles()".

- [image_image_default_styles()](../image.module/image_image_default_styles.md) — `modules/image/image.module`
- [image_module_styles_test_image_default_styles()](../tests/image_module_styles_test.module/image_module_styles_test_image_default_styles.md) — `modules/image/tests/image_module_styles_test.module`

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
