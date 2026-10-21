# theme_more_link()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2345–2347 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2345-L2347)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_more_link($variables)
```

## Documentation

```text
Returns HTML for a "more" link, like those used in blocks.

@param $variables
  An associative array containing:
  - url: The URL of the main page.
  - title: A descriptive verb for the link, like 'Read more'.
```

## Code

```php
function theme_more_link($variables) {
  return '<div class="more-link">' . l(t('More'), $variables['url'], array('attributes' => array('title' => $variables['title']))) . '</div>';
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
