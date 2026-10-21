# theme_pager_previous()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 510–538 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L510-L538)
- **Topics:** [pagerpieces](../../topics/pagerpieces.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_pager_previous($variables)
```

## Documentation

```text
Returns HTML for the "previous page" link in a query pager.

@param $variables
  An associative array containing:
  - text: The name (or image) of the link.
  - element: An optional integer to distinguish between multiple pagers on
    one page.
  - interval: The number of pages to move backward when the link is clicked.
  - parameters: An associative array of query string parameters to append to
    the pager links.

@ingroup themeable
```

## Code

```php
function theme_pager_previous($variables) {
  $text = $variables['text'];
  $element = $variables['element'];
  $interval = $variables['interval'];
  $parameters = $variables['parameters'];
  global $pager_page_array;
  $output = '';

  // Nothing to do if there is no pager.
  if (!isset($pager_page_array[$element])) {
    return;
  }

  // If we are anywhere but the first page
  if ($pager_page_array[$element] > 0) {
    $page_new = pager_load_array($pager_page_array[$element] - $interval, $element, $pager_page_array);

    // If the previous page is the first page, mark the link as such.
    if ($page_new[$element] == 0) {
      $output = theme('pager_first', array('text' => $text, 'element' => $element, 'parameters' => $parameters));
    }
    // The previous page is not the first page.
    else {
      $output = theme('pager_link', array('text' => $text, 'page_new' => $page_new, 'element' => $element, 'parameters' => $parameters));
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
