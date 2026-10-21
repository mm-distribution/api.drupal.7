# image_module_test_image_effect_info_alter()

- **Type:** Function
- **File:** [`modules/image/tests/image_module_test.module`](_file.md), lines 51–54 · [local source](../../../../../source/modules/image/tests/image_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module#L51-L54)
- **Module/theme:** image_module_styles_test
- **Implements:** [hook_image_effect_info_alter()](../../image.api.php/hook_image_effect_info_alter.md)

## Signature

```php
function image_module_test_image_effect_info_alter(&$effects)
```

## Documentation

```text
Implements hook_image_effect_info_alter().

Used to keep a count of cache misses in image_effect_definitions().
```

## Code

```php
function image_module_test_image_effect_info_alter(&$effects) {
  $image_effects_definition_called = &drupal_static(__FUNCTION__, 0);
  $image_effects_definition_called++;
}
```

---
_Drupal 7.103 · [modules/image/tests/image_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
