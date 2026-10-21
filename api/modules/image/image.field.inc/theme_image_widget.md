# theme_image_widget()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 459–479 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L459-L479)
- **Module/theme:** image
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_image_widget($variables)
```

## Documentation

```text
Returns HTML for an image field widget.

@param $variables
  An associative array containing:
  - element: A render element representing the image field widget.

@ingroup themeable
```

## Code

```php
function theme_image_widget($variables) {
  $element = $variables['element'];
  $output = '';
  $output .= '<div class="image-widget form-managed-file clearfix">';

  if (isset($element['preview'])) {
    $output .= '<div class="image-preview">';
    $output .= drupal_render($element['preview']);
    $output .= '</div>';
  }

  $output .= '<div class="image-widget-data">';
  if ($element['fid']['#value'] != 0) {
    $element['filename']['#markup'] .= ' <span class="file-size">(' . format_size($element['#file']->filesize) . ')</span> ';
  }
  $output .= drupal_render_children($element);
  $output .= '</div>';
  $output .= '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
