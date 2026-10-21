# menu_reset_static_cache()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2736–2743 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2736-L2743)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_reset_static_cache()
```

## Documentation

```text
Resets the menu system static cache.
```

## Code

```php
function menu_reset_static_cache() {
  drupal_static_reset('_menu_build_tree');
  drupal_static_reset('menu_tree');
  drupal_static_reset('menu_tree_all_data');
  drupal_static_reset('menu_tree_page_data');
  drupal_static_reset('menu_load_all');
  drupal_static_reset('menu_link_get_preferred');
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
