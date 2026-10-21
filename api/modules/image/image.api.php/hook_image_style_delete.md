# hook_image_style_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 97–103 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L97-L103)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_style_delete($style)
```

## Documentation

```text
Respond to image style deletion.

This hook enables modules to update settings when a image style is being
deleted. If a style is deleted, a replacement name may be specified in
$style['name'] and the style being deleted will be specified in
$style['old_name'].

@param $style
  The image style array that being deleted.
```

## Code

```php
function hook_image_style_delete($style) {
  // Administrators can choose an optional replacement style when deleting.
  // Update the modules style variable accordingly.
  if (isset($style['old_name']) && $style['old_name'] == variable_get('mymodule_image_style', '')) {
    variable_set('mymodule_image_style', $style['name']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_style_delete()".

- [image_image_style_delete()](../image.module/image_image_style_delete.md) — `modules/image/image.module`
- [user_image_style_delete()](../../user/user.module/user_image_style_delete.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
