# user_image_style_delete()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3749–3753 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3749-L3753)
- **Module/theme:** user
- **Implements:** [hook_image_style_delete()](../../image/image.api.php/hook_image_style_delete.md)

## Signature

```php
function user_image_style_delete($style)
```

## Documentation

```text
Implements hook_image_style_delete().
```

## Code

```php
function user_image_style_delete($style) {
  // If a style is deleted, update the variables.
  // Administrators choose a replacement style when deleting.
  user_image_style_save($style);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
