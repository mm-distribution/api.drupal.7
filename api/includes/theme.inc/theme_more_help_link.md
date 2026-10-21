# theme_more_help_link()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2278–2280 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2278-L2280)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_more_help_link($variables)
```

## Documentation

```text
Returns HTML for a "more help" link.

@param $variables
  An associative array containing:
  - url: The URL for the link.
```

## Code

```php
function theme_more_help_link($variables) {
  return '<div class="more-help-link">' . l(t('More help'), $variables['url']) . '</div>';
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
