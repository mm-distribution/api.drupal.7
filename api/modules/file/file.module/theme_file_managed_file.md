# theme_file_managed_file()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 734–752 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L734-L752)
- **Module/theme:** file
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_file_managed_file($variables)
```

## Documentation

```text
Returns HTML for a managed file element.

@param $variables
  An associative array containing:
  - element: A render element representing the file.

@ingroup themeable
```

## Code

```php
function theme_file_managed_file($variables) {
  $element = $variables['element'];

  $attributes = array();
  if (isset($element['#id'])) {
    $attributes['id'] = $element['#id'];
  }
  if (!empty($element['#attributes']['class'])) {
    $attributes['class'] = (array) $element['#attributes']['class'];
  }
  $attributes['class'][] = 'form-managed-file';

  // This wrapper is required to apply JS behaviors and CSS styling.
  $output = '';
  $output .= '<div' . drupal_attributes($attributes) . '>';
  $output .= drupal_render_children($element);
  $output .= '</div>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
