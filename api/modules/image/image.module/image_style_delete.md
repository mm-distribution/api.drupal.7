# image_style_delete()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 735–747 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L735-L747)
- **Module/theme:** image

## Signature

```php
function image_style_delete($style, $replacement_style_name = '')
```

## Documentation

```text
Deletes an image style.

@param $style
  An image style array.
@param $replacement_style_name
  (optional) When deleting a style, specify a replacement style name so
  that existing settings (if any) may be converted to a new style.

@return
  TRUE on success.
```

## Code

```php
function image_style_delete($style, $replacement_style_name = '') {
  image_style_flush($style);

  db_delete('image_effects')->condition('isid', $style['isid'])->execute();
  db_delete('image_styles')->condition('isid', $style['isid'])->execute();

  // Let other modules update as necessary on save.
  $style['old_name'] = $style['name'];
  $style['name'] = $replacement_style_name;
  module_invoke_all('image_style_delete', $style);

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
