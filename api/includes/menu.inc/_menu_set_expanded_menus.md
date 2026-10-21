# _menu_set_expanded_menus()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3411–3414 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3411-L3414)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_set_expanded_menus()
```

## Documentation

```text
Updates a list of menus with expanded items.
```

## Code

```php
function _menu_set_expanded_menus() {
  $names = db_query("SELECT menu_name FROM {menu_links} WHERE expanded <> 0 GROUP BY menu_name")->fetchCol();
  variable_set('menu_expanded', $names);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
