# theme_menu_local_action()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1703–1719 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1703-L1719)
- **Topics:** [menu](../../topics/menu.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_menu_local_action($variables)
```

## Documentation

```text
Returns HTML for a single local action link.

@param $variables
  An associative array containing:
  - element: A render element containing:
    - #link: A menu link array with 'title', 'href', and 'localized_options'
      keys.

@ingroup themeable
```

## Code

```php
function theme_menu_local_action($variables) {
  $link = $variables['element']['#link'];

  $output = '<li>';
  if (isset($link['href'])) {
    $output .= l($link['title'], $link['href'], isset($link['localized_options']) ? $link['localized_options'] : array());
  }
  elseif (!empty($link['localized_options']['html'])) {
    $output .= $link['title'];
  }
  else {
    $output .= check_plain($link['title']);
  }
  $output .= "</li>\n";

  return $output;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
