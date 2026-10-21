# image_module_styles_test_image_default_styles()

- **Type:** Function
- **File:** [`modules/image/tests/image_module_styles_test.module`](_file.md), lines 11–29 · [local source](../../../../../source/modules/image/tests/image_module_styles_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_styles_test.module#L11-L29)
- **Module/theme:** image_module_styles_test
- **Implements:** [hook_image_default_styles()](../../image.api.php/hook_image_default_styles.md)

## Signature

```php
function image_module_styles_test_image_default_styles()
```

## Documentation

```text
Implements hook_image_default_styles().
```

## Code

```php
function image_module_styles_test_image_default_styles() {
  $styles = array();

  $styles['test_image_style'] = array(
    'label' => 'Test Image Style',
    'effects' => array(
      array(
        'name' => 'image_scale',
        'data' => array('width' => 100, 'height' => 100, 'upscale' => 1),
        'weight' => 0,
      ),
      array(
        'name' => 'image_module_test_null',
      ),
    )
  );

  return $styles;
}
```

---
_Drupal 7.103 · [modules/image/tests/image_module_styles_test.module](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_styles_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
