# user_image_style_save()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3758–3763 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3758-L3763)
- **Module/theme:** user
- **Implements:** [hook_image_style_save()](../../image/image.api.php/hook_image_style_save.md)

## Signature

```php
function user_image_style_save($style)
```

## Documentation

```text
Implements hook_image_style_save().
```

## Code

```php
function user_image_style_save($style) {
  // If a style is renamed, update the variables that use it.
  if (isset($style['old_name']) && $style['old_name'] == variable_get('user_picture_style', '')) {
    variable_set('user_picture_style', $style['name']);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
