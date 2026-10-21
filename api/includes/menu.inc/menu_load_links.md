# menu_load_links()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3033–3047 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3033-L3047)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_load_links($menu_name)
```

## Documentation

```text
Returns an array containing all links for a menu.

@param $menu_name
  The name of the menu whose links should be returned.

@return
  An array of menu links.
```

## Code

```php
function menu_load_links($menu_name) {
  $links = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC))
    ->fields('ml')
    ->condition('ml.menu_name', $menu_name)
    // Order by weight so as to be helpful for menus that are only one level
    // deep.
    ->orderBy('weight')
    ->execute()
    ->fetchAll();

  foreach ($links as &$link) {
    $link['options'] = unserialize($link['options']);
  }
  return $links;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
