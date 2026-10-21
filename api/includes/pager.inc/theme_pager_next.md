# theme_pager_next()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 554–581 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L554-L581)
- **Topics:** [pagerpieces](../../topics/pagerpieces.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_pager_next($variables)
```

## Documentation

```text
Returns HTML for the "next page" link in a query pager.

@param $variables
  An associative array containing:
  - text: The name (or image) of the link.
  - element: An optional integer to distinguish between multiple pagers on
    one page.
  - interval: The number of pages to move forward when the link is clicked.
  - parameters: An associative array of query string parameters to append to
    the pager links.

@ingroup themeable
```

## Code

```php
function theme_pager_next($variables) {
  $text = $variables['text'];
  $element = $variables['element'];
  $interval = $variables['interval'];
  $parameters = $variables['parameters'];
  global $pager_page_array, $pager_total;
  $output = '';

  // Nothing to do if there is no pager.
  if (!isset($pager_page_array[$element]) || !isset($pager_total[$element])) {
    return;
  }

  // If we are anywhere but the last page
  if ($pager_page_array[$element] < ($pager_total[$element] - 1)) {
    $page_new = pager_load_array($pager_page_array[$element] + $interval, $element, $pager_page_array);
    // If the next page is the last page, mark the link as such.
    if ($page_new[$element] == ($pager_total[$element] - 1)) {
      $output = theme('pager_last', array('text' => $text, 'element' => $element, 'parameters' => $parameters));
    }
    // The next page is not the last page.
    else {
      $output = theme('pager_link', array('text' => $text, 'page_new' => $page_new, 'element' => $element, 'parameters' => $parameters));
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
