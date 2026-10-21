# theme_menu_link()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1649–1658 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1649-L1658)
- **Topics:** [menu](../../topics/menu.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_menu_link(array $variables)
```

## Documentation

```text
Returns HTML for a menu link and submenu.

@param $variables
  An associative array containing:
  - element: Structured array data for a menu link.

@ingroup themeable
```

## Code

```php
function theme_menu_link(array $variables) {
  $element = $variables['element'];
  $sub_menu = '';

  if ($element['#below']) {
    $sub_menu = drupal_render($element['#below']);
  }
  $output = l($element['#title'], $element['#href'], $element['#localized_options']);
  return '<li' . drupal_attributes($element['#attributes']) . '>' . $output . $sub_menu . "</li>\n";
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
