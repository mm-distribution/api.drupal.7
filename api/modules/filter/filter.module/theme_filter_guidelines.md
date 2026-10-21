# theme_filter_guidelines()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1211–1220 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1211-L1220)
- **Module/theme:** filter
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_filter_guidelines($variables)
```

## Documentation

```text
Returns HTML for guidelines for a text format.

@param $variables
  An associative array containing:
  - format: An object representing a text format.

@ingroup themeable
```

## Code

```php
function theme_filter_guidelines($variables) {
  $format = $variables['format'];
  $attributes['class'][] = 'filter-guidelines-item';
  $attributes['class'][] = 'filter-guidelines-' . $format->format;
  $output = '<div' . drupal_attributes($attributes) . '>';
  $output .= '<h3>' . check_plain($format->name) . '</h3>';
  $output .= theme('filter_tips', array('tips' => _filter_tips($format->format, FALSE)));
  $output .= '</div>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
