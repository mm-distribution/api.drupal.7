# hook_image_effect_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 61–66 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L61-L66)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_effect_info_alter(&$effects)
```

## Documentation

```text
Alter the information provided in hook_image_effect_info().

@param $effects
  The array of image effects, keyed on the machine-readable effect name.

@see hook_image_effect_info()
```

## Code

```php
function hook_image_effect_info_alter(&$effects) {
  // Override the Image module's crop effect with more options.
  $effects['image_crop']['effect callback'] = 'mymodule_crop_effect';
  $effects['image_crop']['dimensions callback'] = 'mymodule_crop_dimensions';
  $effects['image_crop']['form callback'] = 'mymodule_crop_form';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_effect_info_alter()".

- [image_module_test_image_effect_info_alter()](../tests/image_module_test.module/image_module_test_image_effect_info_alter.md) — `modules/image/tests/image_module_test.module`

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
