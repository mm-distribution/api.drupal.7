# theme_menu_admin_overview()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 36–41 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L36-L41)
- **Module/theme:** menu
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_menu_admin_overview($variables)
```

## Documentation

```text
Returns HTML for a menu title and description for the menu overview page.

@param $variables
  An associative array containing:
  - title: The menu's title.
  - description: The menu's description.

@ingroup themeable
```

## Code

```php
function theme_menu_admin_overview($variables) {
  $output = check_plain($variables['title']);
  $output .= '<div class="description">' . filter_xss_admin($variables['description']) . '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
