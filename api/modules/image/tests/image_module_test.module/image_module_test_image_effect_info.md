# image_module_test_image_effect_info()

- **Type:** Function
- **File:** [`modules/image/tests/image_module_test.module`](_file.md), lines 20–29 · [local source](../../../../../source/modules/image/tests/image_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module#L20-L29)
- **Module/theme:** image_module_styles_test
- **Implements:** [hook_image_effect_info()](../../image.api.php/hook_image_effect_info.md)

## Signature

```php
function image_module_test_image_effect_info()
```

## Documentation

```text
Implements hook_image_effect_info().
```

## Code

```php
function image_module_test_image_effect_info() {
  $effects = array(
    'image_module_test_null' => array(
      'label' => 'image_module_test_null',
      'effect callback' => 'image_module_test_null_effect',
    ),
  );

  return $effects;
}
```

---
_Drupal 7.103 · [modules/image/tests/image_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
