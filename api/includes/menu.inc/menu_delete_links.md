# menu_delete_links()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3055–3065 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3055-L3065)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_delete_links($menu_name)
```

## Documentation

```text
Deletes all links for a menu.

@param $menu_name
  The name of the menu whose links will be deleted.
```

## Code

```php
function menu_delete_links($menu_name) {
  $links = menu_load_links($menu_name);
  foreach ($links as $link) {
    // To speed up the deletion process, we reset some link properties that
    // would trigger re-parenting logic in _menu_delete_item() and
    // _menu_update_parental_status().
    $link['has_children'] = FALSE;
    $link['plid'] = 0;
    _menu_delete_item($link);
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
