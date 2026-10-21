# theme_pager_last()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 596–614 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L596-L614)
- **Topics:** [pagerpieces](../../topics/pagerpieces.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_pager_last($variables)
```

## Documentation

```text
Returns HTML for the "last page" link in query pager.

@param $variables
  An associative array containing:
  - text: The name (or image) of the link.
  - element: An optional integer to distinguish between multiple pagers on
    one page.
  - parameters: An associative array of query string parameters to append to
    the pager links.

@ingroup themeable
```

## Code

```php
function theme_pager_last($variables) {
  $text = $variables['text'];
  $element = $variables['element'];
  $parameters = $variables['parameters'];
  global $pager_page_array, $pager_total;
  $output = '';

  // Nothing to do if there is no pager.
  if (!isset($pager_page_array[$element]) || !isset($pager_total[$element])) {
    return;
  }

  // If we are anywhere but the last page
  if ($pager_page_array[$element] < ($pager_total[$element] - 1)) {
    $output = theme('pager_link', array('text' => $text, 'page_new' => pager_load_array($pager_total[$element] - 1, $element, $pager_page_array), 'element' => $element, 'parameters' => $parameters));
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
