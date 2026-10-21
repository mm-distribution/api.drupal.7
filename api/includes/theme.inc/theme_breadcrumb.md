# theme_breadcrumb()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1898–1909 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1898-L1909)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_breadcrumb($variables)
```

## Documentation

```text
Returns HTML for a breadcrumb trail.

@param $variables
  An associative array containing:
  - breadcrumb: An array containing the breadcrumb links.
```

## Code

```php
function theme_breadcrumb($variables) {
  $breadcrumb = $variables['breadcrumb'];

  if (!empty($breadcrumb)) {
    // Provide a navigational heading to give context for breadcrumb links to
    // screen-reader users. Make the heading invisible with .element-invisible.
    $output = '<h2 class="element-invisible">' . t('You are here') . '</h2>';

    $output .= '<div class="breadcrumb">' . implode(' » ', $breadcrumb) . '</div>';
    return $output;
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
