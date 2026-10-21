# theme_tablesort_indicator()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2169–2176 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2169-L2176)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_tablesort_indicator($variables)
```

## Documentation

```text
Returns HTML for a sort icon.

@param $variables
  An associative array containing:
  - style: Set to either 'asc' or 'desc', this determines which icon to
    show.
```

## Code

```php
function theme_tablesort_indicator($variables) {
  if ($variables['style'] == "asc") {
    return theme('image', array('path' => 'misc/arrow-asc.png', 'width' => 13, 'height' => 13, 'alt' => t('sort ascending'), 'title' => t('sort ascending')));
  }
  else {
    return theme('image', array('path' => 'misc/arrow-desc.png', 'width' => 13, 'height' => 13, 'alt' => t('sort descending'), 'title' => t('sort descending')));
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
