# theme_text_format_wrapper()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1007–1017 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1007-L1017)
- **Module/theme:** filter
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_text_format_wrapper($variables)
```

## Documentation

```text
Returns HTML for a text format-enabled form element.

@param $variables
  An associative array containing:
  - element: A render element containing #children and #description.

@ingroup themeable
```

## Code

```php
function theme_text_format_wrapper($variables) {
  $element = $variables['element'];
  $output = '<div class="text-format-wrapper">';
  $output .= $element['#children'];
  if (!empty($element['#description'])) {
    $output .= '<div class="description">' . $element['#description'] . '</div>';
  }
  $output .= "</div>\n";

  return $output;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
