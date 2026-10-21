# hook_image_style_save()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 78–84 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L78-L84)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_style_save($style)
```

## Documentation

```text
Respond to image style updating.

This hook enables modules to update settings that might be affected by
changes to an image. For example, updating a module specific variable to
reflect a change in the image style's name.

@param $style
  The image style array that is being updated.
```

## Code

```php
function hook_image_style_save($style) {
  // If a module defines an image style and that style is renamed by the user
  // the module should update any references to that style.
  if (isset($style['old_name']) && $style['old_name'] == variable_get('mymodule_image_style', '')) {
    variable_set('mymodule_image_style', $style['name']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_style_save()".

- [image_image_style_save()](../image.module/image_image_style_save.md) — `modules/image/image.module`
- [user_image_style_save()](../../user/user.module/user_image_style_save.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
