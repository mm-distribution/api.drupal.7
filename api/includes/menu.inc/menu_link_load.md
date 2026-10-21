# menu_link_load()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2685–2701 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2685-L2701)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_load($mlid)
```

## Documentation

```text
Gets a translated, access-checked menu link that is ready for rendering.

This function should never be called from within node_load() or any other
function used as a menu object load function since an infinite recursion may
occur.

@param $mlid
  The mlid of the menu item.

@return
  A menu link, with $item['access'] filled and link translated for
  rendering.
```

## Code

```php
function menu_link_load($mlid) {
  if (is_numeric($mlid)) {
    $query = db_select('menu_links', 'ml');
    $query->leftJoin('menu_router', 'm', 'm.path = ml.router_path');
    $query->fields('ml');
    // Weight should be taken from {menu_links}, not {menu_router}.
    $query->addField('ml', 'weight', 'link_weight');
    $query->fields('m');
    $query->condition('ml.mlid', $mlid);
    if ($item = $query->execute()->fetchAssoc()) {
      $item['weight'] = $item['link_weight'];
      _menu_link_translate($item);
      return $item;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
