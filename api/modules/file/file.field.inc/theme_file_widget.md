# theme_file_widget()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 806–820 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L806-L820)
- **Module/theme:** file
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_file_widget($variables)
```

## Documentation

```text
Returns HTML for an individual file upload widget.

@param $variables
  An associative array containing:
  - element: A render element representing the widget.

@ingroup themeable
```

## Code

```php
function theme_file_widget($variables) {
  $element = $variables['element'];
  $output = '';

  // The "form-managed-file" class is required for proper Ajax functionality.
  $output .= '<div class="file-widget form-managed-file clearfix">';
  if ($element['fid']['#value'] != 0) {
    // Add the file size after the file name.
    $element['filename']['#markup'] .= ' <span class="file-size">(' . format_size($element['#file']->filesize) . ')</span> ';
  }
  $output .= drupal_render_children($element);
  $output .= '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
