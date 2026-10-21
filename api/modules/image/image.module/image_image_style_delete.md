# image_image_style_delete()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 419–421 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L419-L421)
- **Module/theme:** image
- **Implements:** [hook_image_style_delete()](../image.api.php/hook_image_style_delete.md)

## Signature

```php
function image_image_style_delete($style)
```

## Documentation

```text
Implements hook_image_style_delete().
```

## Code

```php
function image_image_style_delete($style) {
  image_image_style_save($style);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
