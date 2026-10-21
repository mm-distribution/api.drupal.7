# menu_overview_title()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 207–209 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L207-L209)
- **Module/theme:** menu

## Signature

```php
function menu_overview_title($menu)
```

## Documentation

```text
Title callback for the menu overview page and links.
```

## Code

```php
function menu_overview_title($menu) {
  return $menu['title'];
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
