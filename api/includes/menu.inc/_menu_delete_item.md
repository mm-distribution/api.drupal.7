# _menu_delete_item()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3097–3120 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3097-L3120)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_delete_item($item, $force = FALSE)
```

## Documentation

```text
Deletes a single menu link.

@param $item
  Item to be deleted.
@param $force
  Forces deletion. Internal use only, setting to TRUE is discouraged.

@see menu_link_delete()
```

## Code

```php
function _menu_delete_item($item, $force = FALSE) {
  $item = is_object($item) ? get_object_vars($item) : $item;
  if ($item && ($item['module'] != 'system' || $item['updated'] || $force)) {
    // Children get re-attached to the item's parent.
    if ($item['has_children']) {
      $result = db_query("SELECT mlid FROM {menu_links} WHERE plid = :plid", array(':plid' => $item['mlid']));
      foreach ($result as $m) {
        $child = menu_link_load($m->mlid);
        $child['plid'] = $item['plid'];
        menu_link_save($child);
      }
    }

    // Notify modules we are deleting the item.
    module_invoke_all('menu_link_delete', $item);

    db_delete('menu_links')->condition('mlid', $item['mlid'])->execute();

    // Update the has_children status of the parent.
    _menu_update_parental_status($item);
    menu_cache_clear($item['menu_name']);
    _menu_clear_page_cache();
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
