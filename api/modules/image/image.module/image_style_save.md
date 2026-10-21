# image_style_save()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 695–721 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L695-L721)
- **Module/theme:** image

## Signature

```php
function image_style_save($style)
```

## Documentation

```text
Saves an image style.

@param array $style
  An image style array containing:
  - name: A unique name for the style.
  - isid: (optional) An image style ID.

@return array
  An image style array containing:
  - name: An unique name for the style.
  - old_name: The original name for the style.
  - isid: An image style ID.
  - is_new: TRUE if this is a new style, and FALSE if it is an existing
    style.
```

## Code

```php
function image_style_save($style) {
  if (isset($style['isid']) && is_numeric($style['isid'])) {
    // Load the existing style to make sure we account for renamed styles.
    $old_style = image_style_load(NULL, $style['isid']);
    image_style_flush($old_style);
    drupal_write_record('image_styles', $style, 'isid');
    if ($old_style['name'] != $style['name']) {
      $style['old_name'] = $old_style['name'];
    }
  }
  else {
    // Add a default label when not given.
    if (empty($style['label'])) {
      $style['label'] = $style['name'];
    }
    drupal_write_record('image_styles', $style);
    $style['is_new'] = TRUE;
  }

  // Let other modules update as necessary on save.
  module_invoke_all('image_style_save', $style);

  // Clear all caches and flush.
  image_style_flush($style);

  return $style;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
