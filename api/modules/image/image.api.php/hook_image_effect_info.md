# hook_image_effect_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 38–51 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L38-L51)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_effect_info()
```

## Documentation

```text
Define information about image effects provided by a module.

This hook enables modules to define image manipulation effects for use with
an image style.

@return
  An array of image effects. This array is keyed on the machine-readable
  effect name. Each effect is defined as an associative array containing the
  following items:
  - "label": The human-readable name of the effect.
  - "effect callback": The function to call to perform this image effect.
  - "dimensions passthrough": (optional) Set this item if the effect doesn't
    change the dimensions of the image.
  - "dimensions callback": (optional) The function to call to transform
    dimensions for this effect.
  - "help": (optional) A brief description of the effect that will be shown
    when adding or configuring this image effect.
  - "form callback": (optional) The name of a function that will return a
    $form array providing a configuration form for this image effect.
  - "summary theme": (optional) The name of a theme function that will output
    a summary of this image effect's configuration.

@see hook_image_effect_info_alter()
```

## Code

```php
function hook_image_effect_info() {
  $effects = array();

  $effects['mymodule_resize'] = array(
    'label' => t('Resize'),
    'help' => t('Resize an image to an exact set of dimensions, ignoring aspect ratio.'),
    'effect callback' => 'mymodule_resize_effect',
    'dimensions callback' => 'mymodule_resize_dimensions',
    'form callback' => 'mymodule_resize_form',
    'summary theme' => 'mymodule_resize_summary',
  );

  return $effects;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_effect_info()".

- [image_image_effect_info()](../image.effects.inc/image_image_effect_info.md) — `modules/image/image.effects.inc`
- [image_module_test_image_effect_info()](../tests/image_module_test.module/image_module_test_image_effect_info.md) — `modules/image/tests/image_module_test.module`

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
