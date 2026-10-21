# image_default_style_revert()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1217–1224 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1217-L1224)
- **Module/theme:** image

## Signature

```php
function image_default_style_revert($style)
```

## Documentation

```text
Reverts the changes made by users to a default image style.

@param style
  An image style array.
@return
  Boolean TRUE if the operation succeeded.
```

## Code

```php
function image_default_style_revert($style) {
  image_style_flush($style);

  db_delete('image_effects')->condition('isid', $style['isid'])->execute();
  db_delete('image_styles')->condition('isid', $style['isid'])->execute();

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
